import streamlit as st
import pandas as pd

from core.resume_parser import parse_resume
from core.keyword_engine import KeywordEngine


def ats_analysis_page():

    st.header("📊 ATS Resume Analysis")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"],
        key="ats"
    )

    if uploaded_file is None:
        return

    resume_text = parse_resume(uploaded_file)

    engine = KeywordEngine()

    # All skills from skills_master.csv
    required_skills = engine.skills["Skill"].tolist()

    report = engine.analyze(
        resume_text,
        required_skills
    )

    st.success("Analysis Completed Successfully!")

    st.metric(
        "ATS Score",
        f"{report['ATS Score']}%"
    )

    st.progress(report["ATS Score"] / 100)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Matched Skills")

        st.write(report["Matched Skills"])

    with col2:

        st.subheader("Missing Skills")

        st.write(report["Missing Skills"])

    st.subheader("Technical Skills")

    st.write(report["Technical Skills"])

    st.subheader("Soft Skills")

    st.write(report["Soft Skills"])

    st.subheader("Skill Gap")

    st.json(report["Skill Gap"])

    st.subheader("Priority Skills")

    st.dataframe(
        report["Priority"],
        use_container_width=True
    )