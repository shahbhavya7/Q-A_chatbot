import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import os

import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith Tracking

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Simple Q&A Chatbot With Ollama"

## Prompt Template

prompt  = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant . Please  repsonse to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question, llm):
    llm = Ollama(model=llm)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser # chain basically takes the output of the prompt and passes it to the llm and then takes the output of the llm and passes it to the output parser
    answer = chain.invoke({'question': question}) # invoke is used to call the chain with the input question which will be passed to the prompt and then to the llm and then to the output parser
    return answer

# Title of the app
st.title("Enhanced Q&A Chatbot With Ollama")
llm=st.sidebar.selectbox("Select Open Source model",["gemma3"])

## Main interface for user input
st.write("Go ahead and ask any question")
user_input=st.text_input("You:")

if user_input :
    response=generate_response(user_input,llm)
    st.write(response)
else:
    st.write("Please provide the user input")