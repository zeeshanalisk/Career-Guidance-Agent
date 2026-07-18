import streamlit as st
from granite_client import generate_response
from prompts import PROMPTS

st.set_page_config(
    page_title="InterviewAce AI",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.title("🎯 InterviewAce AI")
st.caption("Agentic Interview Preparation Assistant powered by IBM Granite")


with st.sidebar:

    st.title("🎯 InterviewAce AI")

    st.markdown("---")

    feature = st.radio(
        "Choose a Feature",
        [
            "🏠 Home",
            "🎤 Interview Preparation",
            "📄 Resume Review",
            "📚 Learning Roadmap",
            "💼 Career Guidance"
        ]
    )

    st.markdown("---")

    st.success("✅ IBM Granite Connected")

    st.info("Powered by IBM watsonx.ai")


if feature == "🏠 Home":

    st.header("Welcome to InterviewAce AI 👋")

    st.write("""
InterviewAce AI is an AI-powered interview preparation platform built using IBM Granite Foundation Models on IBM watsonx.ai.

### 🚀 Features

- 🎤 Personalized Interview Preparation
- 📄 AI Resume Review
- 📚 Personalized Learning Roadmap
- 💼 Career Guidance

### ⚙️ Technology Stack

- IBM Granite Foundation Models
- IBM watsonx.ai
- IBM Cloud
- Python
- Streamlit

### 📌 Workflow

Profile ➜ IBM Granite ➜ AI Analysis ➜ Personalized Recommendations
""")


elif feature == "🎤 Interview Preparation":

    st.header("🎤 Interview Preparation")

    with st.form("interview_form"):

        name = st.text_input("Your Name")

        job_role = st.text_input("Target Job Role")

        experience = st.selectbox(
            "Experience",
            [
                "Fresher",
                "0-2 Years",
                "2-5 Years",
                "5+ Years"
            ]
        )

        skills = st.text_area(
            "Skills (comma separated)",
            placeholder="Python, SQL, Flask, Git"
        )

        submitted = st.form_submit_button("🚀 Generate Interview")

    if submitted:

        prompt = f"""
{PROMPTS["Interview Preparation"]}

Name:
{name}

Target Job Role:
{job_role}

Experience:
{experience}

Skills:
{skills}
"""

        with st.spinner("IBM Granite is preparing your interview..."):

            response = generate_response(prompt)

        st.success("Interview generated successfully!")

        st.balloons()

        st.markdown(response)


elif feature == "📄 Resume Review":

    st.header("📄 Resume Review")

    with st.form("resume_form"):

        resume_text = st.text_area(
            "Paste your Resume",
            height=350,
            placeholder="Paste your resume here..."
        )

        review = st.form_submit_button("📄 Analyze Resume")

    if review:

        prompt = f"""
{PROMPTS["Resume Review"]}

Resume:

{resume_text}
"""

        with st.spinner("Analyzing resume using IBM Granite..."):

            response = generate_response(prompt)

        st.success("Resume analysis completed!")

        st.balloons()

        st.markdown(response)


elif feature == "📚 Learning Roadmap":

    st.header("📚 AI Learning Roadmap")

    with st.form("roadmap_form"):

        role = st.text_input("Target Job Role")

        experience = st.selectbox(
            "Experience",
            [
                "Fresher",
                "0-2 Years",
                "2-5 Years",
                "5+ Years"
            ]
        )

        current_skills = st.text_area(
            "Current Skills",
            placeholder="Python\nSQL\nGit"
        )

        goal = st.text_input(
            "Career Goal",
            placeholder="Become an AI Engineer"
        )

        submit = st.form_submit_button("📚 Generate Roadmap")

    if submit:

        prompt = f"""
{PROMPTS["Learning Roadmap"]}

Target Role:
{role}

Experience:
{experience}

Current Skills:
{current_skills}

Career Goal:
{goal}
"""

        with st.spinner("Generating personalized roadmap..."):

            response = generate_response(prompt)

        st.success("Roadmap generated!")

        st.balloons()

        st.markdown(response)


elif feature == "💼 Career Guidance":

    st.header("💼 AI Career Guidance")

    with st.form("career_form"):

        education = st.text_input(
            "Education",
            placeholder="BCA 3rd Year"
        )

        target_role = st.text_input(
            "Target Job Role",
            placeholder="AI Engineer"
        )

        skills = st.text_area(
            "Current Skills",
            placeholder="Python\nSQL\nGit"
        )

        interests = st.text_area(
            "Interests",
            placeholder="Machine Learning, Data Science"
        )

        submit = st.form_submit_button("💼 Get Career Guidance")

    if submit:

        prompt = f"""
{PROMPTS["Career Guidance"]}

Education:
{education}

Target Job Role:
{target_role}

Current Skills:
{skills}

Interests:
{interests}
"""

        with st.spinner("Generating career guidance..."):

            response = generate_response(prompt)

        st.success("Career guidance generated!")

        st.balloons()

        st.markdown(response)

st.markdown("---")

st.caption(
    "🚀 Powered by IBM Granite | IBM watsonx.ai | Streamlit | EDUNET Foundation Internship Project"
)