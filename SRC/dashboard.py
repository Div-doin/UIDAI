import pandas as pd
import matplotlib.pyplot as plt

print("🔹 Loading RL audit recommendations...")

df = pd.read_csv("Dataset/rl_audit_recommendations.csv")

top = df.head(30)

plt.figure(figsize=(12,6))
plt.bar(top["pincode"].astype(str), top["stability_score"])
plt.title("Top 30 High-Risk PIN Codes (Lower Stability)")
plt.xlabel("Pincode")
plt.ylabel("Stability Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Dataset/high_risk_heatmap.png")
plt.close()

top.to_csv("Dataset/top_30_high_risk_pins.csv", index=False)

print("✅ Dashboard visual saved → Dataset/high_risk_heatmap.png")
