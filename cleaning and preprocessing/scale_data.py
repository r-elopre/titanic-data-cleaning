import pandas as pd
from sklearn.preprocessing import StandardScaler

# === Step 1: Load the encoded dataset ===
file_path = r"C:\Users\ri\OneDrive\ai project\data cleaning\titanic\data\train_encoded_complete.csv"
df = pd.read_csv(file_path)

# === Step 2: Identify numeric columns to scale ===
numeric_cols = ['Age', 'Fare', 'SibSp', 'Parch']

# === Step 3: Apply Standard Scaling ===
scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# === Step 4: Verify scaling ===
print("🟩 Summary Statistics After Scaling:")
print(df[numeric_cols].describe(), "\n")

print("🟩 Dataset Shape After Scaling:")
print(df.shape, "\n")

print("🟩 Column Names After Scaling:")
print(df.columns.tolist(), "\n")

print("🟩 Missing Values After Scaling:")
print(df.isnull().sum(), "\n")

print("🟩 Data Types After Scaling:")
print(df.dtypes, "\n")

print("🟩 First 5 Rows After Scaling:")
print(df.head(), "\n")

# === Step 5: Save scaled dataset ===
output_path = r"C:\Users\ri\OneDrive\ai project\data cleaning\titanic\data\train_scaled.csv"
df.to_csv(output_path, index=False)
print(f"🟩 Scaled dataset saved to: {output_path}")