"""
=========================================================
Resume Intelligence AI
Deep Learning Prediction Engine
Version : 8.0
Author : Naveen Kumar
=========================================================
"""

import os
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

import joblib


class DeepLearningModel:

    def __init__(self):

        self.model_path = "models/deep_learning_model.keras"

        self.scaler_path = "models/scaler.pkl"

        self.model = None

        self.scaler = MinMaxScaler()

    # -------------------------------------------------------
    # Generate Training Dataset
    # -------------------------------------------------------

    def load_dataset(self):

        np.random.seed(42)

        rows = 1000

        df = pd.DataFrame({

            "Experience":np.random.randint(0,15,rows),

            "Skills":np.random.randint(5,35,rows),

            "Projects":np.random.randint(0,15,rows),

            "Education":np.random.randint(1,5,rows),

            "Certifications":np.random.randint(0,10,rows)

        })

        df["HiringScore"]=(

            df["Experience"]*5+

            df["Skills"]*2+

            df["Projects"]*2+

            df["Education"]*10+

            df["Certifications"]*3+

            np.random.randint(-10,10,rows)

        )

        df["HiringScore"]=df["HiringScore"].clip(0,100)

        return df

    # -------------------------------------------------------
    # Build Neural Network
    # -------------------------------------------------------

    def build_model(self):

        model=Sequential()

        model.add(

            Dense(

                64,

                activation="relu",

                input_shape=(5,)

            )

        )

        model.add(

            Dropout(0.30)

        )

        model.add(

            Dense(

                32,

                activation="relu"

            )

        )

        model.add(

            Dropout(0.20)

        )

        model.add(

            Dense(

                16,

                activation="relu"

            )

        )

        model.add(

            Dense(

                1,

                activation="linear"

            )

        )

        model.compile(

            optimizer="adam",

            loss="mse",

            metrics=["mae"]

        )

        return model

    # -------------------------------------------------------
    # Train Model
    # -------------------------------------------------------

    def train(self):

        df=self.load_dataset()

        X=df.drop("HiringScore",axis=1)

        y=df["HiringScore"]

        X=self.scaler.fit_transform(X)

        joblib.dump(

            self.scaler,

            self.scaler_path

        )

        X_train,X_test,y_train,y_test=train_test_split(

            X,

            y,

            test_size=0.20,

            random_state=42

        )

        self.model=self.build_model()

        early=EarlyStopping(

            monitor="val_loss",

            patience=10,

            restore_best_weights=True

        )

        history=self.model.fit(

            X_train,

            y_train,

            validation_split=0.20,

            epochs=100,

            batch_size=32,

            callbacks=[early],

            verbose=1

        )

        self.model.save(

            self.model_path

        )

        return history
    # -------------------------------------------------------
    # Load Model
    # -------------------------------------------------------

    def load(self):

        if os.path.exists(self.model_path):

            self.model = load_model(self.model_path)

        if os.path.exists(self.scaler_path):

            self.scaler = joblib.load(self.scaler_path)

    # -------------------------------------------------------
    # Evaluate Model
    # -------------------------------------------------------

    def evaluate(self):

        df = self.load_dataset()

        X = df.drop("HiringScore", axis=1)

        y = df["HiringScore"]

        X = self.scaler.fit_transform(X)

        loss, mae = self.model.evaluate(

            X,

            y,

            verbose=0

        )

        return {

            "Loss": round(loss, 3),

            "MAE": round(mae, 3)

        }

    # -------------------------------------------------------
    # Predict Hiring Score
    # -------------------------------------------------------

    def predict(

        self,

        experience,

        skills,

        projects,

        education,

        certifications

    ):

        if self.model is None:

            self.load()

        sample = pd.DataFrame({

            "Experience":[experience],

            "Skills":[skills],

            "Projects":[projects],

            "Education":[education],

            "Certifications":[certifications]

        })

        sample = self.scaler.transform(sample)

        prediction = self.model.predict(

            sample,

            verbose=0

        )[0][0]

        prediction = max(0, min(100, prediction))

        return round(float(prediction),2)

    # -------------------------------------------------------
    # Confidence Score
    # -------------------------------------------------------

    def confidence(self, prediction):

        if prediction >= 85:

            return "Very High"

        elif prediction >= 70:

            return "High"

        elif prediction >= 50:

            return "Medium"

        else:

            return "Low"

    # -------------------------------------------------------
    # AI Recommendation
    # -------------------------------------------------------

    def recommendation(self, prediction):

        if prediction >= 85:

            return """
Excellent Resume.

Very strong hiring probability.

Keep applying to premium companies.
"""

        elif prediction >= 70:

            return """
Strong Resume.

Improve certifications and projects
for better opportunities.
"""

        elif prediction >= 50:

            return """
Average Resume.

Add more technical skills.

Complete industry certifications.

Improve project portfolio.
"""

        else:

            return """
Resume needs significant improvement.

Focus on:

• Skills

• Projects

• Certifications

• Resume Formatting

• ATS Optimization
"""

    # -------------------------------------------------------
    # Demo Prediction
    # -------------------------------------------------------

    def demo_prediction(self):

        if not os.path.exists(self.model_path):

            self.train()

        self.load()

        prediction = self.predict(

            experience=5,

            skills=18,

            projects=5,

            education=4,

            certifications=2

        )

        return prediction

    # -------------------------------------------------------
    # Complete Report
    # -------------------------------------------------------

    def full_report(

        self,

        experience,

        skills,

        projects,

        education,

        certifications

    ):

        score = self.predict(

            experience,

            skills,

            projects,

            education,

            certifications

        )

        report = {

            "Hiring Score": score,

            "Confidence": self.confidence(score),

            "Recommendation": self.recommendation(score)

        }

        return report