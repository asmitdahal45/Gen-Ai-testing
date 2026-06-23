import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_ai(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are an academic performance analyst."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


st.title("📊 Student Performance Analyzer")

name = st.text_input("Student Name")
marks = st.number_input("Average Marks", 0, 100)
attendance = st.number_input("Attendance %", 0, 100)

if st.button("Analyze Performance 🚀"):

    prompt = f"""
    Student Name: {name}
    Marks: {marks}/100
    Attendance: {attendance}%

    Provide:
    1. Performance level (Weak/Good/Excellent)
    2. Prediction of future result
    3. Weak areas
    4. Improvement tips
    5. Motivation message
    """

    result = ask_ai(prompt)
    st.success("Analysis Result")
    st.write(result)