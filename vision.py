from dotenv import load_dotenv
load_dotenv() #Loading all environment variables

import streamlit as sl
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load gemini model and get responses
model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(prompt, image):
    if input !="":
        response = model.generate_content([prompt,image])
    else:
        response = model.generate_content(image)
    return response.text

from PIL import Image
#StreamLit app

sl.set_page_config(page_title="Gemini Image Demo")
sl.header("Gemini  Application")
input=sl.text_input("Input: ",key="input")
img_file_buffer = sl.file_uploader('Upload an image', type=['jpg','jpeg''png'])
image=""
if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    sl.image(image,caption="Uploaded Image", use_column_width=True)
submit=sl.button("Tell me about the image")

#On clicking submit

if submit:
    response=get_gemini_response(input,image)
    sl.subheader("Response")
    sl.write(response)
    