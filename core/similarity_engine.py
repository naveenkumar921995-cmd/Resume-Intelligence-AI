"""
=========================================================
NEXUS AI
Enterprise NLP Similarity Engine
Author : Naveen Kumar
Version : 9.0
=========================================================
"""

import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SimilarityEngine:

    def __init__(self):

        self.vectorizer = TfidfVectorizer(

            stop_words="english",

            lowercase=True

        )

    # --------------------------------------------------
    # Clean Text
    # --------------------------------------------------

    def clean_text(self, text):

        if text is None:

            return ""

        text = str(text).lower()

        text = re.sub(r"[^a-zA-Z0-9 ]", " ", text)

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    # --------------------------------------------------
    # Vectorization
    # --------------------------------------------------

    def vectorize(

        self,

        resume,

        job

    ):

        resume = self.clean_text(resume)

        job = self.clean_text(job)

        vectors = self.vectorizer.fit_transform(

            [

                resume,

                job

            ]

        )

        return vectors

    # --------------------------------------------------
    # Similarity Score
    # --------------------------------------------------

    def similarity_score(

        self,

        resume,

        job

    ):

        if not resume or not job:

            return 0.0

        vectors = self.vectorize(

            resume,

            job

        )

        score = cosine_similarity(

            vectors[0],

            vectors[1]

        )[0][0]

        return round(

            score * 100,

            2

        )

    # --------------------------------------------------
    # Grade
    # --------------------------------------------------

    def grade(

        self,

        score

    ):

        if score >= 95:

            return "A+"

        elif score >= 85:

            return "A"

        elif score >= 75:

            return "B+"

        elif score >= 65:

            return "B"

        else:

            return "C"

    # --------------------------------------------------
    # Hiring Status
    # --------------------------------------------------

    def hiring_status(

        self,

        score

    ):

        if score >= 95:

            return "🟢 Outstanding Match"

        elif score >= 85:

            return "🟢 Highly Recommended"

        elif score >= 75:

            return "🟡 Recommended"

        elif score >= 60:

            return "🟠 Consider After Review"

        else:

            return "🔴 Poor Match"

    # --------------------------------------------------
    # Confidence
    # --------------------------------------------------

    def confidence(

        self,

        score

    ):

        if score >= 90:

            return "Very High"

        elif score >= 75:

            return "High"

        elif score >= 60:

            return "Medium"

        else:

            return "Low"

    # --------------------------------------------------
    # Recommendation
    # --------------------------------------------------

    def recommendation(

        self,

        score

    ):

        if score >= 90:

            return (
                "Excellent alignment between the resume and "
                "the job description."
            )

        elif score >= 75:

            return (
                "Good match. Improve a few missing skills "
                "to increase ATS performance."
            )

        elif score >= 60:

            return (
                "Average match. Add more technical keywords, "
                "projects and measurable achievements."
            )

        elif score >= 40:

            return (
                "Resume requires optimization before applying."
            )

        else:

            return (
                "Resume has very low similarity with the target role."
            )

    # --------------------------------------------------
    # Keyword Match
    # --------------------------------------------------

    def keyword_match(

        self,

        resume,

        job

    ):

        resume_words = set(

            self.clean_text(resume).split()

        )

        job_words = set(

            self.clean_text(job).split()

        )

        if len(job_words) == 0:

            return 0

        matched = resume_words.intersection(job_words)

        return round(

            len(matched) / len(job_words) * 100,

            2

        )

    # --------------------------------------------------
    # Complete Analysis
    # --------------------------------------------------

    def analyze(

        self,

        resume,

        job

    ):

        score = self.similarity_score(

            resume,

            job

        )

        keyword_score = self.keyword_match(

            resume,

            job

        )

        return {

            "Similarity Score": score,

            "Keyword Match": keyword_score,

            "Grade": self.grade(score),

            "Confidence": self.confidence(score),

            "Hiring Status": self.hiring_status(score),

            "Recommendation": self.recommendation(score)

        }