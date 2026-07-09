"""
==========================================================
Resume Intelligence AI
AI Interview Question Generator
Author : Naveen Kumar
Version : 6.0
==========================================================
"""

import random


class InterviewGenerator:

    def __init__(self):
        pass

    # ------------------------------------

    def technical_questions(
        self,
        matched_skills,
        experience
    ):

        questions = []

        for skill in matched_skills:

            questions.append(

                f"Explain your practical experience with {skill}."

            )

            questions.append(

                f"What challenges did you face while using {skill}?"

            )

            if experience >= 3:

                questions.append(

                    f"Describe a real project where {skill} improved business outcomes."

                )

        return questions

    # ------------------------------------

    def missing_skill_questions(self, missing):

        questions = []

        for skill in missing:

            questions.append(

                f"If assigned a project requiring {skill}, how would you learn and implement it?"

            )

        return questions

    # ------------------------------------

    def behavioral_questions(self):

        return [

            "Describe a difficult problem you solved.",

            "Tell us about a project you are proud of.",

            "How do you prioritize multiple deadlines?",

            "Describe a leadership situation.",

            "How do you handle criticism?",

            "Explain a failure and what you learned.",

            "How do you work under pressure?"

        ]

    # ------------------------------------

    def hr_questions(self):

        return [

            "Tell me about yourself.",

            "Why should we hire you?",

            "Where do you see yourself in five years?",

            "Why are you leaving your current job?",

            "Describe your biggest strength.",

            "Describe one weakness you're improving."

        ]

    # ------------------------------------

    def generate(

        self,

        matched_skills,

        missing_skills,

        experience

    ):

        questions = []

        questions.extend(

            self.technical_questions(

                matched_skills,

                experience

            )

        )

        questions.extend(

            self.missing_skill_questions(

                missing_skills

            )

        )

        questions.extend(

            self.behavioral_questions()

        )

        questions.extend(

            self.hr_questions()

        )

        random.shuffle(questions)

        return questions[:20]