"""
=========================================================
NEXUS AI
Enterprise Dashboard
Version : 10.0 Enterprise
Author : Naveen Kumar
=========================================================
"""

import streamlit as st
import pandas as pd

from config import (
    TOTAL_DEPARTMENTS,
    TOTAL_JOB_ROLES,
    TOTAL_SKILLS,
    TOTAL_AI_MODULES,
)


def dashboard_page():

    st.title("🚀 NEXUS AI Enterprise")

    st.caption("Resume Intelligence Platform • Version 10 Enterprise")

    st.markdown("""
## AI Powered Resume Intelligence Platform

Analyze, Rank and Optimize resumes using:

- ATS Analysis
- NLP Engine
- Machine Learning
- Deep Learning
- LLM Career Coach
- Recruiter Intelligence
- Resume Analytics
- Skill Gap Detection
- AI Recommendations
""")

    st.divider()

    # =====================================
    # KPI Dashboard
    # =====================================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Departments",
        TOTAL_DEPARTMENTS
    )

    c2.metric(
        "Job Roles",
        TOTAL_JOB_ROLES
    )

    c3.metric(
        "Skills",
        TOTAL_SKILLS
    )

    c4.metric(
        "AI Modules",
        TOTAL_AI_MODULES
    )

    st.divider()

    # =====================================
    # AI Engine Status
    # =====================================

    st.subheader("🟢 AI Engine Status")

    col1, col2 = st.columns(2)

    with col1:

        st.success("Resume Parser")

        st.success("ATS Engine")

        st.success("Analytics Engine")

        st.success("Machine Learning")

        st.success("Deep Learning")

    with col2:

        st.success("LLM Engine")

        st.success("Career Coach")

        st.success("Recruiter Dashboard")

        st.success("Report Generator")

        st.success("PDF Export")

    st.divider()

    # =====================================
    # Quick Actions
    # =====================================

    st.subheader("⚡ Quick Actions")

    a1, a2, a3, a4 = st.columns(4)

    with a1:
        st.info("📄 Resume Analyzer")

    with a2:
        st.info("🤖 ML Prediction")

    with a3:
        st.info("🧠 AI Career Coach")

    with a4:
        st.info("📈 Analytics")

    st.divider()

    # =====================================
    # Platform Modules
    # =====================================

    st.subheader("🏆 Enterprise Modules")

    modules = pd.DataFrame({

        "Module":[

            "Resume Parser",

            "ATS Analyzer",

            "Analytics",

            "Machine Learning",

            "Deep Learning",

            "AI Career Coach",

            "Recruiter Dashboard",

            "Report Generator",

            "Resume Ranking",

            "Skill Gap Analysis",

            "Interview Generator",

            "Cover Letter Generator"

        ],

        "Status":[

            "✅ Ready",

            "✅ Ready",

            "✅ Ready",

            "✅ Ready",

            "✅ Ready",

            "✅ Ready",

            "🚧 Upgrading",

            "🚧 Upgrading",

            "🚧 Upgrading",

            "🚧 Upgrading",

            "🚧 Upgrading",

            "🚧 Upgrading"

        ]

    })

    st.dataframe(
        modules,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # =====================================
    # Technology Stack
    # =====================================

    st.subheader("💻 Technology Stack")

    tech = pd.DataFrame({

        "Category":[

            "Programming",

            "Analytics",

            "Machine Learning",

            "Deep Learning",

            "LLM",

            "Visualization",

            "Deployment"

        ],

        "Technology":[

            "Python",

            "Pandas • NumPy",

            "Scikit-Learn",

            "TensorFlow",

            "OpenAI • Ollama • Gemini",

            "Plotly",

            "Streamlit"

        ]

    })

    st.dataframe(

        tech,

        hide_index=True,

        use_container_width=True

    )

    st.divider()

    # =====================================
    # Enterprise Workflow
    # =====================================

    st.subheader("📊 Enterprise Workflow")

    st.code("""

Upload Resume
      │
      ▼
Resume Parsing
      │
      ▼
ATS Analysis
      │
      ▼
NLP Processing
      │
      ▼
Machine Learning
      │
      ▼
Deep Learning
      │
      ▼
Resume Ranking
      │
      ▼
Skill Gap Detection
      │
      ▼
AI Recommendation
      │
      ▼
Professional PDF Report

""")

    st.divider()

    # =====================================
    # Platform Version
    # =====================================

    st.success("NEXUS AI Enterprise Platform")

    st.caption("""
Version : 10.0 Enterprise

Author : Naveen Kumar

Enterprise Resume Intelligence Platform
""")