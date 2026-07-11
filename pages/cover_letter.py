import streamlit as st
from core.cover_letter import CoverLetterGenerator


def cover_letter_page():
    """
    AI Cover Letter Generator
    """

    st.header("📜 AI Cover Letter Generator")

    name = st.text_input("Candidate Name")

    company = st.text_input("Company Name")

    role = st.text_input("Job Role")

    if st.button("Generate Cover Letter"):

        if not (name and company and role):
            st.warning("Please fill all fields.")
            return

        generator = CoverLetterGenerator()

        with st.spinner("Generating Cover Letter..."):

            letter = generator.generate(
                name,
                company,
                role
            )

        st.success("Cover Letter Generated Successfully!")

        st.text_area(
            "Generated Cover Letter",
            value=letter,
            height=350
        )