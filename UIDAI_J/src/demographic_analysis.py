import pandas as pd
import glob

files = glob.glob("../../Dataset/api_data_aadhar_demographic/*.csv")
print("Files found:", files)

df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

df['date'] = pd.to_datetime(df['date'], dayfirst=True)
df['month'] = df['date'].dt.to_period('M')
monthly = df.groupby(['pincode','month'])[['demo_age_5_17','demo_age_17_']].sum().reset_index()
print(monthly.head())
monthly['identity_drift'] = monthly['demo_age_5_17'] + monthly['demo_age_17_']
monthly['drift_norm'] = (monthly['identity_drift'] - monthly['identity_drift'].min()) / \
                        (monthly['identity_drift'].max() - monthly['identity_drift'].min())
monthly.to_csv("../outputs/J_demographic_features.csv", index=False)
print("Saved demographic feature file successfully.")
