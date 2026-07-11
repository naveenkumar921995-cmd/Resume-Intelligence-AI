"""
=========================================================
NEXUS AI
Intelligent Talent Intelligence Platform
Author : Naveen Kumar
=========================================================
"""

import streamlit as st
import pandas as pd
def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

from config import *

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS
# -----------------------------

st.markdown("""
<style>

.main{
    padding-top:1rem;
}

.block-container{
    padding-top:2rem;
}

.metric-card{
    background:#f8fafc;
    padding:20px;
    border-radius:12px;
    border:1px solid #e5e7eb;
}

.big-font{
    font-size:28px;
    font-weight:bold;
}

.small-font{
    color:gray;
}

</style>
""",unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
from ui.sidebar import render_sidebar

menu = render_sidebar()
# -----------------------------
# Dashboard
# -----------------------------
from pages.dashboard import dashboard_page
if menu == "🏠 Dashboard":
    dashboard_page()
# ==========================================================
# Resume Analyzer
# ==========================================================
from pages.resume_analyzer import resume_analyzer_page

elif menu == "📄 Resume Analyzer":
    resume_analyzer_page()
# ==========================================================
# ATS Analysis
# ==========================================================

elif menu == "📊 ATS Analysis":

    st.header("📊 ATS Resume Analysis")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=SUPPORTED_FILES,
        key="ats"
    )

    if uploaded_file:

        from core.resume_parser import parse_resume
        from core.keyword_engine import KeywordEngine

        resume = parse_resume(uploaded_file)

        engine = KeywordEngine()

        score = engine.ats_score(resume)

        metric_card("ATS Score", ats_score)

        st.progress(score/100)

# ==========================================================
# NLP
# ==========================================================

elif menu == "🧠 NLP Analysis":

    st.header("🧠 NLP Resume Similarity")

    st.info("Compare Resume vs Job Description")

    resume = st.text_area("Resume")

    jd = st.text_area("Job Description")

    if st.button("Calculate Similarity"):

        from core.similarity_engine import SimilarityEngine

        sim = SimilarityEngine()

        score = sim.calculate_similarity(
            resume,
            jd
        )

        st.metric(
            "Similarity",
            f"{score:.2f}%"
        )

# ==========================================================
# EDA
# ==========================================================

elif menu == "📈 EDA Dashboard":

    from core.analytics import Analytics

    st.header("📈 Resume Analytics")

    analytics = Analytics()

    analytics.dashboard()

# ==========================================================
# Machine Learning
# ==========================================================
from core.ml_prediction import MLPredictor

st.header("🤖 Machine Learning Prediction")

ml = MLPredictor()

comparison = ml.train_models()

st.subheader("📊 Model Comparison")

st.dataframe(
    comparison,
    use_container_width=True
)

st.divider()

st.subheader("Predict Hiring Score")

experience = st.slider("Experience",0,20,3)

skills = st.slider("Skills",0,40,15)

education = st.slider("Education Level",1,5,3)

projects = st.slider("Projects",0,20,5)

certifications = st.slider("Certifications",0,15,2)

model = st.selectbox(

    "Select Model",

    comparison["Model"]

)

if st.button("Predict"):

    score = ml.predict(

        experience,

        skills,

        education,

        projects,

        certifications,

        model

    )

    st.metric(

        "Predicted Hiring Score",

        f"{score}%"

    )

# ==========================================================
# Deep Learning
# ==========================================================
elif menu == "🧬 Deep Learning":

    from core.deep_learning import DeepLearningModel

    st.header("🧬 Deep Learning Hiring Prediction")

    dl = DeepLearningModel()

    experience = st.slider("Experience",0,20,4)

    skills = st.slider("Skills",0,40,15)

    projects = st.slider("Projects",0,20,5)

    education = st.slider("Education",1,5,3)

    certifications = st.slider("Certifications",0,15,2)

    if st.button("Predict using Neural Network"):

        report = dl.full_report(

            experience,

            skills,

            projects,

            education,

            certifications

        )

        st.metric(

            "Hiring Score",

            f"{report['Hiring Score']}%"

        )

        st.success(

            f"Confidence : {report['Confidence']}"

        )

        st.info(

            report["Recommendation"]

        )
# ==========================================================
# Recruiter Dashboard
# ==========================================================

elif menu == "🎯 Recruiter Dashboard":

    st.header("🎯 Recruiter Dashboard")

    st.success(
        "Upload multiple resumes to compare candidates."
    )

# ==========================================================
# Salary Prediction
# ==========================================================

elif menu == "💼 Salary Prediction":

    st.header("💼 Salary Prediction")

    exp = st.slider(
        "Experience",
        0,
        20,
        2
    )

    st.metric(
        "Estimated Salary",
        f"₹ {5+exp*2} LPA"
    )
    # ==========================================================
# Learning Roadmap
# ==========================================================

elif menu == "📚 Learning Roadmap":

    from core.learning_recommender import LearningRecommender

    st.header("📚 AI Learning Roadmap")

    lr = LearningRecommender()

    df = lr.learning

    st.dataframe(
        df,
        use_container_width=True
    )

# ==========================================================
# AI Career Coach
# ==========================================================

elif menu == "💬 AI Career Coach":

    from core.llm_engine import AIResumeCoach

    st.header("💬 AI Career Coach")

    resume = st.text_area("Paste Resume")

    if st.button("Review Resume"):

        coach = AIResumeCoach()

        st.write(
            coach.review(resume)
        )

# ==========================================================
# Interview Generator
# ==========================================================

elif menu == "🎤 Interview Generator":

    from core.interview_generator import InterviewGenerator

    st.header("🎤 AI Interview Questions")

    role = st.text_input("Target Role")

    if st.button("Generate"):

        generator = InterviewGenerator()

        questions = generator.generate(role)

        for q in questions:

            st.write("•", q)

# ==========================================================
# Cover Letter
# ==========================================================

elif menu == "📜 Cover Letter":

    from core.cover_letter import CoverLetterGenerator

    st.header("📜 Cover Letter")

    name = st.text_input("Name")

    company = st.text_input("Company")

    role = st.text_input("Role")

    if st.button("Generate Cover Letter"):

        cover = CoverLetterGenerator()

        st.text_area(

            "",

            cover.generate(

                name,

                company,

                role

            ),

            height=350

        )

# ==========================================================
# Email Generator
# ==========================================================

elif menu == "📧 Email Generator":

    from core.email_generator import EmailGenerator

    st.header("📧 HR Email Generator")

    name = st.text_input("Candidate")

    company = st.text_input("Company")

    role = st.text_input("Role")

    if st.button("Generate Email"):

        email = EmailGenerator()

        st.text_area(

            "",

            email.application_email(

                name,

                company,

                role

            ),

            height=300

        )

# ==========================================================
# LinkedIn Optimizer
# ==========================================================

elif menu == "👤 LinkedIn Optimizer":

    st.header("👤 LinkedIn Profile Optimizer")

    st.info("Coming in Version 8.1")

# ==========================================================
# GitHub Portfolio
# ==========================================================

elif menu == "💻 GitHub Portfolio":

    st.header("💻 GitHub Analyzer")

    st.info("Coming in Version 8.2")

# ==========================================================
# Executive Report
# ==========================================================

elif menu == "📑 Executive Report":

    st.header("📑 Executive AI Report")

    from core.report_generator import ReportGenerator

    if st.button("Generate Sample Report"):

        generator = ReportGenerator()

        pdf = generator.generate_report(

            candidate_name="Naveen Kumar",

            department="Data Science",

            job_role="Data Analyst",

            ats_score=88,

            matched_skills=["Python","Pandas","SQL"],

            missing_skills=["Power BI","AWS"],

            ml_score=91,

            dl_score=93,

            recommendation="Excellent candidate with strong analytical skills.",

            statistics={

                "Words":620,

                "Characters":4200,

                "Sentences":41,

                "Lines":86

            }

        )

        with open(pdf, "rb") as file:

            st.download_button(

                "📄 Download AI Report",

                file,

                file_name="Resume_Report.pdf",

                mime="application/pdf"

            )
st.success("Report Generated Successfully!")

# ==========================================================
# Settings
# ==========================================================

elif menu == "⚙ Settings":

    st.header("⚙ Settings")

    st.write("Application Version :", APP_VERSION)

    st.write("Developed By :", "Naveen Kumar")
st.markdown("---")
st.caption("NEXUS AI | Version 1.0.0")