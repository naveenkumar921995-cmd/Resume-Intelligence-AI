import streamlit as st
from core.llm_engine import AIResumeCoach


def ai_career_coach_page():
    """
    AI Career Coach Page
    """

    st.header("💬 AI Career Coach")

    resume = st.text_area(
        "Paste Your Resume",
        height=250,
        placeholder="Paste your resume text here..."
    )

    if st.button("🚀 Review Resume"):

        if not resume.strip():
            st.warning("Please paste your resume first.")
            return

        coach = AIResumeCoach()

        with st.spinner("Analyzing Resume..."):
            review = coach.review(resume)

        st.success("Analysis Completed!")

        st.write(review)