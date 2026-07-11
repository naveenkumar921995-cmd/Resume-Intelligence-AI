import streamlit as st
from core.report_generator import ReportGenerator


def executive_report_page():
    """
    Executive AI Report Page
    """

    st.header("📑 Executive AI Report")

    if st.button("📄 Generate Sample Report"):

        generator = ReportGenerator()

        with st.spinner("Generating Report..."):

            pdf = generator.generate_report(
                candidate_name="Naveen Kumar",
                department="Data Science",
                job_role="Data Analyst",
                ats_score=88,
                matched_skills=["Python", "Pandas", "SQL"],
                missing_skills=["Power BI", "AWS"],
                ml_score=91,
                dl_score=93,
                recommendation="Excellent candidate with strong analytical skills.",
                statistics={
                    "Words": 620,
                    "Characters": 4200,
                    "Sentences": 41,
                    "Lines": 86
                }
            )

        st.success("Report Generated Successfully!")

        with open(pdf, "rb") as file:
            st.download_button(
                label="📥 Download Report",
                data=file,
                file_name="Resume_Report.pdf",
                mime="application/pdf"
            )