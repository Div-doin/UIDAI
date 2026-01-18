import pandas as pd
from sklearn.preprocessing import MinMaxScaler

print("🔹 Loading master Aadhaar intelligence...")

df = pd.read_csv("Dataset/master_aadhaar_intelligence.csv")

# RL state features
state_cols = [
    "stability_score",
    "enrolment_risk_score",
    "demographic_instability_score",
    "biometric_risk"
]

scaler = MinMaxScaler()
df[state_cols] = scaler.fit_transform(df[state_cols])

print("State features normalized.")

# Audit priority (lower stability = higher priority)
df["audit_priority"] = df["stability_score"].rank(ascending=True)

df = df.sort_values("audit_priority")

df.to_csv("Dataset/rl_audit_recommendations.csv", index=False)

print("✅ RL audit recommendations saved → Dataset/rl_audit_recommendations.csv")
