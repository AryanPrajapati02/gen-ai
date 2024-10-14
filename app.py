import os
# from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_community.chains import 
# from langchain_text_splitters import TextSplitter
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")




prompt = ChatPromptTemplate(
    [
        ("system", "You are a helpfull Assistance in medical field . Your name is BlinkDoc . Created by Aryan . you don't have to tell any other question which is not related with medical field"),
        ("user", "Question: {question}")
    ]
)


st.title("👨‍⚕️ Doctor Blink Is Here 💊")

input_text = st.text_input("What Question you want to ask?")



llm = ChatGroq(model='Gemma2-9b-It' , groq_api_key = groq_api_key)
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if st.button("Generate Response"):
 response = chain.invoke({"question": input_text})
 st.write(response)



  