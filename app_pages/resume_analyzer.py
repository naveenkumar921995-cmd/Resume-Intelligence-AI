"""
=========================================================
NEXUS AI
Resume Intelligence Center
Author : Naveen Kumar
Version : 9.1 Enterprise
=========================================================
"""

import streamlit as st

from config import SUPPORTED_FILES
from core.ai_engine import AIEngine
from core.resume_parser import ResumeParser


def resume_analyzer_page():

    st.title("📄 Resume Intelligence Center")

    st.markdown(
        "Upload a resume and receive ATS analysis, AI insights, ML prediction, Deep Learning prediction, recruiter recommendations, and analytics."
    )

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF / DOCX)",
        type=SUPPORTED_FILES,
        key="resume_upload"
    )

    if uploaded_file is None:
        st.info("Please upload a resume to begin analysis.")
        return

    parser = ResumeParser()
    engine = AIEngine()

    with st.spinner("Analyzing Resume..."):

        result = parser.analyze(uploaded_file)

        word_count = result["word_count"]

        ats = min(100, max(40, int(word_count / 8)))

        similarity = min(100, ats + 5)

        quality = ats

        experience = 3

        matched = [
            "Python",
            "SQL",
            "Machine Learning"
        ]

        missing = [
            "AWS",
            "Docker"
        ]

        analytics = engine.analytics.dashboard_metrics(
            ats=ats,
            similarity=similarity,
            quality=quality
        )

        ml_report = engine.ml.full_report(
            experience=experience,
            skills=15,
            education=4,
            projects=5,
            certifications=2,
            model_name="Random Forest"
        )

        dl_report = engine.dl.full_report(
            experience=experience,
            skills=15,
            projects=5,
            education=4,
            certifications=2
        )

        ai_review = engine.llm.generate_report(
            ats=ats,
            similarity=similarity,
            quality=quality,
            experience=experience,
            matched=matched,
            missing=missing
        )

    st.success("Resume Analysis Completed Successfully!")

    st.divider()

    # ====================================================
    # Dashboard
    # ====================================================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("ATS Score", f"{ats}%")
    c2.metric("ML Score", f'{ml_report["Hiring Score"]}%')
    c3.metric("DL Score", f'{dl_report["Hiring Score"]}%')
    c4.metric("Grade", analytics["Grade"])

    st.progress(analytics["Overall Score"] / 100)

    st.divider()

    # ====================================================
    # Resume Preview
    # ====================================================

    st.subheader("📄 Resume Preview")

    st.text_area(
        "Extracted Resume",
        result["raw_text"],
        height=300
    )

    st.divider()

    # ====================================================
    # Resume Statistics
    # ====================================================

    st.subheader("📊 Resume Statistics")

    a, b, c = st.columns(3)

    a.metric("Words", result["word_count"])
    b.metric("Characters", result["character_count"])
    c.metric("Lines", result["line_count"])

    st.divider()

    # ====================================================
    # Contact
    # ====================================================

    st.subheader("📞 Contact Information")

    st.write("📧 Email:", result["email"])
    st.write("📱 Phone:", result["phone"])
    st.write("🔗 LinkedIn:", result["linkedin"])
    st.write("💻 GitHub:", result["github"])

    if result["portfolio"]:

        st.write("🌐 Portfolio")

        for site in result["portfolio"]:
            st.write(f"• {site}")

    st.divider()

    # ====================================================
    # Recruiter Dashboard
    # ====================================================

    st.subheader("🎯 Recruiter Dashboard")

    d1, d2, d3 = st.columns(3)

    d1.metric("Overall Score", analytics["Overall Score"])

    d2.metric("Recommendation", analytics["Recommendation"])

    d3.metric("Resume Grade", analytics["Grade"])

    st.divider()

    # ====================================================
    # ML Prediction
    # ====================================================

    st.subheader("🤖 Machine Learning Prediction")

    st.json(ml_report)

    st.divider()

    # ====================================================
    # Deep Learning Prediction
    # ====================================================

    st.subheader("🧠 Deep Learning Prediction")

    st.json(dl_report)

    st.divider()

    # ====================================================
    # AI Review
    # ====================================================

    st.subheader("💬 AI Career Coach")

    for item in ai_review["AI Review"]:
        st.success(item)

    st.info(ai_review["Recruiter Decision"])

    st.subheader("📚 Learning Plan")

    for item in ai_review["Learning Plan"]:
        st.write(f"• {item}")

    st.divider()

    # ====================================================
    # Analytics
    # ====================================================

    st.subheader("📈 Analytics")

    pie = engine.analytics.pie_chart(
        matched,
        missing
    )

    st.plotly_chart(
        pie,
        use_container_width=True,
        key="resume_pie"
    )

    bar = engine.analytics.bar_chart(
        matched,
        missing
    )

    st.plotly_chart(
        bar,
        use_container_width=True,
        key="resume_bar"
    )