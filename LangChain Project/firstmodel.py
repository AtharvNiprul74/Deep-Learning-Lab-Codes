from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import streamlit as st
import os
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    google_api_key=os.getenv("Gemini_API_KEY"),
    temperature=0.7
)

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=llm,
    memory=st.session_state.memory
)

st.title("📚AI Study Evaluator")

mode = st.selectbox("Select Mode:", ["Evaluate Answer", "Improve Answer"])

user_input = st.text_area("Enter your answer / concept:")

def get_prompt(mode, text):
    if mode == "Evaluate Answer":
        return f"""
You are a strict teacher.

Evaluate the student's answer:
{text}

Give:
1. Feedback
2. Missing points
3. Score out of 10

Also suggest 3 next questions the student should ask.
"""
    else:
        return f"""
Improve the following answer and make it perfect for exams:

{text}

Also suggest 2 follow-up questions for deeper understanding.
"""

if st.button("Process") and user_input:
    prompt = get_prompt(mode, user_input)
    response = conversation.run(prompt)

    st.text_area("Result:", value=response, height=300)

if st.button("Reset"):
    st.session_state.memory.clear()