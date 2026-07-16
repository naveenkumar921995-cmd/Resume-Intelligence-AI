"""
=========================================================
NEXUS AI
Resume Analytics Dashboard
Author : Naveen Kumar
Version : 9.0
=========================================================
"""

import streamlit as st
import pandas as pd

from core.analytics import ResumeAnalytics


def analytics_page():

    st.title("📈 Resume Analytics Dashboard")

    st.markdown(
        "Analyze resume quality, experience level, skill distribution, and key metrics."
    )

    analytics = ResumeAnalytics()

    st.divider()

    # -----------------------------------------------------
    # Candidate Details
    # -----------------------------------------------------

    st.subheader("Candidate Information")

    col1, col2 = st.columns(2)

    with col1:

        experience = st.slider(
            "Years of Experience",
            0,
            20,
            3
        )

        projects = st.number_input(
            "Projects",
            0,
            50,
            5
        )

        certifications = st.number_input(
            "Certifications",
            0,
            20,
            2
        )

    with col2:

        resume_words = st.number_input(
            "Resume Word Count",
            100,
            5000,
            600
        )

        resume_score = st.slider(
            "Resume Quality Score",
            0,
            100,
            80
        )

    st.divider()

    # -----------------------------------------------------
    # Skills
    # -----------------------------------------------------

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
            "Docker"

        ],

        default=[

            "Python",
            "SQL",
            "Machine Learning"

        ]

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
            "Azure"

        ],

        default=[

            "AWS",
            "Docker"

        ]

    )

    st.divider()

    # -----------------------------------------------------
    # Generate Analytics
    # -----------------------------------------------------

    if st.button("Generate Analytics"):

        features = {

            "Experience": experience,

            "Projects": projects,

            "Certifications": certifications,

            "Resume Words": resume_words,

            "Resume Quality Score": resume_score

        }

        summary = analytics.summary(features)

        st.subheader("Resume Summary")

        st.dataframe(

            summary,

            use_container_width=True,

            hide_index=True

        )

        st.subheader("Skill Distribution")

        skill_df = analytics.skill_distribution(

            matched,

            missing

        )

        st.dataframe(

            skill_df,

            use_container_width=True,

            hide_index=True

        )

        fig = analytics.pie_chart(
        matched,
        missing
        )

        st.plotly_chart(
        fig,
        use_container_width=True
        )
        bar = analytics.bar_chart(
        matched,
        missing
        )

        st.plotly_chart(
        fig,
        use_container_width=True
        )
        bar = analytics.bar_chart(
        matched,
        missing
        )

        st.plotly_chart(
        bar,
        use_container_width=True
        )

        st.pyplot(fig)

        st.subheader("Analytics")

        c1, c2, c3 = st.columns(3)

        c1.metric(

            "Experience Level",

            analytics.experience_level(

                experience

            )

        )

        c2.metric(

            "Resume Strength",

            analytics.resume_strength(

                resume_score

            )

        )

        c3.metric(

            "Matched Skills",

            len(matched)

        )

        metrics = analytics.dashboard_metrics(

            ats=resume_score,

            similarity=85,

            quality=resume_score

        )

        st.divider()

        st.subheader("Dashboard Metrics")

        st.json(metrics)