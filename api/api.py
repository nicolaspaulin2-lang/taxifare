"""
FastAPI test to check everything is in order
"""

import os
import pandas as pd
from fastapi import FastAPI
### from taxifare.predict import model

### MODEL_PATH = "models/pipeline_linear.joblib"

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
