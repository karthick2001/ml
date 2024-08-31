# src/inference.py

import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
from sklearn.preprocessing import StandardScaler

# Initialize the Flask application
app = Flask(__name__)

# Load the trained model and the scaler used during training
model = joblib.load('model.pkl')
scaler = StandardScaler()

@app.route('/predict', methods=['POST'])
def predict():
    """
    API endpoint that receives JSON data and returns model predictions.
    
    Expected input JSON format:
    {
        "data": [
            [5.1, 3.5, 1.4, 0.2],
            [6.2, 3.4, 5.4, 2.3]
        ]
    }
    
    Returns JSON:
    {
        "predictions": [0, 2]
    }
    """
    try:
        # Get the input data from the request
        data = request.json['data']
        data = np.array(data)

        # Assuming the model was trained with scaled features
        data_scaled = scaler.fit_transform(data)

        # Make predictions
        predictions = model.predict(data_scaled)
        predictions = predictions.tolist()

        # Map the numerical labels back to the species names if needed
        species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
        species_predictions = [species_map[pred] for pred in predictions]

        # Return the predictions as a JSON response
        return jsonify({'predictions': species_predictions})

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/health', methods=['GET'])
def health_check():
    """
    Simple health check endpoint.
    """
    return jsonify({'status': 'up'})

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
