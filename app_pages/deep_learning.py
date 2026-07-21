"""
=========================================================
NEXUS AI
Enterprise Deep Learning Prediction
Version : 11.0 Enterprise
Author : Naveen Kumar
=========================================================
"""

import streamlit as st

from core.ai_engine import AIEngine
from core.hiring_score import HiringScoreEngine


def deep_learning_page():

    st.title("🧠 Enterprise Deep Learning Prediction")

    st.markdown(
        """
Predict candidate hiring potential using
Neural Networks + Enterprise Hiring Intelligence.
        """
    )

    engine = AIEngine()

    hiring = HiringScoreEngine()

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

    # =====================================================
    # Prediction
    # =====================================================

    if st.button(

        "🚀 Predict Using Deep Learning",

        use_container_width=True

    ):

        with st.spinner(

            "Running Enterprise Neural Network..."

        ):

            report = engine.dl.full_report(

                experience=experience,

                skills=skills,

                projects=projects,

                education=education,

                certifications=certifications

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

            "Enterprise Deep Learning Prediction Completed Successfully."

        )

        st.divider()
        # =====================================================
        # Enterprise Dashboard
        # =====================================================

        st.subheader("📊 Enterprise Deep Learning Dashboard")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(

            "DL Score",

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
        # Prediction Summary
        # =====================================================

        st.subheader("📈 Prediction Summary")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(

                "Confidence",

                report["Confidence"]

            )

            st.success(

                report["Grade"]

            )

        with col2:

            st.metric(

                "Hiring Status",

                report["Hiring Status"]

            )

            st.info(

                report["Recommendation"]

            )

        st.divider()

        # =====================================================
        # Recruiter Recommendation
        # =====================================================

        st.subheader("🎯 Recruiter Recommendation")

        st.success(

            hiring_report["Recommendation"]

        )

        st.warning(

            f'Risk Level : {hiring_report["Risk"]}'

        )

        st.info(

            f'Hiring Probability : {hiring_report["Hiring Probability"]}%'

        )

        st.divider()

        # =====================================================
        # Candidate Inputs
        # =====================================================

        st.subheader("👤 Candidate Profile Summary")

        st.dataframe(

            {

                "Feature": [

                    "Experience",

                    "Technical Skills",

                    "Education",

                    "Projects",

                    "Certifications"

                ],

                "Value": [

                    experience,

                    skills,

                    education,

                    projects,

                    certifications

                ]

            },

            hide_index=True,

            use_container_width=True

        )

        st.divider()

        # =====================================================
        # Model Evaluation
        # =====================================================

        st.subheader("🧠 Deep Learning Model Evaluation")

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

        # =====================================================
        # Enterprise Report
        # =====================================================

        st.subheader("📄 Enterprise Prediction Report")

        st.json({

            "Deep Learning": report,

            "Hiring Report": hiring_report,

            "Model Metrics": metrics

        })

        st.divider()

        st.caption(

            "NEXUS AI Enterprise Resume Intelligence Platform • Version 11.0"

        )