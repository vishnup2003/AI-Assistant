from flask import Flask, render_template, request
from google import genai
import os

app = Flask(__name__)

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
            response = "Please enter some text first."

        else:

            if selected_function == "question":

                prompt = f"""
You are a helpful educational AI assistant.

Answer the following question accurately and clearly.
Use simple language suitable for a college student.
Explain important concepts properly and give examples where useful.

Question:
{user_input}
"""

            elif selected_function == "summary":

                prompt = f"""
You are a helpful AI summarization assistant.

Summarize the following text clearly and concisely.
Keep all important information.
Remove unnecessary repetition.
Use simple and easy-to-understand language.

Text:
{user_input}
"""

            elif selected_function == "creative":

                prompt = f"""
You are a creative writing assistant.

Create high-quality creative content based on the following user request.
Make the content interesting, clear, and appropriate for the user's request.

Request:
{user_input}
"""

            else:
                prompt = None
                response = "Please select a valid function."

            if prompt:
                try:
                    ai_response = client.models.generate_content(
                        model="gemini-3-flash-preview",
                        contents=prompt
                    )

                    response = ai_response.text

                except Exception as e:
                    response = "Error: " + str(e)

    return render_template(
        "index.html",
        response=response
    )


if __name__ == "__main__":
    app.run(debug=True)