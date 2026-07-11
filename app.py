"""
"""
=========================================================
NEXUS AI
Intelligent Talent Intelligence Platform
Author : Naveen Kumar
=========================================================
"""

# ==========================================================
# Standard Library Imports
# ==========================================================


# ==========================================================
# Third Party Imports
# ==========================================================

import streamlit as st
import pandas as pd

# ==========================================================
# Configuration
# ==========================================================

from config import *

# ==========================================================
# UI Components
# ==========================================================

from ui.sidebar import render_sidebar

# ==========================================================
# Page Modules
# ==========================================================

from pages.dashboard import dashboard_page
from pages.resume_analyzer import resume_analyzer_page
from pages.ats_analysis import ats_analysis_page
from pages.analytics import analytics_page
from pages.ml_prediction import ml_prediction_page
from pages.deep_learning import deep_learning_page
from pages.interview import interview_page
from pages.cover_letter import cover_letter_page
from pages.learning import learning_page
from pages.executive_report import executive_report_page
from pages.recruiter_dashboard import recruiter_dashboard_page
from pages.salary_prediction import salary_prediction_page
from pages.learning_roadmap import learning_roadmap_page
from pages.ai_career_coach import ai_career_coach_page
from pages.interview_generator import interview_generator_page
from pages.email_generator import email_generator_page
# ==========================================================
# Load Custom CSS
# ==========================================================

def load_css():
    with open("assets/style.css", "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ==========================================================
# Streamlit Page Configuration
# ==========================================================

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state="expanded"
)

# ==========================================================
# Load Styles
# ==========================================================

load_css()

# ==========================================================
# Additional Custom CSS
# ==========================================================

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
""", unsafe_allow_html=True)
# -----------------------------
# Sidebar
# -----------------------------
# Imports
import streamlit as st

from ui.sidebar import render_sidebar

from pages.dashboard import dashboard_page
from pages.resume_analyzer import resume_analyzer_page
from pages.ats_analysis import ats_analysis_page

# Sidebar
menu = render_sidebar()

# Routing
if menu == "🏠 Dashboard":
    dashboard_page()

elif menu == "📄 Resume Analyzer":
    resume_analyzer_page()

# ==========================================================
# ATS Analysis
# ==========================================================

elif menu == "📊 ATS Analysis":
    ats_analysis_page()

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

elif menu == "🤖 Machine Learning":
    ml_prediction_page()

# ==========================================================
# Deep Learning
# ==========================================================

elif menu == "🧬 Deep Learning":
    deep_learning_page()

# ==========================================================
# Recruiter Dashboard
# ==========================================================
elif menu == "🎯 Recruiter Dashboard":
    recruiter_dashboard_page()

# ==========================================================
# Salary Prediction
# ==========================================================

elif menu == "💼 Salary Prediction":
    salary_prediction_page()

# ==========================================================
# Learning Roadmap
# ==========================================================

elif menu == "📚 Learning Roadmap":
    learning_roadmap_page()

# ==========================================================
# AI Career Coach
# ==========================================================

elif menu == "💬 AI Career Coach":
    ai_career_coach_page()

# ==========================================================
# Interview Generator
# ==========================================================

elif menu == "🎤 Interview Generator":
    interview_generator_page()

# ==========================================================
# Cover Letter
# ==========================================================
elif menu == "📜 Cover Letter":
    cover_letter_page()

# ==========================================================
# Email Generator
# ==========================================================
elif menu == "📧 Email Generator":
    email_generator_page()

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
    executive_report_page()

# ==========================================================
# Settings
# ==========================================================

elif menu == "⚙️ Settings":
    settings_page()