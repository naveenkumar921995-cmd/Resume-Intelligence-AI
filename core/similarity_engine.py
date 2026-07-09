"""
====================================================
Resume Intelligence AI
NLP Similarity Engine
Author : Naveen Kumar
Version : 5.0
====================================================
"""

import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity


class SimilarityEngine:

    def __init__(self):

        self.vectorizer = TfidfVectorizer(
            stop_words="english"
        )

    # ----------------------------------------
    # TF-IDF Vectorization
    # ----------------------------------------

    def vectorize(self, resume, job):

        vectors = self.vectorizer.fit_transform(

            [resume, job]

        )

        return vectors

    # ----------------------------------------
    # Cosine Similarity
    # ----------------------------------------

    def similarity_score(self, resume, job):

        vectors = self.vectorize(

            resume,

            job

        )

        similarity = cosine_similarity(

            vectors[0],

            vectors[1]

        )[0][0]

        return round(

            similarity * 100,

            2

        )

    # ----------------------------------------
    # Similarity Grade
    # ----------------------------------------

    def grade(self, score):

        if score >= 90:

            return "Excellent"

        elif score >= 75:

            return "Very Good"

        elif score >= 60:

            return "Good"

        elif score >= 40:

            return "Average"

        else:

            return "Poor"

    # ----------------------------------------
    # Recommendation
    # ----------------------------------------

    def recommendation(self, score):

        if score >= 90:

            return "Resume is highly aligned with the selected job role."

        elif score >= 75:

            return "Resume is well matched. Minor improvements recommended."

        elif score >= 60:

            return "Improve missing technical skills and ATS keywords."

        elif score >= 40:

            return "Resume requires significant optimization."

        return "Resume requires major improvements before applying."

    # ----------------------------------------
    # Complete Analysis
    # ----------------------------------------

    def analyze(self, resume, job):

        score = self.similarity_score(

            resume,

            job

        )

        return {

            "Similarity Score": score,

            "Grade": self.grade(score),

            "Recommendation":

                self.recommendation(score)

        }