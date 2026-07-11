def resume_analyzer_page():
    elif menu == "📄 Resume Analyzer":

    from core.resume_parser import parse_resume
    from core.keyword_engine import KeywordEngine
    

    st.header("📄 Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=SUPPORTED_FILES
    )

    if uploaded_file:

        resume_text = parse_resume(uploaded_file)

        st.subheader("Resume Preview")

        st.text_area(
            "",
            resume_text,
            height=300
        )

        st.metric(
            "Total Words",
            len(resume_text.split())
        )
