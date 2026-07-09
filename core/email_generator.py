"""
=========================================================
Resume Intelligence AI
Professional Email Generator
Author : Naveen Kumar
Version : 6.0
=========================================================
"""

from datetime import datetime


class EmailGenerator:

    def __init__(self):
        pass

    # ---------------------------------------------------
    # Job Application Email
    # ---------------------------------------------------

    def application_email(

        self,

        candidate_name,

        company,

        role

    ):

        email = f"""
Subject: Application for {role}

Dear Hiring Manager,

I hope you are doing well.

I am writing to express my interest in the {role} position at {company}.

My background includes experience in Python, Data Analytics, Machine Learning, AI, and software development. I have also developed multiple end-to-end projects demonstrating practical implementation of these skills.

I have attached my resume for your review and would appreciate the opportunity to discuss how I can contribute to your organization.

Thank you for your valuable time.

Kind Regards,

{candidate_name}
"""

        return email

    # ---------------------------------------------------
    # HR Follow-up Email
    # ---------------------------------------------------

    def followup_email(

        self,

        candidate_name,

        company,

        role

    ):

        email = f"""
Subject: Follow-up Regarding {role} Application

Dear Hiring Manager,

I hope you are doing well.

I wanted to follow up regarding my application for the {role} position at {company}.

I remain very interested in this opportunity and would appreciate any updates regarding the recruitment process.

Thank you for your consideration.

Best Regards,

{candidate_name}
"""

        return email

    # ---------------------------------------------------
    # Interview Thank You Email
    # ---------------------------------------------------

    def thankyou_email(

        self,

        candidate_name,

        interviewer,

        company,

        role

    ):

        email = f"""
Subject: Thank You for the Interview Opportunity

Dear {interviewer},

Thank you for taking the time to interview me for the {role} position at {company}.

It was a pleasure discussing the role and learning more about your organization.

I appreciate the opportunity and look forward to hearing from you.

Kind Regards,

{candidate_name}
"""

        return email

    # ---------------------------------------------------
    # Interview Invitation Reply
    # ---------------------------------------------------

    def interview_acceptance(

        self,

        candidate_name,

        company,

        interview_date

    ):

        email = f"""
Subject: Interview Confirmation

Dear Hiring Team,

Thank you for inviting me to interview with {company}.

I am pleased to confirm my availability for the interview scheduled on {interview_date}.

I look forward to speaking with you.

Best Regards,

{candidate_name}
"""

        return email

    # ---------------------------------------------------
    # Offer Acceptance
    # ---------------------------------------------------

    def offer_acceptance(

        self,

        candidate_name,

        company,

        role

    ):

        email = f"""
Subject: Acceptance of Offer - {role}

Dear Hiring Manager,

Thank you for offering me the position of {role} at {company}.

I am delighted to accept the offer and look forward to joining your team.

Thank you once again for this opportunity.

Warm Regards,

{candidate_name}
"""

        return email

    # ---------------------------------------------------
    # Offer Decline
    # ---------------------------------------------------

    def offer_decline(

        self,

        candidate_name,

        company,

        role

    ):

        email = f"""
Subject: Offer for {role}

Dear Hiring Manager,

Thank you very much for offering me the position of {role} at {company}.

After careful consideration, I have decided to decline the offer at this time.

I sincerely appreciate your time and wish the organization continued success.

Kind Regards,

{candidate_name}
"""

        return email