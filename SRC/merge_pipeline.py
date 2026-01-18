import pandas as pd

print("🔹 Merging Aadhaar intelligence from all pipelines...")


enrol = pd.read_csv("Dataset/enrolment_risk_features.csv")

demo = pd.read_csv("Dataset/J_demographic_instability.csv")


demo.rename(columns={"identity_drift": "demographic_instability_score"}, inplace=True)


bio = pd.read_csv("Dataset/biometric_anomalies.csv")


master = enrol.merge(demo, on=["pincode", "month"], how="outer")
master = master.merge(bio, on=["pincode", "month"], how="outer")

master = master.fillna(0)


master["stability_score"] = 1 - (
    master["enrolment_risk_score"]
  + master["demographic_instability_score"]
  + master["biometric_risk"]
)


master.to_csv("Dataset/master_aadhaar_intelligence.csv", index=False)

print("✅ Master Intelligence file created → Dataset/master_aadhaar_intelligence.csv")
