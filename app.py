from flask import Flask, render_template, request
from google import genai
import os

app = Flask(__name__)

# Get Gemini API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. Please set the environment variable first."
    )

client = genai.Client(api_key=api_key)


@app.route("/", methods=["GET", "POST"])
def home():

    response = None

    if request.method == "POST":

        selected_function = request.form.get("function")
        user_input = request.form.get("user_input", "").strip()

        if not user_input:
            response = "⚠️ Please enter some text first."

        else:

            # -------------------------
            # QUESTION ANSWERING
            # -------------------------
            if selected_function == "question":

                prompt = f"""
You are a helpful educational AI assistant.

Answer the following question accurately and clearly.

Instructions:
- Use simple language suitable for a college student.
- Explain important concepts properly.
- Use headings where useful.
- Use bullet points when appropriate.
- Give examples where they help understanding.
- Format the response using Markdown.

Question:
{user_input}
"""

            # -------------------------
            # SUMMARIZATION
            # -------------------------
            elif selected_function == "summary":

                prompt = f"""
You are a helpful AI summarization assistant.

Summarize the following text clearly and concisely.

Instructions:
- Keep all important information.
- Remove unnecessary repetition.
- Use simple and easy-to-understand language.
- Organize key information using bullet points.
- Use Markdown formatting.

Text:
{user_input}
"""

            # -------------------------
            # CREATIVE CONTENT
            # -------------------------
            elif selected_function == "creative":

                prompt = f"""
You are a creative writing assistant.

Create high-quality creative content based on the user's request.

Instructions:
- Make the content interesting and engaging.
- Follow the user's requirements carefully.
- Keep the writing clear and well structured.
- Use Markdown formatting where appropriate.

Request:
{user_input}
"""

            else:
                prompt = None
                response = "⚠️ Please select a valid function."

            # -------------------------
            # GEMINI API CALL
            # -------------------------
            if prompt:

                try:

                    ai_response = client.models.generate_content(
                        model="gemini-3.5-flash-lite",
                        contents=prompt
                    )

                    if ai_response.text:
                        response = ai_response.text
                    else:
                        response = (
                            "⚠️ The AI did not return a response. "
                            "Please try again."
                        )

                except Exception as e:

                    error_message = str(e)

                    # Handle API quota / rate-limit errors
                    if (
                        "429" in error_message
                        or "RESOURCE_EXHAUSTED" in error_message
                        or "quota" in error_message.lower()
                    ):
                        response = """
## ⚠️ AI Usage Limit Reached

The Gemini API usage limit has temporarily been reached.

Please wait for the API quota to reset and try again later.

Your AI Assistant is working correctly — this is a temporary
API usage limitation.
"""

                    # Other Gemini/API errors
                    else:
                        print(f"Gemini API Error: {error_message}")

                        response = """
## ⚠️ Something went wrong

The AI service is temporarily unavailable.

Please try again in a few moments.
"""

    return render_template(
        "index.html",
        response=response
    )


if __name__ == "__main__":
    app.run(debug=True)