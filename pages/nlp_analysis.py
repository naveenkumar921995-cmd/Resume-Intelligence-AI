"""
=========================================================
NEXUS AI
NLP Resume Similarity Analysis
Author : Naveen Kumar
Version : 9.0
=========================================================
"""

import streamlit as st

from core.similarity_engine import SimilarityEngine


def nlp_analysis_page():

    st.title("🧠 NLP Resume Similarity Analysis")

    st.markdown(
        """
Compare a resume against a Job Description using
TF-IDF Vectorization and Cosine Similarity.
"""
    )

    st.divider()

    resume = st.text_area(
        "📄 Resume Text",
        height=250,
        placeholder="Paste Resume Text Here..."
    )

    job = st.text_area(
        "💼 Job Description",
        height=250,
        placeholder="Paste Job Description Here..."
    )

    st.divider()

    if st.button(
        "🚀 Analyze Similarity",
        use_container_width=True
    ):

        if resume.strip() == "" or job.strip() == "":

            st.warning(
                "Please provide both Resume and Job Description."
            )

            return

        engine = SimilarityEngine()

        report = engine.analyze(
            resume,
            job
        )

        score = report["Similarity Score"]

        st.success("Analysis Completed Successfully")

        st.metric(
            "Similarity Score",
            f"{score}%"
        )

        st.progress(score / 100)

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Grade")

            st.success(
                report["Grade"]
            )

        with col2:

            st.subheader("Recommendation")

            st.info(
                report["Recommendation"]
            )

        st.divider()

        st.subheader("Analysis Report")

        st.json(report)

        st.divider()

        st.subheader("Interpretation")

        if score >= 90:

            st.success(
                "Excellent match. Resume is highly aligned with the Job Description."
            )

        elif score >= 75:

            st.success(
                "Strong match. Only minor improvements are recommended."
            )

        elif score >= 60:

            st.warning(
                "Moderate match. Improve missing keywords and technical skills."
            )

        elif score >= 40:

            st.warning(
                "Low match. Resume requires significant optimization."
            )

        else:

            st.error(
                "Very poor match. Rewrite the resume according to the Job Description."
            )

        st.divider()

        st.subheader("Technology Used")

        st.dataframe(

            {
                "Component": [
                    "Vectorization",
                    "Similarity Metric",
                    "NLP Library",
                    "Language Processing"
                ],
                "Technology": [
                    "TF-IDF",
                    "Cosine Similarity",
                    "Scikit-Learn",
                    "Natural Language Processing"
                ]
            },

            hide_index=True,
            use_container_width=True

        )