"""
=========================================================
Resume Intelligence AI
EDA & Analytics Engine
Author : Naveen Kumar
Version : 5.0
=========================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class ResumeAnalytics:

    def __init__(self):
        pass

    # -----------------------------------------
    # Resume Statistics
    # -----------------------------------------

    def summary(self, features):

        return pd.DataFrame({

            "Metric":[
                "Experience",
                "Projects",
                "Certifications",
                "Resume Words",
                "Resume Score"
            ],

            "Value":[
                features["Experience"],
                features["Projects"],
                features["Certifications"],
                features["Resume Words"],
                features["Resume Quality Score"]
            ]

        })

    # -----------------------------------------

    def skill_distribution(self, matched, missing):

        return pd.DataFrame({

            "Category":[

                "Matched Skills",

                "Missing Skills"

            ],

            "Count":[

                len(matched),

                len(missing)

            ]

        })

    # -----------------------------------------

    def pie_chart(self, matched, missing):

        fig, ax = plt.subplots(figsize=(5,5))

        ax.pie(

            [

                len(matched),

                len(missing)

            ],

            labels=["Matched","Missing"],

            autopct="%1.1f%%"

        )

        ax.set_title("Skill Distribution")

        return fig

    # -----------------------------------------

    def experience_level(self, years):

        if years <= 1:

            return "Fresher"

        elif years <= 3:

            return "Junior"

        elif years <= 7:

            return "Mid Level"

        elif years <= 12:

            return "Senior"

        return "Leadership"

    # -----------------------------------------

    def resume_strength(self, score):

        if score >= 90:

            return "Excellent"

        elif score >= 75:

            return "Strong"

        elif score >= 60:

            return "Average"

        elif score >= 40:

            return "Weak"

        return "Very Weak"

    # -----------------------------------------

    def dashboard_metrics(

            self,

            ats,

            similarity,

            quality

    ):

        return {

            "ATS Score": ats,

            "Similarity": similarity,

            "Resume Quality": quality

        }