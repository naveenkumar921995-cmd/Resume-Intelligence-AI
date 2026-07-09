"""
=========================================================
Resume Intelligence AI
Learning Recommendation Engine
Author : Naveen Kumar
Version : 6.0
=========================================================
"""

import pandas as pd


class LearningRecommender:

    def __init__(self):

        self.learning = pd.read_csv(
            "data/learning_paths.csv"
        )

    # ----------------------------------

    def recommend(self, missing_skills):

        recommendations = []

        for skill in missing_skills:

            row = self.learning[
                self.learning["Skill"].str.lower()
                == skill.lower()
            ]

            if not row.empty:

                recommendations.append({

                    "Skill": row.iloc[0]["Skill"],

                    "Difficulty": row.iloc[0]["Difficulty"],

                    "Duration": row.iloc[0]["Duration"],

                    "Course": row.iloc[0]["Course"],

                    "Project": row.iloc[0]["Project"]

                })

        return pd.DataFrame(recommendations)

    # ----------------------------------

    def roadmap(self, recommendations):

        phases = []

        for _, row in recommendations.iterrows():

            phases.append(

                f"Learn {row['Skill']} "

                f"({row['Duration']}) → "

                f"Build: {row['Project']}"

            )

        return phases