"""
=========================================================
Resume Intelligence AI
Machine Learning Prediction Engine
Version : 8.0
Author : Naveen Kumar
=========================================================
"""

import os
import joblib
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

try:
    from xgboost import XGBRegressor
    XGBOOST_AVAILABLE = True
except:
    XGBOOST_AVAILABLE = False


class MLPredictor:

    def __init__(self):

        self.models = {}

        self.model_folder = "models"

        os.makedirs(self.model_folder, exist_ok=True)

    # -------------------------------------------------
    # Sample Dataset
    # -------------------------------------------------

    def load_sample_dataset(self):

        np.random.seed(42)

        rows = 300

        df = pd.DataFrame({

            "Experience":np.random.randint(0,15,rows),

            "Skills":np.random.randint(5,30,rows),

            "Education":np.random.randint(1,5,rows),

            "Projects":np.random.randint(0,20,rows),

            "Certifications":np.random.randint(0,10,rows)

        })

        df["HiringScore"] = (

            df["Experience"]*5 +

            df["Skills"]*2 +

            df["Education"]*8 +

            df["Projects"]*2 +

            df["Certifications"]*3 +

            np.random.randint(-8,8,rows)

        )

        return df

    # -------------------------------------------------
    # Train Models
    # -------------------------------------------------

    def train_models(self):

        df = self.load_sample_dataset()

        X = df.drop("HiringScore",axis=1)

        y = df["HiringScore"]

        X_train,X_test,y_train,y_test = train_test_split(

            X,

            y,

            test_size=0.2,

            random_state=42

        )

        models = {

            "Linear Regression":LinearRegression(),

            "Random Forest":RandomForestRegressor(

                n_estimators=200,

                random_state=42

            )

        }

        if XGBOOST_AVAILABLE:

            models["XGBoost"] = XGBRegressor(

                n_estimators=200,

                learning_rate=0.05,

                random_state=42

            )

        results = []

        for name,model in models.items():

            model.fit(X_train,y_train)

            pred = model.predict(X_test)

            mae = mean_absolute_error(y_test,pred)

            mse = mean_squared_error(y_test,pred)

            rmse = np.sqrt(mse)

            r2 = r2_score(y_test,pred)

            filename = name.lower().replace(" ","_")+".pkl"

            joblib.dump(

                model,

                os.path.join(

                    self.model_folder,

                    filename

                )

            )

            self.models[name]=model

            results.append({

                "Model":name,

                "MAE":round(mae,2),

                "RMSE":round(rmse,2),

                "R²":round(r2,4)

            })

        return pd.DataFrame(results)

    # -------------------------------------------------
    # Load Models
    # -------------------------------------------------

    def load_models(self):

        for file in os.listdir(self.model_folder):

            if file.endswith(".pkl"):

                model = joblib.load(

                    os.path.join(

                        self.model_folder,

                        file

                    )

                )

                self.models[file]=model

    # -------------------------------------------------
    # Predict Hiring Score
    # -------------------------------------------------

    def predict(

        self,

        experience,

        skills,

        education,

        projects,

        certifications,

        model_name="Random Forest"

    ):

        if not self.models:

            self.load_models()

        if model_name in self.models:

            model = self.models[model_name]

        else:

            model = list(self.models.values())[0]

        X = pd.DataFrame({

            "Experience":[experience],

            "Skills":[skills],

            "Education":[education],

            "Projects":[projects],

            "Certifications":[certifications]

        })

        prediction = model.predict(X)[0]

        prediction = max(0,min(100,prediction))

        return round(prediction,2)

    # -------------------------------------------------
    # Demo Prediction
    # -------------------------------------------------

    def demo_prediction(self):

        if not self.models:

            self.load_models()

        if len(self.models)==0:

            self.train_models()

            self.load_models()

        return self.predict(

            experience=5,

            skills=20,

            education=4,

            projects=8,

            certifications=3

        )