import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

class MLPredictor:
    def __init__(self):
        self.model = LinearRegression()
        self.scaler = StandardScaler()

    def preprocess_data(self, data):
        """Preprocess the input data."""
        # Handle missing values
        data = data.dropna()
        
        # Assuming all columns except the last one are features
        X = data.iloc[:, :-1]
        y = data.iloc[:, -1]
        
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        return X_scaled, y

    def train(self, X, y):
        """Train the model on the given data."""
        self.model.fit(X, y)

    def predict(self, X):
        """Make predictions using the trained model."""
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)

    def evaluate(self, X, y):
        """Evaluate the model performance."""
        predictions = self.predict(X)
        mse = mean_squared_error(y, predictions)
        r2 = r2_score(y, predictions)
        return mse, r2

    def save_model(self, filename):
        """Save the trained model to a file."""
        joblib.dump((self.model, self.scaler), filename)

    def load_model(self, filename):
        """Load a trained model from a file."""
        self.model, self.scaler = joblib.load(filename)

def load_data(filename):
    """Load data from a CSV file."""
    return pd.read_csv(filename)
