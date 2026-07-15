"""
=========================================================
NEXUS AI
Dashboard Page
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

    st.title("🤖 NEXUS AI")

    st.markdown("""
### Enterprise AI Career Intelligence Platform

Analyze resumes using:

- ATS Analysis
- NLP
- Machine Learning
- Deep Learning
- AI Career Guidance
- Skill Gap Analysis
- Recruiter Intelligence
- Learning Recommendation
- Resume Intelligence

---
""")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Departments", TOTAL_DEPARTMENTS)
    c2.metric("Job Roles", TOTAL_JOB_ROLES)
    c3.metric("Skills", TOTAL_SKILLS)
    c4.metric("AI Modules", TOTAL_AI_MODULES)

    st.divider()

    st.subheader("Technology Stack")

    tech = pd.DataFrame({
        "Category": [
            "Programming",
            "Analytics",
            "Machine Learning",
            "Deep Learning",
            "Natural Language Processing",
            "Generative AI",
            "Visualization",
            "Deployment"
        ],
        "Technology": [
            "Python",
            "NumPy • Pandas",
            "Scikit-learn",
            "TensorFlow",
            "Regex • TF-IDF • spaCy",
            "OpenAI • Ollama • Gemini",
            "Matplotlib • Plotly",
            "Streamlit"
        ]
    })

    st.dataframe(
        tech,
        hide_index=True,
        use_container_width=True
    )

    st.divider()

    st.subheader("Platform Features")

    col1, col2 = st.columns(2)

    with col1:
        st.success("Resume Parsing")
        st.success("ATS Resume Analysis")
        st.success("Skill Gap Analysis")
        st.success("Resume Ranking")
        st.success("Department-wise Analysis")
        st.success("Learning Recommendation")
        st.success("Interview Questions")

    with col2:
        st.success("Machine Learning")
        st.success("Deep Learning")
        st.success("NLP Similarity")
        st.success("AI Resume Review")
        st.success("Cover Letter Generator")
        st.success("Email Generator")
        st.success("Recruiter Dashboard")

    st.divider()

    st.subheader("Platform Workflow")

    st.markdown("""
```text
Upload Resume
      │
      ▼
Resume Parsing
      │
      ▼
Feature Engineering
      │
      ▼
ATS Analysis
      │
      ▼
NLP Similarity
      │
      ▼
Machine Learning
      │
      ▼
Deep Learning
      │
      ▼
Skill Gap Analysis
      │
      ▼
AI Recommendation
      │
      ▼
Executive Report
""")