"""
=========================================================
NEXUS AI
Enterprise LLM Engine
Author : Naveen Kumar
Version : 9.0
=========================================================
"""

from datetime import datetime


class LLMEngine:

    def __init__(self):
        pass

    # ==================================================
    # Resume Review
    # ==================================================

    def review_resume(
        self,
        ats,
        similarity,
        quality,
        experience,
        matched,
        missing
    ):

        review = []

        if ats >= 90:
            review.append("Excellent ATS compatibility.")
        elif ats >= 70:
            review.append("Good ATS compatibility.")
        else:
            review.append("ATS compatibility requires improvement.")

        if similarity >= 80:
            review.append("Resume is strongly aligned with the target job.")
        else:
            review.append("Improve alignment with the job description.")

        if quality >= 80:
            review.append("Resume formatting and content are professional.")
        else:
            review.append("Improve formatting, readability and content quality.")

        if experience < 2:
            review.append("Highlight internships, projects and certifications.")
        elif experience < 5:
            review.append("Include measurable achievements.")
        else:
            review.append("Highlight leadership and business impact.")

        if missing:
            review.append(
                "Top missing skills: "
                + ", ".join(missing[:5])
            )

        return review

    # ==================================================
    # Strengths
    # ==================================================

    def strengths(self, matched):

        if not matched:
            return ["No technical strengths identified."]

        return [f"Strong knowledge of {skill}" for skill in matched[:10]]

    # ==================================================
    # Weaknesses
    # ==================================================

    def weaknesses(self, missing):

        if not missing:
            return ["No major weaknesses detected."]

        return [f"Improve {skill}" for skill in missing[:10]]

    # ==================================================
    # Recruiter Decision
    # ==================================================

    def recruiter_feedback(self, score):

        if score >= 95:
            return "Outstanding Candidate"

        elif score >= 85:
            return "Highly Recommended"

        elif score >= 75:
            return "Recommended"

        elif score >= 60:
            return "Consider After Review"

        return "Not Recommended"

    # ==================================================
    # Hiring Probability
    # ==================================================

    def hiring_probability(self, score):

        return min(100, max(0, score))

    # ==================================================
    # Career Advice
    # ==================================================

    def career_advice(
        self,
        experience,
        missing
    ):

        advice = []

        if experience < 2:
            advice.append(
                "Focus on internships and real-world projects."
            )

        elif experience < 5:
            advice.append(
                "Build domain expertise and advanced certifications."
            )

        else:
            advice.append(
                "Develop leadership and mentoring skills."
            )

        if missing:
            advice.append(
                "Prioritize learning: "
                + ", ".join(missing[:5])
            )

        advice.append(
            "Maintain an updated LinkedIn and GitHub portfolio."
        )

        return advice

    # ==================================================
    # Executive Summary
    # ==================================================

    def summarize(
        self,
        ats,
        similarity,
        quality
    ):

        return (
            f"ATS Score: {ats}% | "
            f"Similarity: {similarity}% | "
            f"Resume Quality: {quality}%"
        )

    # ==================================================
    # AI Chat
    # ==================================================

    def chat(
        self,
        message
    ):

        message = message.lower()

        if "resume" in message:
            return "I can help improve your resume."

        if "ats" in message:
            return "Use relevant keywords from the job description."

        if "interview" in message:
            return "Practice technical and behavioral questions."

        if "career" in message:
            return "Continue learning in-demand technologies and build strong projects."

        return "Please ask a resume, interview, ATS or career-related question."

    # ==================================================
    # Cover Letter Prompt
    # ==================================================

    def cover_letter(
        self,
        role
    ):

        return (
            f"Generate a professional cover letter for the position of {role}."
        )

    # ==================================================
    # Interview Prompt
    # ==================================================

    def interview_questions(
        self,
        role
    ):

        return (
            f"Generate interview questions for {role}."
        )

    # ==================================================
    # Generic Generate
    # ==================================================

    def generate(
        self,
        ats,
        similarity,
        quality,
        experience,
        matched,
        missing
    ):

        return {

            "Executive Summary":
                self.summarize(
                    ats,
                    similarity,
                    quality
                ),

            "AI Review":
                self.review_resume(
                    ats,
                    similarity,
                    quality,
                    experience,
                    matched,
                    missing
                ),

            "Strengths":
                self.strengths(
                    matched
                ),

            "Weaknesses":
                self.weaknesses(
                    missing
                ),

            "Career Advice":
                self.career_advice(
                    experience,
                    missing
                ),

            "Recruiter Decision":
                self.recruiter_feedback(
                    ats
                ),

            "Hiring Probability":
                self.hiring_probability(
                    ats
                ),

            "Generated On":
                datetime.now().strftime(
                    "%d-%m-%Y %H:%M"
                )
        }