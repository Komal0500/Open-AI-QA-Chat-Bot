from langchain.llms import OpenAI 
import os 
os.environ["OPEN_API_KEY"]="YOUR_API_KEY"
#llm=OpenAI(openai_api_key=os.environ["OPEN_API_KEY"],temperature=0.6) 
from langchain.llms import OpenAI


import streamlit as st
import os


## Function to load OpenAI model and get respones

def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.environ["OPEN_API_KEY"],model_name="text-davinci-003",temperature=0.5)
    response=llm(question)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input=st.text_input("Input: ",key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)
