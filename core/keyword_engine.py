"""
=========================================================
Resume Intelligence AI
Keyword & ATS Engine
Author : Naveen Kumar
Version : 5.0
=========================================================
"""

import pandas as pd
import re


class KeywordEngine:

    def __init__(self, skills_file="data/skills_master.csv"):

        self.skills = pd.read_csv(skills_file)

    # ------------------------------------
    # Clean Resume
    # ------------------------------------

    def clean(self, text):

        text = text.lower()

        text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)

        return text

    # ------------------------------------
    # Extract Skills
    # ------------------------------------

    def extract_skills(self, resume_text):

        resume = self.clean(resume_text)

        found = []

        for skill in self.skills["Skill"]:

            if skill.lower() in resume:

                found.append(skill)

        return sorted(list(set(found)))

    # ------------------------------------
    # Technical Skills
    # ------------------------------------

    def technical_skills(self, skills):

        df = self.skills

        technical = df[
            df["Category"].isin(
                [
                    "Programming",
                    "Database",
                    "Machine Learning",
                    "Deep Learning",
                    "Artificial Intelligence",
                    "Cloud",
                    "Deployment",
                    "DevOps",
                    "Facility Management",
                    "Analytics",
                    "Data Visualization"
                ]
            )
        ]

        return list(
            set(skills).intersection(
                set(technical["Skill"])
            )
        )

    # ------------------------------------
    # Soft Skills
    # ------------------------------------

    def soft_skills(self, skills):

        df = self.skills

        soft = df[
            df["Category"] == "Soft Skill"
        ]

        return list(
            set(skills).intersection(
                set(soft["Skill"])
            )
        )

    # ------------------------------------
    # Match Skills
    # ------------------------------------

    def compare(self, resume_skills, required_skills):

        matched = []

        missing = []

        for skill in required_skills:

            if skill in resume_skills:

                matched.append(skill)

            else:

                missing.append(skill)

        return matched, missing

    # ------------------------------------
    # ATS %
    # ------------------------------------

    def ats_score(self, matched, required):

        if len(required) == 0:

            return 0

        return round(
            len(matched) / len(required) * 100,
            2
        )

    # ------------------------------------
    # Skill Gap
    # ------------------------------------

    def skill_gap(self, matched, missing):

        return {

            "Matched Skills": len(matched),

            "Missing Skills": len(missing),

            "Gap %": round(

                len(missing) /

                (len(matched)+len(missing))

                *100,

                2

            )

        }

    # ------------------------------------
    # Importance Ranking
    # ------------------------------------

    def rank_missing(self, missing):

        priority = []

        for skill in missing:

            priority.append(

                {

                    "Skill": skill,

                    "Priority": "High"

                }

            )

        return pd.DataFrame(priority)

    # ------------------------------------
    # Complete ATS Analysis
    # ------------------------------------

    def analyze(self, resume_text, required_skills):

        resume_skills = self.extract_skills(resume_text)

        matched, missing = self.compare(

            resume_skills,

            required_skills

        )

        report = {

            "Resume Skills": resume_skills,

            "Technical Skills":

                self.technical_skills(resume_skills),

            "Soft Skills":

                self.soft_skills(resume_skills),

            "Matched Skills": matched,

            "Missing Skills": missing,

            "ATS Score":

                self.ats_score(

                    matched,

                    required_skills

                ),

            "Skill Gap":

                self.skill_gap(

                    matched,

                    missing

                ),

            "Priority":

                self.rank_missing(

                    missing

                )

        }

        return report