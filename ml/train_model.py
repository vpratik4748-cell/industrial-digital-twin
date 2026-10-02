import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

import joblib


# ==========================================
# 1. CREATE TRAINING DATA
# ==========================================

np.random.seed(42)


normal_samples = 500
anomaly_samples = 500


# ------------------------------------------
# NORMAL OPERATING DATA
# ------------------------------------------

normal_flow = np.random.normal(
    75,
    5,
    normal_samples
)

normal_pressure = np.random.normal(
    4.2,
    0.4,
    normal_samples
)

normal_temperature = np.random.normal(
    55,
    5,
    normal_samples
)

normal_current = np.random.normal(
    8,
    1,
    normal_samples
)

normal_tank = np.random.normal(
    65,
    10,
    normal_samples
)


normal_data = np.column_stack(
    (
        normal_flow,
        normal_pressure,
        normal_temperature,
        normal_current,
        normal_tank
    )
)


# ------------------------------------------
# ABNORMAL OPERATING DATA
# ------------------------------------------

anomaly_flow = np.random.normal(
    35,
    15,
    anomaly_samples
)

anomaly_pressure = np.random.normal(
    1.5,
    0.5,
    anomaly_samples
)

anomaly_temperature = np.random.normal(
    90,
    10,
    anomaly_samples
)

anomaly_current = np.random.normal(
    14,
    2,
    anomaly_samples
)

anomaly_tank = np.random.normal(
    15,
    8,
    anomaly_samples
)


anomaly_data = np.column_stack(
    (
        anomaly_flow,
        anomaly_pressure,
        anomaly_temperature,
        anomaly_current,
        anomaly_tank
    )
)


# ==========================================
# 2. COMBINE DATA
# ==========================================

X = np.vstack(
    (
        normal_data,
        anomaly_data
    )
)


# Normal = 0
# Anomaly = 1

y = np.concatenate(
    (
        np.zeros(normal_samples),
        np.ones(anomaly_samples)
    )
)


# ==========================================
# 3. SPLIT DATA
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42,

    stratify=y
)


# ==========================================
# 4. CREATE ML MODEL
# ==========================================

model = DecisionTreeClassifier(

    max_depth=4,

    random_state=42

)


# ==========================================
# 5. TRAIN MODEL
# ==========================================

print()
print("Training Industrial Pump ML Model...")

model.fit(
    X_train,
    y_train
)


# ==========================================
# 6. TEST MODEL
# ==========================================

predictions = model.predict(
    X_test
)


accuracy = accuracy_score(
    y_test,
    predictions
)


print()
print("Model Accuracy:")
print(
    f"{accuracy * 100:.2f}%"
)


print()
print("Classification Report:")
print(
    classification_report(
        y_test,
        predictions
    )
)


# ==========================================
# 7. SAVE MODEL
# ==========================================

joblib.dump(
    model,
    "ml/pump_anomaly_model.pkl"
)


print()
print("✓ Model saved:")
print(
    "ml/pump_anomaly_model.pkl"
)

print()
print("Training complete.")