import pandas as pd
from sklearn.preprocessing import MinMaxScaler

print("Starting enrolment analysis...")

# --------------------------------------------------
# 1. LOAD ALL CSV FILES
# --------------------------------------------------

df1 = pd.read_csv("api_data_aadhar_enrolment_0_500000.csv")
df2 = pd.read_csv("api_data_aadhar_enrolment_500000_1000000.csv")
df3 = pd.read_csv("api_data_aadhar_enrolment_1000000_1006029.csv")

enrol_df = pd.concat([df1, df2, df3], ignore_index=True)

print("Total rows loaded:", enrol_df.shape[0])

# --------------------------------------------------
# 2. DATE CLEANING
# --------------------------------------------------

# Convert DD-MM-YYYY safely
enrol_df["date"] = pd.to_datetime(
    enrol_df["date"],
    dayfirst=True,
    errors="coerce"
)

# Remove invalid dates & missing pincodes
enrol_df = enrol_df.dropna(subset=["date", "pincode"])

# Create Month column
enrol_df["month"] = enrol_df["date"].dt.to_period("M")

# --------------------------------------------------
# 3. AGGREGATE TO PINCODE × MONTH
# --------------------------------------------------

agg_df = enrol_df[
    ["pincode", "month", "age_0_5", "age_5_17", "age_18_greater"]
]

grouped = (
    agg_df
    .groupby(["pincode", "month"], as_index=False)
    .sum()
)

print("Aggregation complete. Rows:", grouped.shape[0])

# --------------------------------------------------
# 4. FEATURE ENGINEERING
# --------------------------------------------------

# Total enrolments
grouped["total_enrolments"] = (
    grouped["age_0_5"]
    + grouped["age_5_17"]
    + grouped["age_18_greater"]
)

# Adult enrolment ratio
grouped["adult_ratio"] = (
    grouped["age_18_greater"] / grouped["total_enrolments"]
)

# Sort for time-based operations
grouped = grouped.sort_values(["pincode", "month"])

# Spike Index (3-month rolling avg)
grouped["rolling_avg"] = (
    grouped.groupby("pincode")["total_enrolments"]
    .rolling(3, min_periods=1)
    .mean()
    .reset_index(level=0, drop=True)
)

grouped["spike_index"] = (
    grouped["total_enrolments"] / grouped["rolling_avg"]
)

# Volatility (std dev across months)
grouped["volatility"] = (
    grouped.groupby("pincode")["total_enrolments"]
    .transform("std")
)

# --------------------------------------------------
# 5. NORMALIZATION
# --------------------------------------------------

scaler = MinMaxScaler()

grouped[
    ["adult_ratio_norm", "spike_norm", "volatility_norm"]
] = scaler.fit_transform(
    grouped[["adult_ratio", "spike_index", "volatility"]]
)

# --------------------------------------------------
# 6. FINAL ENROLMENT RISK SCORE
# --------------------------------------------------

grouped["enrolment_risk_score"] = (
    0.4 * grouped["adult_ratio_norm"]
    + 0.4 * grouped["spike_norm"]
    + 0.2 * grouped["volatility_norm"]
)

# --------------------------------------------------
# 7. SAVE OUTPUT
# --------------------------------------------------

final_cols = [
    "pincode",
    "month",
    "adult_ratio",
    "spike_index",
    "volatility",
    "enrolment_risk_score"
]

grouped[final_cols].to_csv(
    "enrolment_risk_features.csv",
    index=False
)

print("✅ Enrolment risk features saved as enrolment_risk_features.csv")


