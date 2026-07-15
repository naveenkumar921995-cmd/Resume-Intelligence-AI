"""
=========================================================
NEXUS AI
Hiring Score Engine
Author : Naveen Kumar
=========================================================
"""


def calculate_hiring_score(
    ats_score,
    ml_prediction,
    dl_prediction,
    similarity_score,
    technical_score,
    soft_skill_score,
    experience_score
):
    """
    Calculate final hiring score.
    """

    scores = [
        ats_score,
        ml_prediction,
        dl_prediction,
        similarity_score,
        technical_score,
        soft_skill_score,
        experience_score,
    ]

    final_score = round(sum(scores) / len(scores), 2)

    if final_score >= 95:
        recommendation = "Outstanding Candidate 🟢"
        grade = "A+"
        risk = "Low"

    elif final_score >= 85:
        recommendation = "Highly Recommended 🟢"
        grade = "A"
        risk = "Low"

    elif final_score >= 75:
        recommendation = "Recommended 🟡"
        grade = "B+"
        risk = "Medium"

    elif final_score >= 60:
        recommendation = "Consider After Review 🟠"
        grade = "B"
        risk = "Medium"

    else:
        recommendation = "Not Recommended 🔴"
        grade = "C"
        risk = "High"

    return {
        "Hiring Score": final_score,
        "Grade": grade,
        "Recommendation": recommendation,
        "Skill Gap Risk": risk,
    }