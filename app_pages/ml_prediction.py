"""
=========================================================
NEXUS AI
Machine Learning Prediction Page
Author : Naveen Kumar
Version : 9.1 Enterprise
=========================================================
"""

import streamlit as st
from core.ai_engine import AIEngine


def ml_prediction_page():

    st.title("🤖 Machine Learning Hiring Prediction")

    st.markdown(
        "Predict candidate hiring score using the Enterprise AI Engine."
    )

    engine = AIEngine()

    # -------------------------------------------------
    # Train Models
    # -------------------------------------------------

    with st.spinner("Training Machine Learning Models..."):

        comparison = engine.ml.train_models()

    st.subheader("📊 Model Performance Comparison")

    st.dataframe(
        comparison,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # -------------------------------------------------
    # Candidate Profile
    # -------------------------------------------------

    st.subheader("Candidate Profile")

    col1, col2 = st.columns(2)

    with col1:

        experience = st.slider(
            "Experience (Years)",
            0,
            20,
            3
        )

        skills = st.slider(
            "Technical Skills",
            1,
            40,
            15
        )

        education = st.selectbox(
            "Education Level",
            [1, 2, 3, 4, 5]
        )

    with col2:

        projects = st.slider(
            "Projects",
            0,
            20,
            5
        )

        certifications = st.slider(
            "Certifications",
            0,
            15,
            2
        )

        model = st.selectbox(
            "Prediction Model",
            comparison["Model"].tolist()
        )

    st.divider()

    # -------------------------------------------------
    # Prediction
    # -------------------------------------------------

    if st.button(
        "🚀 Predict Hiring Score",
        use_container_width=True
    ):

        report = engine.ml.full_report(

            experience=experience,

            skills=skills,

            education=education,

            projects=projects,

            certifications=certifications,

            model_name=model

        )

        score = report["Hiring Score"]

        st.success("Prediction Completed Successfully!")

        st.metric(
            "Hiring Score",
            f"{score}%"
        )

        st.progress(score / 100)

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Candidate Grade")
            st.success(report["Grade"])

        with col2:

            st.subheader("Recommendation")
            st.info(report["Recommendation"])

        st.divider()

        st.subheader("Prediction Summary")

        st.json(report)