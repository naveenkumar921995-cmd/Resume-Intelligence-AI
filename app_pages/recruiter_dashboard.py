"""
=========================================================
NEXUS AI
Recruiter Dashboard
Author : Naveen Kumar
Version : 9.1 Enterprise
=========================================================
"""

import streamlit as st
from core.ai_engine import AIEngine


def recruiter_dashboard_page():

    st.title("🎯 Recruiter Dashboard")

    st.markdown(
        "Enterprise dashboard for recruiters to evaluate candidates using AI."
    )

    engine = AIEngine()

    st.divider()

    # =====================================================
    # Candidate Inputs
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        ats = st.slider(
            "ATS Score",
            0,
            100,
            82,
            key="recruiter_ats"
        )

        similarity = st.slider(
            "Job Similarity",
            0,
            100,
            86,
            key="recruiter_similarity"
        )

    with col2:

        quality = st.slider(
            "Resume Quality",
            0,
            100,
            84,
            key="recruiter_quality"
        )

        experience = st.slider(
            "Experience",
            0,
            20,
            4,
            key="recruiter_experience"
        )

    matched = st.multiselect(

        "Matched Skills",

        [
            "Python",
            "SQL",
            "Machine Learning",
            "Deep Learning",
            "Power BI",
            "AWS",
            "Docker",
            "Excel",
        ],

        default=[
            "Python",
            "SQL",
            "Machine Learning",
        ],

        key="recruiter_matched"

    )

    missing = st.multiselect(

        "Missing Skills",

        [
            "AWS",
            "Docker",
            "Kubernetes",
            "Azure",
            "TensorFlow",
            "CI/CD",
        ],

        default=[
            "AWS",
            "Docker",
        ],

        key="recruiter_missing"

    )

    st.divider()

    # =====================================================
    # AI Evaluation
    # =====================================================

    if st.button(
        "🚀 Evaluate Candidate",
        use_container_width=True
    ):

        analytics = engine.analytics
        coach = engine.llm

        metrics = analytics.dashboard_metrics(

            ats=ats,

            similarity=similarity,

            quality=quality

        )

        report = coach.generate_report(

            ats=ats,

            similarity=similarity,

            quality=quality,

            experience=experience,

            matched=matched,

            missing=missing

        )

        # =============================================

        st.subheader("📊 Candidate Score")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "ATS",
            metrics["ATS Score"]
        )

        c2.metric(
            "Similarity",
            metrics["Similarity"]
        )

        c3.metric(
            "Overall",
            metrics["Overall Score"]
        )

        c4.metric(
            "Grade",
            metrics["Grade"]
        )

        st.progress(
            metrics["Overall Score"] / 100
        )

        st.divider()

        # =============================================

        st.subheader("🎯 Recruiter Decision")

        st.success(
            metrics["Recommendation"]
        )

        st.info(
            report["Recruiter Decision"]
        )

        st.divider()

        # =============================================

        st.subheader("📋 AI Review")

        for item in report["AI Review"]:

            st.write(f"✅ {item}")

        st.divider()

        # =============================================

        st.subheader("📚 Recommended Learning")

        for skill in report["Learning Plan"]:

            st.write(f"• {skill}")

        st.divider()

        st.subheader("📄 Complete Report")

        st.json({

            "Analytics": metrics,

            "AI Review": report

        })