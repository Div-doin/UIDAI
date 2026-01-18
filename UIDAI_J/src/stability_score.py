import pandas as pd

demo = pd.read_csv("../outputs/J_demographic_features.csv")
bio = pd.read_csv("../outputs/J_biometric_features.csv")

print(demo.head())
print(bio.head())

merged = pd.merge(demo, bio, on=['pincode','month'], how='inner')

merged['aadhaar_stability_score'] = 1 - (merged['drift_norm'] + merged['bio_norm']) / 2

merged.to_csv("../outputs/J_aadhaar_stability_score.csv", index=False)

print("Aadhaar Stability Score file saved successfully.")
