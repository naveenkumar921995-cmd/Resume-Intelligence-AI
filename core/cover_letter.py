"""
=========================================================
Resume Intelligence AI
AI Cover Letter Generator
Author : Naveen Kumar
Version : 6.0
=========================================================
"""

from datetime import datetime


class CoverLetterGenerator:

    def __init__(self):
        pass

    # --------------------------------------

    def generate(

        self,

        candidate_name,

        company,

        department,

        role,

        experience,

        matched_skills,

        projects

    ):

        today = datetime.today().strftime("%d %B %Y")

        skills = ", ".join(matched_skills[:8])

        letter = f"""

Date: {today}

Hiring Manager
{company}

Subject: Application for {role}

Dear Hiring Manager,

I am writing to express my interest in the {role} position within your {department} department.

With over {experience} years of professional experience and hands-on exposure to {skills}, I have developed practical problem-solving abilities while delivering successful projects.

Throughout my career, I have completed approximately {projects} technical projects, strengthening my expertise in software development, analytics, automation, and continuous learning.

My technical foundation includes Python, Machine Learning, Data Analysis, NLP, and modern AI tools. I enjoy solving real-world problems through data-driven approaches and continuously expanding my technical capabilities.

I would welcome the opportunity to discuss how my skills and experience can contribute to your organization's success.

Thank you for your time and consideration.

Sincerely,

{candidate_name}

"""

        return letter