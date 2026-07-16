"""
=========================================================
NEXUS AI
Deep Learning Prediction Page
Author : Naveen Kumar
Version : 9.1 Enterprise
=========================================================
"""

import streamlit as st
from core.ai_engine import AIEngine


def deep_learning_page():

    st.title("🧠 Deep Learning Hiring Prediction")

    st.markdown(
        "Neural Network based hiring prediction using the Enterprise AI Engine."
    )

    engine = AIEngine()

    st.divider()

    st.subheader("Candidate Profile")

    col1, col2 = st.columns(2)

    with col1:

        experience = st.slider(
            "Experience (Years)",
            0,
            20,
            3,
            key="dl_experience"
        )

        skills = st.slider(
            "Technical Skills",
            1,
            40,
            15,
            key="dl_skills"
        )

        education = st.selectbox(
            "Education Level",
            [1, 2, 3, 4, 5],
            key="dl_education"
        )

    with col2:

        projects = st.slider(
            "Projects",
            0,
            20,
            5,
            key="dl_projects"
        )

        certifications = st.slider(
            "Certifications",
            0,
            15,
            2,
            key="dl_certifications"
        )

    st.divider()

    if st.button(
        "🚀 Predict Using Deep Learning",
        use_container_width=True
    ):

        with st.spinner("Running Neural Network..."):

            report = engine.dl.full_report(

                experience=experience,

                skills=skills,

                projects=projects,

                education=education,

                certifications=certifications

            )

        score = report["Hiring Score"]

        st.success("Prediction Completed Successfully!")

        st.metric(
            "Hiring Score",
            f"{score}%"
        )

        st.progress(score / 100)

        st.divider()

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Confidence",
            report["Confidence"]
        )

        c2.metric(
            "Grade",
            report["Grade"]
        )

        c3.metric(
            "Hiring Status",
            report["Hiring Status"]
        )

        st.divider()

        st.subheader("Recommendation")

        st.info(report["Recommendation"])

        st.divider()

        st.subheader("Model Evaluation")

        metrics = engine.dl.evaluate()

        m1, m2 = st.columns(2)

        m1.metric(
            "Loss",
            metrics["Loss"]
        )

        m2.metric(
            "MAE",
            metrics["MAE"]
        )

        st.divider()

        st.subheader("Complete Prediction Report")

        st.json(report)