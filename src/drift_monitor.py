import pandas as pd

# Load training dataset
train_data = pd.read_csv(
    'data/WA_Fn-UseC_-Telco-Customer-Churn.csv'
)

# Simulated incoming production data
new_data = pd.read_csv(
    'data/WA_Fn-UseC_-Telco-Customer-Churn.csv'
)

# Convert MonthlyCharges to numeric if needed
train_data['MonthlyCharges'] = pd.to_numeric(
    train_data['MonthlyCharges'],
    errors='coerce'
)

new_data['MonthlyCharges'] = pd.to_numeric(
    new_data['MonthlyCharges'],
    errors='coerce'
)

# Calculate averages
train_mean = train_data['MonthlyCharges'].mean()
new_mean = new_data['MonthlyCharges'].mean()

# Print statistics
print("Training Data Mean:", train_mean)
print("New Incoming Data Mean:", new_mean)

# Drift detection logic
difference = abs(train_mean - new_mean)

print("Difference:", difference)

# Decision
if difference > 5:
    print("⚠️ Data Drift Detected!")
else:
    print("✅ No Significant Drift")