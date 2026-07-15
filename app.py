"""
=========================================================
NEXUS AI
Intelligent Talent Intelligence Platform
Author : Naveen Kumar
Version : 9.0 Enterprise
=========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import streamlit as st

from config import (
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
)

from ui.sidebar import render_sidebar

# ==========================================================
# Page Imports
# ==========================================================

from pages.dashboard import dashboard_page
from pages.resume_analyzer import resume_analyzer_page
from pages.ats_analysis import ats_analysis_page
from pages.nlp_analysis import nlp_analysis_page
from pages.analytics import analytics_page
from pages.ml_prediction import ml_prediction_page
from pages.deep_learning import deep_learning_page
from pages.recruiter_dashboard import recruiter_dashboard_page
from pages.salary_prediction import salary_prediction_page
from pages.learning_roadmap import learning_roadmap_page
from pages.ai_career_coach import ai_career_coach_page
from pages.interview_generator import interview_generator_page
from pages.cover_letter import cover_letter_page
from pages.email_generator import email_generator_page
from pages.executive_report import executive_report_page
from pages.settings import settings_page

# ==========================================================
# Streamlit Configuration
# ==========================================================

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state="expanded"
)

# ==========================================================
# Load Custom CSS
# ==========================================================

def load_css():

    try:

        with open(
            "assets/style.css",
            "r",
            encoding="utf-8"
        ) as css:

            st.markdown(
                f"<style>{css.read()}</style>",
                unsafe_allow_html=True
            )

    except FileNotFoundError:

        pass


load_css()

# ==========================================================
# Sidebar
# ==========================================================

menu = render_sidebar()
return menu

# ==========================================================
# Routing Dictionary
# ==========================================================

PAGE_ROUTES = {

    "🏠 Dashboard":
        dashboard_page,

    "📄 Resume Analyzer":
        resume_analyzer_page,

    "📊 ATS Analysis":
        ats_analysis_page,

    "🧠 NLP Analysis":
        nlp_analysis_page,

    "📈 EDA Dashboard":
        analytics_page,

    "🤖 Machine Learning":
        ml_prediction_page,

    "🧬 Deep Learning":
        deep_learning_page,

    "🎯 Recruiter Dashboard":
        recruiter_dashboard_page,

    "💼 Salary Prediction":
        salary_prediction_page,

    "📚 Learning Roadmap":
        learning_roadmap_page,

    "💬 AI Career Coach":
        ai_career_coach_page,

    "🎤 Interview Generator":
        interview_generator_page,

    "📜 Cover Letter":
        cover_letter_page,

    "📧 Email Generator":
        email_generator_page,

    "📑 Executive Report":
        executive_report_page,

    "⚙️ Settings":
        settings_page,
}

# ==========================================================
# Run Selected Page
# ==========================================================

if menu in PAGE_ROUTES:

    PAGE_ROUTES[menu]()

# ==========================================================
# Future Modules
# ==========================================================

elif menu == "👤 LinkedIn Optimizer":

    st.header("👤 LinkedIn Profile Optimizer")

    st.info(
        "Coming in Version 9.1"
    )

elif menu == "💻 GitHub Portfolio":

    st.header("💻 GitHub Portfolio Analyzer")

    st.info(
        "Coming in Version 9.2"
    )

# ==========================================================
# Unknown Route
# ==========================================================

else:

    st.error(
        "Unknown page selected."
    )