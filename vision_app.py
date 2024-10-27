from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from PIL import Image
load_dotenv()
st.set_page_config(page_title="QnA Demo")
st.header("Gemini LIM Application")
api_key = st.sidebar.text_input("Enter the Google API key: ", type='password')
genai.configure(api_key = api_key)
## Fuction to load the Gemini pro model and get responses
model = genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(inputs,image):
    if inputs != '':
        response = model.generate_content([inputs,image])
    else:
        response = model.generate_content(image)
    return response.text


inputs = st.text_input("Input Prompt: ", key = "inputs")

if api_key:
    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
    image = ""
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

    submit = st.button("Tell me about the image")

    if submit:
        response = get_gemini_response(inputs, image)
        st.subheader("The Response is: ")
        st.write(response)
    
