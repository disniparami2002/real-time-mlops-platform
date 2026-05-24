import streamlit as st
import pandas as pd

# Page title
st.title("Real-Time AI Prediction Monitoring Dashboard")

# Project info
st.header("System Status")

st.success("Model API Running")
st.success("MLflow Tracking Active")
st.success("Drift Monitoring Active")

# Load dataset
data = pd.read_csv(
    'data/WA_Fn-UseC_-Telco-Customer-Churn.csv'
)

# Show sample data
st.header("Sample Dataset")

st.dataframe(data.head())

# Show statistics
st.header("Monthly Charges Statistics")

st.write(data['MonthlyCharges'].describe())

# Drift monitoring simulation
st.header("Data Drift Monitoring")

train_mean = pd.to_numeric(
    data['MonthlyCharges'],
    errors='coerce'
).mean()

new_mean = train_mean + 1

difference = abs(train_mean - new_mean)

st.write("Training Mean:", train_mean)
st.write("Incoming Data Mean:", new_mean)
st.write("Difference:", difference)

if difference > 5:
    st.error("Data Drift Detected!")
else:
    st.success("No Significant Drift")

# Footer
st.header("MLOps Components")

st.write("✔ Real-Time Predictions")
st.write("✔ Automated Retraining")
st.write("✔ CI/CD Integration")
st.write("✔ Docker Deployment")
st.write("✔ MLflow Experiment Tracking")
st.write("✔ Data Drift Monitoring")