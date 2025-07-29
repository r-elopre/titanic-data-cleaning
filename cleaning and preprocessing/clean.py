import pandas as pd

# === Step 1: Load the dataset ===
file_path = r"C:\Users\ri\OneDrive\ai project\data cleaning\titanic\data\train.csv"
df = pd.read_csv(file_path)

# === Step 2: Handle missing values ===
# Impute Age with median grouped by Sex and Pclass
df['Age'] = df.groupby(['Sex', 'Pclass'])['Age'].transform(lambda x: x.fillna(x.median()))

# Impute Embarked with mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Extract Deck from Cabin and impute missing as 'Unknown'
df['Deck'] = df['Cabin'].str[0].fillna('Unknown')
df = df.drop('Cabin', axis=1)

# === Step 3: Fix inconsistencies ===
# Standardize text columns to lowercase
df['Sex'] = df['Sex'].str.lower()
df['Embarked'] = df['Embarked'].str.lower()

# Validate categorical columns
valid_sex = ['male', 'female']
valid_embarked = ['c', 'q', 's']
df['Sex'] = df['Sex'].where(df['Sex'].isin(valid_sex), 'unknown')
df['Embarked'] = df['Embarked'].where(df['Embarked'].isin(valid_embarked), df['Embarked'].mode()[0])

# Check for invalid numeric values
# Ensure Age, Fare, SibSp, Parch are non-negative
df['Age'] = df['Age'].clip(lower=0)
df['Fare'] = df['Fare'].clip(lower=0)
df['SibSp'] = df['SibSp'].clip(lower=0)
df['Parch'] = df['Parch'].clip(lower=0)

# Handle extreme Fare outliers (cap at 99th percentile)
fare_cap = df['Fare'].quantile(0.99)
df['Fare'] = df['Fare'].clip(upper=fare_cap)

# === Step 4: Verify cleaning ===
print("🟩 Missing Values After Cleaning:")
print(df.isnull().sum(), "\n")

print("🟩 Unique Values in Categorical Columns:")
print("Sex:", df['Sex'].unique())
print("Embarked:", df['Embarked'].unique())
print("Deck:", df['Deck'].unique(), "\n")

print("🟩 Summary Statistics for Numeric Columns:")
print(df[['Age', 'Fare', 'SibSp', 'Parch']].describe(), "\n")

print("🟩 First 5 Rows After Cleaning:")
print(df.head(), "\n")

# === Step 5: Save cleaned dataset ===
output_path = r"C:\Users\ri\OneDrive\ai project\data cleaning\titanic\data\train_cleaned.csv"
df.to_csv(output_path, index=False)
print(f"🟩 Cleaned dataset saved to: {output_path}")