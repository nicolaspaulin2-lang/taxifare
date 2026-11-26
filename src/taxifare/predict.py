import joblib

def load_model(model_path):
    """Load a model from a given path."""

    return joblib.load(model_path)

def predict(model, X):
    """Make predictions using the provided model and input data."""
    return model.predict(X)

