"""
====================================================
Resume Intelligence AI
GenAI Resume Reviewer
Version : 5.0
====================================================
"""

class LLMEngine:

    def __init__(self):
        pass

    # ----------------------------------

    def review_resume(

        self,

        ats,

        similarity,

        quality,

        experience,

        matched,

        missing

    ):

        review=[]

        if ats<70:

            review.append(
                "ATS compatibility is below industry standards."
            )

        else:

            review.append(
                "Resume has good ATS compatibility."
            )

        if similarity<75:

            review.append(
                "Resume should be aligned more closely with the selected job role."
            )

        else:

            review.append(
                "Resume matches the selected job role well."
            )

        if quality<70:

            review.append(
                "Resume formatting and content quality can be improved."
            )

        else:

            review.append(
                "Resume quality is professional."
            )

        if experience<2:

            review.append(
                "Highlight internships, projects and certifications."
            )

        elif experience<5:

            review.append(
                "Add measurable achievements from previous roles."
            )

        else:

            review.append(
                "Leadership achievements should be highlighted."
            )

        if len(missing)>0:

            review.append(

                "Top missing skills: "

                +", ".join(missing[:5])

            )

        return review

    # ----------------------------------

    def recruiter_feedback(

        self,

        score

    ):

        if score>=90:

            return "Strongly Recommended"

        elif score>=80:

            return "Recommended"

        elif score>=65:

            return "Can be Shortlisted"

        elif score>=50:

            return "Needs Resume Improvement"

        else:

            return "Not Suitable Currently"

    # ----------------------------------

    def improvement_plan(

        self,

        missing

    ):

        plan=[]

        for skill in missing:

            plan.append(

                f"Learn {skill}"

            )

        return plan

    # ----------------------------------

    def generate_report(

        self,

        ats,

        similarity,

        quality,

        experience,

        matched,

        missing

    ):

        return{

            "AI Review":

            self.review_resume(

                ats,

                similarity,

                quality,

                experience,

                matched,

                missing

            ),

            "Recruiter Decision":

            self.recruiter_feedback(

                ats

            ),

            "Learning Plan":

            self.improvement_plan(

                missing

            )

        }
generate()

chat()

summarize()

career_advice()

cover_letter()

interview_questions()