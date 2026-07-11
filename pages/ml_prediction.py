import streamlit as st
from core.ml_prediction import MLPredictor


def ml_prediction_page():
    """
    Machine Learning Prediction Page
    """

    st.header("🤖 Machine Learning Prediction")

    ml = MLPredictor()

    comparison = ml.train_models()

    st.subheader("📊 Model Comparison")

    st.dataframe(
        comparison,
        use_container_width=True
    )

    st.divider()

    st.subheader("🎯 Predict Hiring Score")

    experience = st.slider(
        "Experience (Years)",
        0,
        20,
        3
    )

    skills = st.slider(
        "Number of Skills",
        0,
        40,
        15
    )

    education = st.slider(
        "Education Level",
        1,
        5,
        3
    )

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
        "Select Model",
        comparison["Model"]
    )

    if st.button("🚀 Predict Hiring Score"):

        score = ml.predict(
            experience,
            skills,
            education,
            projects,
            certifications,
            model
        )

        st.success("Prediction Completed Successfully!")

        st.metric(
            "Predicted Hiring Score",
            f"{score:.2f}%"
        )