"""
=========================================================
NEXUS AI
AI Career Coach
Author : Naveen Kumar
Version : 9.1 Enterprise
=========================================================
"""

import streamlit as st
from core.ai_engine import AIEngine


def ai_career_coach_page():

    st.title("💬 AI Career Coach")

    st.markdown(
        "Get AI-powered resume feedback, recruiter insights, and a personalized learning roadmap."
    )

    engine = AIEngine()

    st.divider()

    # =====================================================
    # Resume Metrics
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        ats = st.slider(
            "ATS Score",
            0,
            100,
            75,
            key="coach_ats"
        )

        similarity = st.slider(
            "Job Similarity",
            0,
            100,
            70,
            key="coach_similarity"
        )

    with col2:

        quality = st.slider(
            "Resume Quality",
            0,
            100,
            80,
            key="coach_quality"
        )

        experience = st.slider(
            "Experience (Years)",
            0,
            20,
            3,
            key="coach_experience"
        )

    st.divider()

    # =====================================================
    # Skills
    # =====================================================

    matched = st.text_input(

        "Matched Skills",

        "Python, SQL, Machine Learning",

        key="coach_matched"

    )

    missing = st.text_input(

        "Missing Skills",

        "AWS, Docker",

        key="coach_missing"

    )

    st.divider()

    # =====================================================
    # Generate Review
    # =====================================================

    if st.button(
        "🚀 Generate AI Review",
        use_container_width=True
    ):

        coach = engine.llm

        with st.spinner("Generating AI Career Report..."):

            report = coach.generate_report(

                ats=ats,

                similarity=similarity,

                quality=quality,

                experience=experience,

                matched=[
                    x.strip()
                    for x in matched.split(",")
                    if x.strip()
                ],

                missing=[
                    x.strip()
                    for x in missing.split(",")
                    if x.strip()
                ],

            )

        st.success("AI Review Generated Successfully!")

        st.divider()

        st.subheader("📋 AI Review")

        for item in report["AI Review"]:

            st.success(item)

        st.divider()

        st.subheader("🎯 Recruiter Decision")

        st.info(
            report["Recruiter Decision"]
        )

        st.divider()

        st.subheader("📚 Personalized Learning Plan")

        for skill in report["Learning Plan"]:

            st.write(f"• {skill}")

        st.divider()

        st.subheader("📄 Complete AI Report")

        st.json(report)