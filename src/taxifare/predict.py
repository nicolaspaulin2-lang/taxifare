import joblib
import pandas as pd

def load_model(model_path):
    """Load a model from a given path."""

    return joblib.load(model_path)

def predict(model, X):
    """Make predictions using the provided model and input data."""
    return model.predict(X)


if __name__ == "__main__":
    X_dummy = pd.DataFrame([{
          'pickup_datetime': '2013-07-06 17:18:00 UTC',
          'pickup_longitude': -73.950655,
          'pickup_latitude': 40.783282,
          'dropoff_longitude': -73.984365,
          'dropoff_latitude': 40.769802,
          'passenger_count': 1
    }])

    model = load_model("models/linreg_pipeline.joblib")

    print(predict(model, X_dummy))
