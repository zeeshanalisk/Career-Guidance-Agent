# 🎯 InterviewAce AI

An AI-powered Interview Preparation Assistant built using **IBM Granite Foundation Models** on **IBM watsonx.ai**.

Developed as part of the **IBM SkillsBuild / EDUNET Foundation Internship Project**.


# 📌 Project Overview

InterviewAce AI helps students and job seekers prepare for technical interviews using Generative AI.

The application provides:

- 🎤 Personalized Interview Preparation
- 📄 AI Resume Review
- 📚 Personalized Learning Roadmap
- 💼 Career Guidance

The system analyzes user input and generates structured, professional recommendations using IBM Granite Foundation Models.


# 🚀 Features

## 🎤 Interview Preparation

Generates:

- Technical Interview Questions
- HR Interview Questions
- Behavioral Questions
- Model Answers
- Interview Tips

## 📄 Resume Review

Analyzes a resume and provides:

- Strengths
- Weaknesses
- ATS Compatibility
- Missing Skills
- Resume Score
- Improvement Suggestions

## 📚 Learning Roadmap

Creates a personalized learning plan based on:

- Target Job Role
- Current Skills
- Experience Level
- Career Goals

## 💼 Career Guidance

Provides:

- Career Opportunities
- Required Skills
- Salary Expectations
- Certification Suggestions
- Portfolio Recommendations
- Job Search Tips


# 🏗 Architecture


    USER
      │
      ▼
Streamlit Web Interface
      │
      ▼
Prompt Engineering
      │
      ▼
IBM Granite Foundation Model
      │
      ▼
IBM watsonx.ai
      │
      ▼
AI Generated Response


# 🛠 Technology Stack

- Python 3.13
- Streamlit
- IBM watsonx.ai
- IBM Granite Foundation Models
- IBM Cloud
- python-dotenv
- IBM watsonx.ai Python SDK


# 📂 Project Structure


InterviewAce-AI/
│
├── app.py
├── granite_client.py
├── prompts.py
├── .env
├── requirements.txt
├── README.md
│
├── assets/
│
└── screenshots/


# ⚙ Installation

Clone the repository:

bash
git clone <repository-url>


Create a virtual environment:

bash
python -m venv .venv

Activate the environment:

### Windows

bash
.venv\Scripts\activate


Install dependencies:

bash
pip install -r requirements.txt


Create a `.env` file:

env
URL=https://us-south.ml.cloud.ibm.com
PROJECT_ID=YOUR_PROJECT_ID
MODEL_ID=ibm/granite-4-h-small
WATSONX_APIKEY=YOUR_API_KEY


Run the application:

bash
streamlit run app.py


# 📸 Screenshots

- Home Page
- Interview Preparation
- Resume Review
- Learning Roadmap
- Career Guidance


# Future Enhancements

- Resume PDF Upload
- Interview Difficulty Levels
- Interview History
- Export Results as PDF
- Multi-agent orchestration using IBM enterprise AI services


# 👨‍💻 Developed By

**Zeeshan Ali Sheikh**

IBM SkillsBuild / EDUNET Foundation Internship


# Acknowledgements

- IBM
- IBM SkillsBuild
- EDUNET Foundation
- IBM watsonx.ai
- IBM Granite Foundation Models
- IBM BOB