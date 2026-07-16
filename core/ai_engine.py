"""
=========================================================
Resume Intelligence AI
Universal AI Engine
Version : 9.1 Enterprise
Author : Naveen Kumar
=========================================================
"""

from core.analytics import ResumeAnalytics
from core.ml_prediction import MLPredictor

try:
    from core.deep_learning import DeepLearningModel
    DL_AVAILABLE = True
except Exception:
    DL_AVAILABLE = False

try:
    from core.llm_engine import LLMEngine
    LLM_AVAILABLE = True
except Exception:
    LLM_AVAILABLE = False


class AIEngine:

    def __init__(self):

        self.analytics = ResumeAnalytics()

        self.ml = MLPredictor()

        self.dl = DeepLearningModel() if DL_AVAILABLE else None

        self.llm = LLMEngine() if LLM_AVAILABLE else None

    # ==================================================
    # Machine Learning
    # ==================================================

    def ml_prediction(self, **kwargs):

        return self.ml.full_report(**kwargs)

    # ==================================================
    # Deep Learning
    # ==================================================

    def dl_prediction(self, **kwargs):

        if self.dl is None:

            return {

                "Hiring Score": 0,

                "Grade": "-",

                "Hiring Status": "Unavailable",

                "Recommendation": "Deep Learning module is disabled."

            }

        return self.dl.full_report(**kwargs)

    # ==================================================
    # Analytics
    # ==================================================

    def analytics_summary(self, features):

        return self.analytics.summary(features)

    def dashboard_metrics(

        self,

        ats,

        similarity,

        quality

    ):

        return self.analytics.dashboard_metrics(

            ats,

            similarity,

            quality

        )

    # ==================================================
    # AI Career Coach
    # ==================================================

    def ai_review(

        self,

        ats,

        similarity,

        quality,

        experience,

        matched,

        missing

    ):

        if self.llm is None:

            return {

                "AI Review": [

                    "LLM Engine not available."

                ],

                "Recruiter Decision": "Unavailable",

                "Learning Plan": []

            }

        return self.llm.generate_report(

            ats=ats,

            similarity=similarity,

            quality=quality,

            experience=experience,

            matched=matched,

            missing=missing

        )

    # ==================================================
    # Enterprise Report
    # ==================================================

    def enterprise_report(

        self,

        ats,

        similarity,

        quality,

        experience,

        matched,

        missing,

        ml_kwargs,

        dl_kwargs

    ):

        return {

            "Analytics":

                self.dashboard_metrics(

                    ats,

                    similarity,

                    quality

                ),

            "Machine Learning":

                self.ml_prediction(

                    **ml_kwargs

                ),

            "Deep Learning":

                self.dl_prediction(

                    **dl_kwargs

                ),

            "AI Review":

                self.ai_review(

                    ats,

                    similarity,

                    quality,

                    experience,

                    matched,

                    missing

                )

        }