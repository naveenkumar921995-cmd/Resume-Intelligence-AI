"""
=========================================================
NEXUS AI
ATS Analysis
Author : Naveen Kumar
=========================================================
"""

import streamlit as st

from config import SUPPORTED_FILES
from core.resume_parser import ResumeParser
from core.keyword_engine import KeywordEngine


def ats_analysis_page():

    st.header("📊 ATS Resume Analysis")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=SUPPORTED_FILES,
        key="ats_upload"
    )

    if uploaded_file is None:
        st.info("Please upload a resume.")
        return

    # Parse Resume
    parser = ResumeParser()
    result = parser.analyze(uploaded_file)

    resume_text = result["raw_text"]

    # ATS Engine
    engine = KeywordEngine()

    required_skills = engine.skills["Skill"].tolist()

    report = engine.analyze(
        resume_text,
        required_skills
    )

    st.success("ATS Analysis Completed Successfully")

    st.metric(
        "ATS Score",
        f"{report['ATS Score']}%"
    )

    st.progress(report["ATS Score"] / 100)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Matched Skills")
        st.write(report["Matched Skills"])

    with col2:
        st.subheader("❌ Missing Skills")
        st.write(report["Missing Skills"])

    st.divider()

    st.subheader("Technical Skills")
    st.write(report["Technical Skills"])

    st.subheader("Soft Skills")
    st.write(report["Soft Skills"])

    st.divider()

    st.subheader("Skill Gap")

    st.json(report["Skill Gap"])

    st.subheader("Priority Skills")

    st.dataframe(
        report["Priority"],
        use_container_width=True
    )