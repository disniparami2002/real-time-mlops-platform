from fastapi import FastAPI
import joblib
import pandas as pd

# Create FastAPI app
app = FastAPI()

# Load trained model
model = joblib.load('models/churn_model.pkl')

# Home route
@app.get('/')
def home():

    return {
        'message': 'Real-Time Customer Churn Prediction API Running'
    }

# Prediction route
@app.post('/predict')
def predict(data: dict):

    # Convert incoming data to DataFrame
    df = pd.DataFrame([data])

    # Make prediction
    prediction = model.predict(df)[0]

    # Prediction probability
    probability = model.predict_proba(df)[0]

    # Confidence score
    confidence = round(max(probability) * 100, 2)

    # Human-readable output
    if prediction == 1:
        result = "Customer Likely to Churn"

    else:
        result = "Customer Likely to Stay"

    # Return response
    return {

        'prediction': result,

        'prediction_code': int(prediction),

        'confidence': f'{confidence}%'
    }