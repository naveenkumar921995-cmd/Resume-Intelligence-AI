import streamlit as st
from core.deep_learning import DeepLearningModel


def deep_learning_page():
    """
    Deep Learning Hiring Prediction Page
    """

    st.header("🧬 Deep Learning Hiring Prediction")

    dl = DeepLearningModel()

    experience = st.slider(
        "Experience (Years)",
        0,
        20,
        4
    )

    skills = st.slider(
        "Number of Skills",
        0,
        40,
        15
    )

    projects = st.slider(
        "Projects",
        0,
        20,
        5
    )

    education = st.slider(
        "Education Level",
        1,
        5,
        3
    )

    certifications = st.slider(
        "Certifications",
        0,
        15,
        2
    )

    if st.button("🧠 Predict using Neural Network"):

        report = dl.full_report(
            experience,
            skills,
            projects,
            education,
            certifications
        )

        st.success("Prediction Completed Successfully!")

        st.metric(
            "Hiring Score",
            f"{report['Hiring Score']}%"
        )

        st.info(
            f"Confidence: {report['Confidence']}"
        )

        st.success(
            report["Recommendation"]
        )