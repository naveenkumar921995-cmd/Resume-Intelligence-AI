"""
=========================================================
NEXUS AI
Resume Analyzer
Author : Naveen Kumar
=========================================================
"""

import streamlit as st

from config import SUPPORTED_FILES
from core.resume_parser import ResumeParser


def resume_analyzer_page():

    st.header("📄 Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF / DOCX)",
        type=SUPPORTED_FILES,
        key="resume_upload"
    )

    if uploaded_file is None:
        st.info("Please upload a resume to begin analysis.")
        return

    parser = ResumeParser()

    result = parser.analyze(uploaded_file)

    st.success("Resume parsed successfully.")

    st.subheader("Resume Preview")

    st.text_area(
        "Extracted Resume Text",
        result["raw_text"],
        height=300
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    col1.metric("Words", result["word_count"])
    col2.metric("Characters", result["character_count"])
    col3.metric("Lines", result["line_count"])

    st.divider()

    st.subheader("Contact Information")

    st.write("📧 Email :", result["email"])
    st.write("📱 Phone :", result["phone"])
    st.write("🔗 LinkedIn :", result["linkedin"])
    st.write("💻 GitHub :", result["github"])

    if result["portfolio"]:
        st.subheader("Portfolio / Websites")

        for website in result["portfolio"]:
            st.write("•", website)