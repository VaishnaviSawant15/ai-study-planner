import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("🤖 AI Study / Interview Assistant")

role = st.text_input("Enter Job Role")

if "question" not in st.session_state:
    st.session_state.question = ""

if st.button("Generate Question"):
    if role:
        prompt = f"Generate one interview question for {role}"
        response = model.generate_content(prompt)
        st.session_state.question = response.text

if st.session_state.question:
    st.subheader("Question")
    st.write(st.session_state.question)