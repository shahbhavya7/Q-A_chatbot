import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Simple Q&A Chatbot With Gemini"


# Set Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini Response Generator Function
def generate_response(question, model_name="gemini-pro"):
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(question)
    return response.text

# Streamlit App Title
st.title("Enhanced Q&A Chatbot With Gemini")

# Selectbox for model (currently only gemini-pro available via API)
llm = st.sidebar.selectbox("Select Gemini Model", ["gemini-2.0-flash"])

# User prompt
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

# Response
if user_input:
    response = generate_response(user_input, llm)
    st.write(response)
else:
    st.write("Please provide the user input")
