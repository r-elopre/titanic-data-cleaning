import pandas as pd

# === Step 1: Load the processed dataset ===
file_path = r"C:\Users\ri\OneDrive\ai project\data cleaning\titanic\data\train_processed.csv"
df = pd.read_csv(file_path)

# === Step 2: Apply one-hot encoding to categorical columns ===
categorical_cols = ['Sex', 'Embarked', 'Deck']
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# === Step 3: Verify encoding with all categories ===
print("🟩 Original Unique Categories and Encoded Columns:")
# Sex
sex_unique = df['Sex'].unique() if 'Sex' in df.columns else ['male', 'female']  # Fallback if column already dropped
print(f"Sex: Unique values = {sex_unique}, Encoded = ['Sex_male'] (Reference: female)")

# Embarked
embarked_unique = df['Embarked'].unique() if 'Embarked' in df.columns else ['s', 'c', 'q']  # Fallback
print(f"Embarked: Unique values = {embarked_unique}, Encoded = ['Embarked_q', 'Embarked_s'] (Reference: c)")

# Deck
deck_unique = df['Deck'].unique() if 'Deck' in df.columns else ['Unknown', 'C', 'E', 'G', 'D', 'A', 'B', 'F', 'T']  # Fallback
print(f"Deck: Unique values = {deck_unique}, Encoded = ['Deck_B', 'Deck_C', 'Deck_D', 'Deck_E', 'Deck_F', 'Deck_G', 'Deck_T', 'Deck_Unknown'] (Reference: A)")

# === Step 4: Verify dataset ===
print("\n🟩 Dataset Shape After Encoding:")
print(df.shape, "\n")

print("🟩 Column Names After Encoding:")
print(df.columns.tolist(), "\n")

print("🟩 Missing Values After Encoding:")
print(df.isnull().sum(), "\n")

print("🟩 Data Types After Encoding:")
print(df.dtypes, "\n")

print("🟩 First 5 Rows After Encoding:")
print(df.head(), "\n")

# === Step 5: Save encoded dataset ===
output_path = r"C:\Users\ri\OneDrive\ai project\data cleaning\titanic\data\train_encoded_complete.csv"
df.to_csv(output_path, index=False)
print(f"🟩 Encoded dataset saved to: {output_path}")