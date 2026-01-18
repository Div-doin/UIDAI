import pandas as pd
import glob

files = glob.glob("../../Dataset/api_data_aadhar_biometric/*.csv")
print("Files found:", files)

df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

print(df.head())
print(df.columns)

df['date'] = pd.to_datetime(df['date'], dayfirst=True)
df['month'] = df['date'].dt.to_period('M')

monthly = df.groupby(['pincode','month'])[['bio_age_5_17','bio_age_17_']].sum().reset_index()

monthly['biometric_instability'] = monthly['bio_age_5_17'] + monthly['bio_age_17_']

den = monthly['biometric_instability'].max() - monthly['biometric_instability'].min()
monthly['bio_norm'] = monthly['biometric_instability'] / den if den != 0 else 0

monthly.to_csv("../outputs/J_biometric_features.csv", index=False)
print("Biometric feature file saved successfully.")
