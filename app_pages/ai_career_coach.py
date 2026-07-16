import streamlit as st
from core.llm_engine import LLMEngine


def ai_career_coach_page():
    """
    AI Career Coach Page
    """

    st.header("💬 AI Career Coach")

    ats = st.slider("ATS Score", 0, 100, 75)
    similarity = st.slider("Job Similarity", 0, 100, 70)
    quality = st.slider("Resume Quality", 0, 100, 80)
    experience = st.slider("Experience (Years)", 0, 20, 3)

    matched = st.text_input(
        "Matched Skills",
        "Python, SQL, Machine Learning"
    )

    missing = st.text_input(
        "Missing Skills",
        "AWS, Docker"
    )

    if st.button("🚀 Generate AI Review"):

        coach = LLMEngine()

        report = coach.generate_report(
            ats=ats,
            similarity=similarity,
            quality=quality,
            experience=experience,
            matched=[x.strip() for x in matched.split(",") if x.strip()],
            missing=[x.strip() for x in missing.split(",") if x.strip()],
        )

        st.success("AI Review Generated")

        st.subheader("📋 AI Review")

        for item in report["AI Review"]:
            st.write("✅", item)

        st.subheader("🎯 Recruiter Decision")

        st.info(report["Recruiter Decision"])

        st.subheader("📚 Learning Plan")

        for skill in report["Learning Plan"]:
            st.write("•", skill)