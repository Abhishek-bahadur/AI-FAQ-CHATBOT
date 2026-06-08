# AI FAQ Chatbot 🤖

  An AI-Powered FAQ Chatbot built with Python, Flask, and Google Gemini API.

## Built by
  Abhishek Bahadur — B.Tech (IT)

## Tech Stack
  - Python
  - Flask
  - Google Gemini API (google-genai SDK)
  - HTML + CSS + JavaScript

## How it works
  1. User types a question in the chat interface
  2. Bot first checks a local FAQ database using keyword matching
  3. If no match found — calls Google Gemini AI for an intelligent response

## How to run locally
  1. Clone the repo
  2. Install dependencies: pip install -r requirements.txt
  3. Add your Gemini API key in a .env file: GEMINI_API_KEY=your_key
  4. Run: python app.py
  5. Open: http://localhost:5000
