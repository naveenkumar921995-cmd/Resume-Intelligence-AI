"""
=========================================================
NEXUS AI
Enterprise Keyword Engine
Version : 10.0 Enterprise
Author : Naveen Kumar
=========================================================
"""

import re
from collections import Counter


class KeywordEngine:

    def __init__(self):

        self.skill_database = {

            "Programming": [
                "Python", "Java", "C", "C++", "C#", "JavaScript",
                "TypeScript", "Go", "Rust", "PHP", "R", "MATLAB"
            ],

            "Data Science": [
                "NumPy", "Pandas", "Scikit-learn",
                "Matplotlib", "Seaborn",
                "Plotly", "SciPy", "OpenCV"
            ],

            "Machine Learning": [
                "Machine Learning",
                "Deep Learning",
                "TensorFlow",
                "PyTorch",
                "Keras",
                "XGBoost",
                "LightGBM",
                "CatBoost"
            ],

            "NLP": [
                "NLP",
                "spaCy",
                "NLTK",
                "Transformers",
                "BERT",
                "GPT",
                "LangChain",
                "RAG",
                "FAISS"
            ],

            "Databases": [
                "SQL",
                "MySQL",
                "PostgreSQL",
                "MongoDB",
                "Oracle",
                "SQLite"
            ],

            "Cloud": [
                "AWS",
                "Azure",
                "Google Cloud",
                "GCP"
            ],

            "DevOps": [
                "Docker",
                "Kubernetes",
                "Git",
                "GitHub",
                "CI/CD",
                "Linux",
                "Jenkins"
            ],

            "BI": [
                "Excel",
                "Power BI",
                "Tableau",
                "Looker"
            ]
        }

        self.soft_skills = [

            "Leadership",
            "Communication",
            "Problem Solving",
            "Critical Thinking",
            "Teamwork",
            "Decision Making",
            "Presentation",
            "Negotiation",
            "Management",
            "Time Management"

        ]

        self.certifications = [

            "AWS Certified",
            "Azure",
            "Google Professional",
            "PMP",
            "ITIL",
            "CCNA",
            "CompTIA",
            "Microsoft Certified",
            "Oracle Certified"

        ]

    # --------------------------------------------------

    def clean_text(self, text):

        return re.sub(r"\s+", " ", text.lower())

    # --------------------------------------------------

    def extract_skills(self, text):

        text = self.clean_text(text)

        found = []

        for category in self.skill_database.values():

            for skill in category:

                if skill.lower() in text:

                    found.append(skill)

        return sorted(list(set(found)))

    # --------------------------------------------------

    def extract_soft_skills(self, text):

        text = self.clean_text(text)

        found = []

        for skill in self.soft_skills:

            if skill.lower() in text:

                found.append(skill)

        return sorted(found)

    # --------------------------------------------------

    def extract_certifications(self, text):

        text = self.clean_text(text)

        found = []

        for cert in self.certifications:

            if cert.lower() in text:

                found.append(cert)

        return sorted(found)

    # --------------------------------------------------

    def keyword_frequency(self, text):

        words = re.findall(r"\b\w+\b", text.lower())

        return Counter(words)

    # --------------------------------------------------

    def keyword_density(self, text):

        words = re.findall(r"\b\w+\b", text.lower())

        total = len(words)

        freq = Counter(words)

        density = {}

        for word, count in freq.items():

            density[word] = round(count / total * 100, 2)

        return density

    # --------------------------------------------------

    def missing_keywords(self, resume_text, job_keywords):

        resume = self.clean_text(resume_text)

        missing = []

        for keyword in job_keywords:

            if keyword.lower() not in resume:

                missing.append(keyword)

        return missing

    # --------------------------------------------------

    def matched_keywords(self, resume_text, job_keywords):

        resume = self.clean_text(resume_text)

        matched = []

        for keyword in job_keywords:

            if keyword.lower() in resume:

                matched.append(keyword)

        return matched

    # --------------------------------------------------

    def keyword_score(self, resume_text, job_keywords):

        matched = self.matched_keywords(

            resume_text,

            job_keywords

        )

        if len(job_keywords) == 0:

            return 0

        score = len(matched) / len(job_keywords) * 100

        return round(score, 2)

    # --------------------------------------------------

    def role_database(self):

        return {

            "Data Scientist": [

                "Python",

                "Machine Learning",

                "Deep Learning",

                "SQL",

                "Pandas",

                "NumPy",

                "TensorFlow",

                "Scikit-learn"

            ],

            "Data Analyst": [

                "Excel",

                "SQL",

                "Power BI",

                "Python",

                "Tableau",

                "Statistics"

            ],

            "AI Engineer": [

                "Python",

                "TensorFlow",

                "PyTorch",

                "LangChain",

                "RAG",

                "LLM",

                "Docker"

            ],

            "Backend Developer": [

                "Python",

                "Java",

                "SQL",

                "Docker",

                "Git",

                "API"

            ]

        }

    # --------------------------------------------------

    def role_match(self, resume_text, role):

        db = self.role_database()

        if role not in db:

            return 0

        return self.keyword_score(

            resume_text,

            db[role]

        )

    # --------------------------------------------------

    def summary(self, resume_text):

        return {

            "Technical Skills":

                self.extract_skills(resume_text),

            "Soft Skills":

                self.extract_soft_skills(resume_text),

            "Certifications":

                self.extract_certifications(resume_text)

        }