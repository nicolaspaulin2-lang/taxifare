"""
FastAPI test to check everything is in order
"""

import os
import pandas as pd
from fastapi import FastAPI
from taxifare.predict import load_model, predict


### from taxifare.predict import model

MODEL_PATH = "models/linreg_pipeline.joblib"

# FastApi Instance
app = FastAPI()

# Root Endpoint
@app.get("/")
def root():
    """Root endpoint returning a greeting."""
    return {"greeting": "hello"}

# Dummy endpoint
@app.get("/dummy")
def dummy(number: int):
    """Dummy endpoint that returns the square of the input number."""
    return {"result": number ** 2}

# Prediction endpoint
@app.get('/predict')
def prediction(pickup_datetime:str,
            pickup_longitude:float,
            pickup_latitude:float,
            dropoff_longitude:float,
            dropoff_latitude:float,
            passenger_count:float
            ):
    X_pred = pd.DataFrame([{
        'pickup_datetime': pickup_datetime,
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
        }])

    model = load_model(MODEL_PATH)
    prediction = predict(model, X_pred)
    return {'fare': prediction[0]}
