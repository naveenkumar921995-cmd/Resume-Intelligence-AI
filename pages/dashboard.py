def dashboard_page():
    if menu=="🏠 Dashboard":

    st.title("🤖 Resume Intelligence AI")

    st.markdown("""

### Enterprise AI Career Intelligence Platform

Analyze resumes using

- ATS Logic
- NLP
- Machine Learning
- Deep Learning
- AI Career Guidance
- Skill Gap Analysis
- Recruiter Intelligence
- Learning Recommendation
- Resume Intelligence

---
""")

    c1,c2,c3,c4=st.columns(4)

    c1.metric(
        "Departments",
        TOTAL_DEPARTMENTS
    )

    c2.metric(
        "Job Roles",
        TOTAL_JOB_ROLES
    )

    c3.metric(
        "Skills",
        TOTAL_SKILLS
    )

    c4.metric(
        "AI Modules",
        TOTAL_AI_MODULES
    )

    st.divider()

    st.subheader("Technology Stack")
        tech = pd.DataFrame({

        "Category":[

            "Programming",

            "Analytics",

            "Machine Learning",

            "Deep Learning",

            "Natural Language Processing",

            "Generative AI",

            "Visualization",

            "Deployment"

        ],

        "Technology":[

            "Python",

            "NumPy • Pandas",

            "Scikit-learn",

            "TensorFlow",

            "Regex • TF-IDF • spaCy",

            "OpenAI • Ollama • Gemini",

            "Matplotlib • Plotly",

            "Streamlit"

        ]

    })

    st.dataframe(

        tech,

        hide_index=True,

        use_container_width=True

    )

    st.divider()

    st.subheader("Platform Features")

    feature1,feature2=st.columns(2)

    with feature1:

        st.success("Resume Parsing")

        st.success("ATS Resume Analysis")

        st.success("Skill Gap Analysis")

        st.success("Resume Ranking")

        st.success("Department-wise Analysis")

        st.success("Learning Recommendation")

        st.success("Interview Questions")

    with feature2:

        st.success("Machine Learning")

        st.success("Deep Learning")

        st.success("NLP Similarity")

        st.success("AI Resume Review")

        st.success("Cover Letter")

        st.success("Email Generator")

        st.success("Recruiter Dashboard")

    st.divider()

    st.subheader("Workflow")

    st.markdown("""

Upload Resume

⬇

Resume Parsing

⬇

Feature Engineering

⬇

ATS Analysis

⬇

NLP Similarity

⬇

Machine Learning Prediction

⬇

Deep Learning Prediction

⬇

Skill Gap Analysis

⬇

AI Recommendation

⬇

Generate Report

""")
