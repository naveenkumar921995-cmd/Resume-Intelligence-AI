"""
=========================================================
NEXUS AI
Resume Analytics Dashboard
Author : Naveen Kumar
Version : 9.0
=========================================================
"""

import streamlit as st
from core.analytics import ResumeAnalytics


def analytics_page():

    st.title("📈 Resume Analytics Dashboard")

    st.markdown(
        "Analyze resume quality, experience level, skill distribution, and key metrics."
    )

    analytics = ResumeAnalytics()

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
            key="experience_slider"
        )

        projects = st.number_input(
            "Projects",
            0,
            50,
            5,
            key="projects_input"
        )

        certifications = st.number_input(
            "Certifications",
            0,
            20,
            2,
            key="certifications_input"
        )

    with col2:

        resume_words = st.number_input(
            "Resume Word Count",
            100,
            5000,
            600,
            key="resume_words_input"
        )

        resume_score = st.slider(
            "Resume Quality Score",
            0,
            100,
            80,
            key="resume_score_slider"
        )

    st.divider()

    # =====================================================
    # Skills
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
        key="matched_skills"
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
        key="missing_skills"
    )

    st.divider()

    # =====================================================
    # Generate Analytics
    # =====================================================

    if st.button("🚀 Generate Analytics", key="generate_analytics"):

        features = {
            "Experience": experience,
            "Projects": projects,
            "Certifications": certifications,
            "Resume Words": resume_words,
            "Resume Quality Score": resume_score,
        }

        # -------------------------------------------------

        st.subheader("📋 Resume Summary")

        summary = analytics.summary(features)

        st.dataframe(
            summary,
            use_container_width=True,
            hide_index=True,
        )

        # -------------------------------------------------

        st.subheader("🛠 Skill Distribution")

        skill_df = analytics.skill_distribution(
            matched,
            missing,
        )

        st.dataframe(
            skill_df,
            use_container_width=True,
            hide_index=True,
        )

        # -------------------------------------------------
        # Pie Chart
        # -------------------------------------------------

        pie_fig = analytics.pie_chart(
            matched,
            missing,
        )

        st.plotly_chart(
            pie_fig,
            use_container_width=True,
            key="pie_chart"
        )

        # -------------------------------------------------
        # Bar Chart
        # -------------------------------------------------

        bar_fig = analytics.bar_chart(
            matched,
            missing,
        )

        st.plotly_chart(
            bar_fig,
            use_container_width=True,
            key="bar_chart"
        )

        st.divider()

        # =====================================================
        # Analytics Metrics
        # =====================================================

        st.subheader("📊 Analytics")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Experience Level",
                analytics.experience_level(experience),
            )

        with col2:
            st.metric(
                "Resume Strength",
                analytics.resume_strength(resume_score),
            )

        with col3:
            st.metric(
                "Matched Skills",
                len(matched),
            )

        st.divider()

        # =====================================================
        # Dashboard Metrics
        # =====================================================

        metrics = analytics.dashboard_metrics(
            ats=resume_score,
            similarity=85,
            quality=resume_score,
        )

        st.subheader("📈 Dashboard Metrics")

        st.json(metrics)