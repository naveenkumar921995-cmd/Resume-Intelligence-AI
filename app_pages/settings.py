import streamlit as st
from config import APP_VERSION


def settings_page():
    """
    Application Settings Page
    """

    st.header("⚙️ Settings")

    st.subheader("Application Information")

    st.write(f"**Application Version:** {APP_VERSION}")
    st.write("**Developer:** Naveen Kumar")

    st.divider()

    st.subheader("About")

    st.info(
        """
        NEXUS AI is an AI-powered Talent Intelligence Platform.

        Features:
        • Resume Intelligence
        • ATS Analysis
        • Hiring Prediction
        • AI Career Coach
        • Executive Reports
        • Learning Roadmaps
        """
    )