import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
data = pd.read_csv("../Data/loan_data.csv")

# Remove Loan_ID
data.drop("Loan_ID", axis=1, inplace=True)

# Fill missing values
data = data.ffill()

# Categorical columns
categorical_columns = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "Property_Area",
    "Loan_Status"
]

# Store Label Encoders
label_encoders = {}

for column in categorical_columns:
    encoder = LabelEncoder()
    data[column] = encoder.fit_transform(data[column])
    label_encoders[column] = encoder

# Features and Target
X = data.drop("Loan_Status", axis=1)
y = data["Loan_Status"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Train Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save model
joblib.dump(model, "loan_model.pkl")

# Save encoders
joblib.dump(label_encoders, "encoders.pkl")

print("Model and encoders saved successfully!")