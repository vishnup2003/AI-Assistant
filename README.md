# AI Assistant – Prompt Engineering Application

AI Assistant is a web-based application developed using Python and Flask that integrates the Google Gemini API to perform multiple AI-powered tasks.

## Features

- Answer Questions
- Summarize Text
- Generate Creative Content
- Task-specific prompt engineering
- Modern and responsive user interface
- Copy AI responses
- Clear generated responses
- Download AI responses

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Google Gemini API
- Google GenAI Python SDK

## Project Structure

AI_Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

## Installation

1. Clone or download the project.

2. Create a virtual environment:

   python -m venv venv

3. Activate the virtual environment on Windows:

   .\venv\Scripts\Activate.ps1

4. Install the required packages:

   pip install -r requirements.txt

5. Set your Gemini API key as an environment variable:

   $env:GEMINI_API_KEY="YOUR_API_KEY"

6. Run the Flask application:

   python app.py

7. Open the application in your browser:

   http://127.0.0.1:5000

## How It Works

1. The user selects an AI function.
2. The user enters a question, text, or creative request.
3. Flask receives the input.
4. A task-specific prompt is created.
5. The prompt is sent to the Gemini model using the Gemini API.
6. Gemini generates an AI response.
7. The generated response is displayed on the web interface.

## Prompt Engineering

Different prompt instructions are used according to the selected task.

### Question Answering
The AI is instructed to provide accurate and easy-to-understand educational answers.

### Text Summarization
The AI is instructed to identify important information and produce a concise summary.

### Creative Content
The AI is instructed to generate engaging and relevant creative content according to the user's request.

## Security

The Gemini API key is stored as an environment variable and is not included directly in the source code.

## Author
Vishnu Shankar Pathak