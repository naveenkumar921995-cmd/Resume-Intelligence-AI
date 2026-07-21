"""
=========================================================
NEXUS AI
Enterprise Machine Learning Prediction
Version : 11.0 Enterprise
Author : Naveen Kumar
=========================================================
"""

import streamlit as st

from core.ai_engine import AIEngine
from core.hiring_score import HiringScoreEngine


def ml_prediction_page():

    st.title("🤖 Enterprise Machine Learning Prediction")

    st.markdown(
        """
Predict candidate hiring potential using
Machine Learning + Enterprise Hiring Intelligence.
"""
    )

    engine = AIEngine()

    hiring = HiringScoreEngine()

    # =====================================================
    # Train ML Models
    # =====================================================

    with st.spinner("Training Enterprise ML Models..."):

        comparison = engine.ml.train_models()

    st.subheader("📊 Model Performance Comparison")

    st.dataframe(

        comparison,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # =====================================================
    # Candidate Profile
    # =====================================================

    st.subheader("👤 Candidate Profile")

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

            [

                1,

                2,

                3,

                4,

                5

            ]

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

    # =====================================================
    # Predict
    # =====================================================

    if st.button(

        "🚀 Predict Hiring Score",

        use_container_width=True

    ):

        with st.spinner(

            "Running Enterprise ML Prediction..."

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

        hiring_report = hiring.report(

            ats=score,

            similarity=score,

            ml=score,

            dl=score,

            technical=skills * 2.5,

            soft_skills=80,

            experience=min(

                experience * 10,

                100

            )

        )

        st.success(

            "Enterprise Prediction Completed Successfully."

        )

        st.divider()
        # =====================================================
        # Enterprise Dashboard
        # =====================================================

        st.subheader("📊 Enterprise Hiring Dashboard")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(

            "ML Score",

            f"{score}%"

        )

        c2.metric(

            "Hiring Score",

            f'{hiring_report["Hiring Score"]}%'

        )

        c3.metric(

            "Grade",

            hiring_report["Grade"]

        )

        c4.metric(

            "Hiring Probability",

            f'{hiring_report["Hiring Probability"]}%'

        )

        st.progress(

            hiring_report["Hiring Score"] / 100

        )

        st.divider()

        # =====================================================
        # Candidate Summary
        # =====================================================

        st.subheader("👤 Candidate Summary")

        s1, s2, s3 = st.columns(3)

        s1.metric(

            "Experience",

            f"{experience} Years"

        )

        s2.metric(

            "Technical Skills",

            skills

        )

        s3.metric(

            "Projects",

            projects

        )

        st.divider()

        # =====================================================
        # Recruiter Recommendation
        # =====================================================

        st.subheader("🎯 Recruiter Recommendation")

        st.success(

            hiring_report["Recommendation"]

        )

        st.info(

            report["Recommendation"]

        )

        st.warning(

            f'Risk Level : {hiring_report["Risk"]}'

        )

        st.divider()

        # =====================================================
        # Prediction Summary
        # =====================================================

        st.subheader("📈 Machine Learning Prediction Summary")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(

                "Predicted Hiring Score",

                f"{score}%"

            )

            st.success(

                report["Grade"]

            )

        with col2:

            st.metric(

                "Hiring Probability",

                f'{hiring_report["Hiring Probability"]}%'

            )

            st.info(

                hiring_report["Recommendation"]

            )

        st.divider()

        # =====================================================
        # Candidate Input Summary
        # =====================================================

        st.subheader("📋 Candidate Inputs")

        st.dataframe(

            {

                "Feature": [

                    "Experience",

                    "Technical Skills",

                    "Education",

                    "Projects",

                    "Certifications",

                    "Prediction Model"

                ],

                "Value": [

                    experience,

                    skills,

                    education,

                    projects,

                    certifications,

                    model

                ]

            },

            hide_index=True,

            use_container_width=True

        )

        st.divider()

        # =====================================================
        # Enterprise JSON Report
        # =====================================================

        st.subheader("📄 Enterprise Prediction Report")

        st.json({

            "Machine Learning": report,

            "Hiring Report": hiring_report

        })

        st.divider()

        st.caption(

            "NEXUS AI Enterprise Resume Intelligence Platform • Version 11.0"

        )