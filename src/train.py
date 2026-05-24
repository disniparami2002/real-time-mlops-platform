import pandas as pd
import mlflow
import mlflow.sklearn
import joblib

mlflow.set_tracking_uri("file:./mlruns")

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Set MLflow experiment
mlflow.set_experiment("Customer_Churn_Experiment")

# Start MLflow run
with mlflow.start_run():

    # Load dataset
    df = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

    # Remove unnecessary column
    df.drop('customerID', axis=1, inplace=True)

    # Convert TotalCharges to numeric
    df['TotalCharges'] = pd.to_numeric(
        df['TotalCharges'],
        errors='coerce'
    )

    # Fill missing values
    df['TotalCharges'] = df['TotalCharges'].fillna(
        df['TotalCharges'].median()
    )

    # Encode categorical variables
    for col in df.columns:
        if df[col].dtype == 'object':
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))

    # Features and target
    X = df.drop('Churn', axis=1)
    y = df['Churn']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Model
    model = RandomForestClassifier()

    # Train model
    model.fit(X_train, y_train)

    # Predictions
    predictions = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(y_test, predictions)

    print(f'Accuracy: {accuracy}')

    # Log metric
    mlflow.log_metric("accuracy", accuracy)

    # Log model
    mlflow.sklearn.log_model(
        model,
        "customer_churn_model"
    )

    # Save model locally
    joblib.dump(
        model,
        'models/churn_model.pkl'
    )

    print("Model saved successfully!")