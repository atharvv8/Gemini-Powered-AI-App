from dotenv import load_dotenv
load_dotenv() #Loading all environment variables

import streamlit as sl
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load gemini model and get responses
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(prompt):
    response = model.generate_content(prompt)
    return response.text

#StreamLit app

sl.set_page_config(page_title="Q&A Demo")
sl.header("Gemini LLM App")
input=sl.text_input("Input: ",key="input")
submit=sl.button("Enter prompt")
#On clicking submit

if submit:
    response=get_gemini_response(input)
    sl.subheader("Response")
    sl.write(response)
    
    