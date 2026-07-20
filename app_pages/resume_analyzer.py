"""
=========================================================
NEXUS AI
Enterprise Resume Analyzer
Version : 10.0 Enterprise
Author : Naveen Kumar
=========================================================
"""

import streamlit as st

from config import SUPPORTED_FILES
from core.resume_parser import ResumeParser



def resume_analyzer_page():

    st.title("📄 Enterprise Resume Analyzer")

    st.markdown(
        "Upload your resume and receive a complete AI-powered ATS analysis."
    )

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF / DOCX)",
        type=SUPPORTED_FILES,
        key="resume_upload"
    )

    if uploaded_file is None:
        st.info("Upload a resume to start analysis.")
        return

    parser = ResumeParser()

    with st.spinner("Analyzing Resume..."):
        result = parser.analyze(uploaded_file)

    st.success("Resume analyzed successfully.")

    # ===================================================
    # Candidate Header
    # ===================================================

    st.divider()

    col1, col2 = st.columns([3, 1])

    with col1:

        st.subheader(result["name"])

        st.write("📧", result["email"])
        st.write("📱", result["phone"])

    with col2:

        score = result["resume_score"]

        if score >= 90:
            grade = "A+"
            color = "🟢"

        elif score >= 80:
            grade = "A"

            color = "🟢"

        elif score >= 70:
            grade = "B+"

            color = "🟡"

        elif score >= 60:
            grade = "B"

            color = "🟠"

        else:

            grade = "C"

            color = "🔴"

        st.metric(
            "ATS Score",
            f"{score}%"
        )

        st.metric(
            "Grade",
            f"{color} {grade}"
        )

    st.divider()

    # ===================================================
    # Resume Statistics
    # ===================================================

    st.subheader("📊 Resume Statistics")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Words", result["word_count"])

    c2.metric("Characters", result["character_count"])

    c3.metric("Lines", result["line_count"])

    c4.metric(
        "Reading Time",
        f'{result["reading_time"]} min'
    )

    st.divider()

    # ===================================================
    # Skills
    # ===================================================

    st.subheader("🛠 Skills Detected")

    skills = result["skills"]

    if skills:

        cols = st.columns(4)

        for i, skill in enumerate(skills):

            cols[i % 4].success(skill)

    else:

        st.warning("No skills detected.")

    st.divider()

    # ===================================================
    # Links
    # ===================================================

    st.subheader("🌐 Professional Profiles")

    st.write("LinkedIn :", result["linkedin"] or "-")

    st.write("GitHub :", result["github"] or "-")

    if result["portfolio"]:

        st.write("Portfolio")

        for site in result["portfolio"]:

            st.write("•", site)

    st.divider()

    # ===================================================
    # ATS Feedback
    # ===================================================

    st.subheader("🤖 AI ATS Review")

    if score >= 90:

        st.success(
            """
Excellent ATS optimized resume.

Strong keyword coverage.

Well formatted for recruiters.
"""
        )

    elif score >= 75:

        st.info(
            """
Good resume.

Add more measurable achievements.

Improve technical keywords.
"""
        )

    else:

        st.error(
            """
Resume requires improvement.

• Add projects

• Add certifications

• Improve formatting

• Improve ATS keywords

• Add measurable achievements
"""
        )

    st.divider()

    # ===================================================
    # Resume Preview
    # ===================================================

    st.subheader("📄 Resume Preview")

    st.text_area(

        "",

        result["raw_text"],

        height=350

    )

    st.divider()

    # ===================================================
    # Final Recommendation
    # ===================================================

    st.subheader("🎯 Recruiter Recommendation")

    if score >= 90:

        st.success("Highly Recommended")

    elif score >= 75:

        st.info("Recommended")

    elif score >= 60:

        st.warning("Needs Improvement")

    else:

        st.error("Not Recommended")

    st.divider()

    # ===================================================
    # Version Footer
    # ===================================================

    st.caption(
        "NEXUS AI Resume Intelligence Platform • Version 10 Enterprise"
    )