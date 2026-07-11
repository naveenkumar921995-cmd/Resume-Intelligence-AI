def metric_card(
    title,
    value,
    delta=None,
    help_text=None
):
    elif menu == "📊 ATS Analysis":

    st.header("📊 ATS Resume Analysis")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=SUPPORTED_FILES,
        key="ats"
    )

    if uploaded_file:

        from core.resume_parser import parse_resume
        from core.keyword_engine import KeywordEngine

        resume = parse_resume(uploaded_file)

        engine = KeywordEngine()

        score = engine.ats_score(resume)

        st.metric(
            "ATS Score",
            f"{score}%"
        )

        st.progress(score/100)
