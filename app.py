import os
from dotenv import load_dotenv
from flask import Flask,request,jsonify,render_template
import json
from google import genai

load_dotenv()
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

app=Flask(__name__)

with open("faq.json","r") as f:
    faq_data=json.load(f)["faqs"]

def keyword_match(user_message):
    user_message=user_message.lower()

    for faq in faq_data:
        for keyword in faq["keywords"]:
            if keyword in user_message:
                return faq["response"]
    return None

def ask_gemini(user_message):
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Answer this question in 2-3 sentences only: {user_message}"
        )
        return response.text
    except Exception as e:
        return f"Sorry, I could not connect to AI right now. Error: {str(e)}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat",methods=["POST"])
def chat():
    data=request.get_json()
    user_message=data["message"]

    if user_message.strip()=="":
        return jsonify({"response":"please type something! I'm here to help."})

    response=keyword_match(user_message)
    
    if response is None:
        response=ask_gemini(user_message)

    return jsonify({"response":response})



if __name__ =="__main__":
    app.run(debug=True)