import pandas as pd

# === Step 1: Load the cleaned dataset ===
file_path = r"C:\Users\ri\OneDrive\ai project\data cleaning\titanic\data\train_cleaned.csv"
df = pd.read_csv(file_path)

# === Step 2: Remove Name and Ticket columns ===
df = df.drop(['Name', 'Ticket'], axis=1)

# === Step 3: Count unique values and frequencies for specified columns ===
print("🟩 Unique Value Counts and Frequencies:")

# Sex
sex_counts = df['Sex'].value_counts().to_dict()
sex_output = ", ".join([f"{k} = {v}" for k, v in sex_counts.items()])
print(f"Sex: {sex_output}")

# SibSp
sibsp_counts = df['SibSp'].value_counts().sort_index().to_dict()
sibsp_output = ", ".join([f"{k} = {v}" for k, v in sibsp_counts.items()])
print(f"SibSp: {sibsp_output}")

# Parch
parch_counts = df['Parch'].value_counts().sort_index().to_dict()
parch_output = ", ".join([f"{k} = {v}" for k, v in parch_counts.items()])
print(f"Parch: {parch_output}")

# Embarked
embarked_counts = df['Embarked'].value_counts().to_dict()
embarked_output = ", ".join([f"{k} = {v}" for k, v in embarked_counts.items()])
print(f"Embarked: {embarked_output}")

# Deck
deck_counts = df['Deck'].value_counts().to_dict()
deck_output = ", ".join([f"{k} = {v}" for k, v in deck_counts.items()])
print(f"Deck: {deck_output}")

# === Step 4: Verify the updated dataset ===
print("\n🟩 Dataset Shape After Removing Columns:")
print(df.shape, "\n")

print("🟩 Column Names After Removing Columns:")
print(df.columns.tolist(), "\n")

print("🟩 Missing Values After Processing:")
print(df.isnull().sum(), "\n")

# === Step 5: Save the processed dataset ===
output_path = r"C:\Users\ri\OneDrive\ai project\data cleaning\titanic\data\train_processed.csv"
df.to_csv(output_path, index=False)
print(f"🟩 Processed dataset saved to: {output_path}")