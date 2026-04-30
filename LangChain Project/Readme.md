# 📚 AI Study Evaluator

---

## 📌 Overview

AI Study Evaluator is a Streamlit-based application that uses **LangChain and Google Gemini (LLM)** to evaluate and improve student answers.

It acts like a virtual teacher by providing feedback, identifying missing points, and suggesting improvements.

---

## 🚀 Features

- Evaluate student answers with detailed feedback.  
- Provide score out of 10.  
- Identify missing concepts.  
- Improve answers to make them exam-ready.
- Suggest follow-up questions for deeper understanding.  
- Maintain conversation context using memory. 

---

## ⚙️ Working

The application integrates:

- **LangChain** for managing LLM workflows  
- **Gemini 2.5 Flash Lite** for fast response generation  
- **ConversationBufferMemory** to retain context  
- **Prompt Engineering** for evaluation and improvement  
- **Streamlit** for user interface  

---

## 🧠 Modes

### 🔹 Evaluate Answer
- Acts like a strict teacher  
- Gives:
  - Feedback  
  - Missing points  
  - Score out of 10  
  - Next questions  

---

### 🔹 Improve Answer
- Enhances the answer quality  
- Makes it suitable for exams  
- Suggests follow-up questions  

---

## 🛠️ Tech Stack

- Python  
- LangChain  
- Google Gemini API  
- Streamlit  
- Python-dotenv  

---

## 🔐 Environment Variable

Create a `.env` file and add:
Gemini_API_KEY=your_api_key_here
---

## ▶️ Run the Project

```bash
pip install langchain langchain-google-genai streamlit python-dotenv

streamlit run firstmodel.py
