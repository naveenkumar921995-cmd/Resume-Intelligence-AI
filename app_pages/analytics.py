"""
=========================================================
NEXUS AI
Enterprise Resume Analytics Dashboard
Author : Naveen Kumar
Version : 9.1 Enterprise
=========================================================
"""

import streamlit as st
from core.ai_engine import AIEngine


def analytics_page():

    st.title("📈 Resume Analytics Dashboard")

    st.markdown(
        "Enterprise Resume Analytics powered by the AI Engine."
    )

    engine = AIEngine()

    st.divider()

    # =====================================================
    # Candidate Information
    # =====================================================

    st.subheader("Candidate Information")

    col1, col2 = st.columns(2)

    with col1:

        experience = st.slider(
            "Years of Experience",
            0,
            20,
            3,
            key="analytics_experience"
        )

        projects = st.number_input(
            "Projects",
            0,
            50,
            5,
            key="analytics_projects"
        )

        certifications = st.number_input(
            "Certifications",
            0,
            20,
            2,
            key="analytics_certifications"
        )

    with col2:

        resume_words = st.number_input(
            "Resume Word Count",
            100,
            5000,
            600,
            key="analytics_words"
        )

        resume_score = st.slider(
            "Resume Quality Score",
            0,
            100,
            80,
            key="analytics_score"
        )

    st.divider()

    # =====================================================
    # Skill Analysis
    # =====================================================

    st.subheader("Skill Analysis")

    matched = st.multiselect(

        "Matched Skills",

        [
            "Python",
            "SQL",
            "Pandas",
            "NumPy",
            "Machine Learning",
            "Deep Learning",
            "Power BI",
            "Excel",
            "AWS",
            "Docker",
        ],

        default=[
            "Python",
            "SQL",
            "Machine Learning",
        ],

        key="analytics_matched"

    )

    missing = st.multiselect(

        "Missing Skills",

        [
            "AWS",
            "Docker",
            "Kubernetes",
            "CI/CD",
            "TensorFlow",
            "Power BI",
            "Azure",
        ],

        default=[
            "AWS",
            "Docker",
        ],

        key="analytics_missing"

    )

    st.divider()

    # =====================================================
    # Generate Analytics
    # =====================================================

    if st.button(
        "🚀 Generate Analytics",
        use_container_width=True
    ):

        analytics = engine.analytics

        features = {

            "Experience": experience,

            "Projects": projects,

            "Certifications": certifications,

            "Resume Words": resume_words,

            "Resume Quality Score": resume_score

        }

        # ------------------------------------------------

        st.subheader("📋 Resume Summary")

        summary = analytics.summary(features)

        st.dataframe(
            summary,
            use_container_width=True,
            hide_index=True
        )

        # ------------------------------------------------

        st.subheader("🛠 Skill Distribution")

        skill_df = analytics.skill_distribution(
            matched,
            missing
        )

        st.dataframe(
            skill_df,
            use_container_width=True,
            hide_index=True
        )

        # ------------------------------------------------

        pie = analytics.pie_chart(
            matched,
            missing
        )

        st.plotly_chart(
            pie,
            use_container_width=True,
            key="analytics_pie"
        )

        # ------------------------------------------------

        bar = analytics.bar_chart(
            matched,
            missing
        )

        st.plotly_chart(
            bar,
            use_container_width=True,
            key="analytics_bar"
        )

        st.divider()

        # =====================================================
        # Analytics Metrics
        # =====================================================

        st.subheader("📊 Analytics Metrics")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Experience Level",
            analytics.experience_level(experience)
        )

        c2.metric(
            "Resume Strength",
            analytics.resume_strength(resume_score)
        )

        c3.metric(
            "Matched Skills",
            len(matched)
        )

        st.divider()

        # =====================================================
        # Dashboard Metrics
        # =====================================================

        metrics = analytics.dashboard_metrics(

            ats=resume_score,

            similarity=85,

            quality=resume_score

        )

        st.subheader("📈 Dashboard Metrics")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Overall Score",
            metrics["Overall Score"]
        )

        col2.metric(
            "Grade",
            metrics["Grade"]
        )

        col3.metric(
            "Recommendation",
            metrics["Recommendation"]
        )

        st.divider()

        st.json(metrics)