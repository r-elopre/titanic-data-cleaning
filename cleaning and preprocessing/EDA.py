import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Set seaborn style for better visuals
sns.set_style("whitegrid")

# === Step 1: Load the cleaned dataset ===
file_path = r"C:\Users\ri\OneDrive\ai project\data cleaning\titanic\data\train_cleaned.csv"
df = pd.read_csv(file_path)

# === Step 2: Verify data cleanliness ===
print("🟩 Missing Values Check:")
print(df.isnull().sum(), "\n")

# Validate categorical columns
print("🟩 Unique Values in Categorical Columns:")
print("Sex:", df['Sex'].unique())
print("Embarked:", df['Embarked'].unique())
print("Deck:", df['Deck'].unique(), "\n")

# Check for invalid numeric values
print("🟩 Numeric Columns Validation (Negative Values):")
numeric_cols = ['Age', 'Fare', 'SibSp', 'Parch']
for col in numeric_cols:
    negatives = df[df[col] < 0][col].count()
    print(f"{col}: {negatives} negative values")
print("\n")

# === Step 3: Summary Statistics ===
print("🟩 Summary Statistics for Numeric Columns:")
print(df[numeric_cols].describe(), "\n")

# === Step 4: Visualizations ===
output_dir = r"C:\Users\ri\OneDrive\ai project\data cleaning\titanic\data\plots"
os.makedirs(output_dir, exist_ok=True)

# Histogram for Age
plt.figure(figsize=(8, 6))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.savefig(os.path.join(output_dir, 'age_distribution.png'))
plt.close()

# Histogram for Fare
plt.figure(figsize=(8, 6))
sns.histplot(df['Fare'], bins=30, kde=True)
plt.title('Fare Distribution')
plt.xlabel('Fare')
plt.ylabel('Count')
plt.savefig(os.path.join(output_dir, 'fare_distribution.png'))
plt.close()

# Bar plot for Survived
plt.figure(figsize=(8, 6))
sns.countplot(x='Survived', data=df)
plt.title('Survival Count')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.savefig(os.path.join(output_dir, 'survived_count.png'))
plt.close()

# Bar plot for Pclass
plt.figure(figsize=(8, 6))
sns.countplot(x='Pclass', data=df)
plt.title('Passenger Class Distribution')
plt.xlabel('Pclass')
plt.ylabel('Count')
plt.savefig(os.path.join(output_dir, 'pclass_distribution.png'))
plt.close()

# Bar plot for Sex
plt.figure(figsize=(8, 6))
sns.countplot(x='Sex', data=df)
plt.title('Sex Distribution')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.savefig(os.path.join(output_dir, 'sex_distribution.png'))
plt.close()

# Bar plot for Embarked
plt.figure(figsize=(8, 6))
sns.countplot(x='Embarked', data=df)
plt.title('Embarked Distribution')
plt.xlabel('Embarked')
plt.ylabel('Count')
plt.savefig(os.path.join(output_dir, 'embarked_distribution.png'))
plt.close()

# Bar plot for Deck
plt.figure(figsize=(8, 6))
sns.countplot(x='Deck', data=df, order=df['Deck'].value_counts().index)
plt.title('Deck Distribution')
plt.xlabel('Deck')
plt.ylabel('Count')
plt.savefig(os.path.join(output_dir, 'deck_distribution.png'))
plt.close()

# Correlation heatmap for numeric columns
plt.figure(figsize=(8, 6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap of Numeric Columns')
plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'))
plt.close()

# Survival rate by Pclass
plt.figure(figsize=(8, 6))
sns.barplot(x='Pclass', y='Survived', data=df, errorbar=None)
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Pclass')
plt.ylabel('Survival Rate')
plt.savefig(os.path.join(output_dir, 'survival_by_pclass.png'))
plt.close()

# Survival rate by Sex
plt.figure(figsize=(8, 6))
sns.barplot(x='Sex', y='Survived', data=df, errorbar=None)
plt.title('Survival Rate by Sex')
plt.xlabel('Sex')
plt.ylabel('Survival Rate')
plt.savefig(os.path.join(output_dir, 'survival_by_sex.png'))
plt.close()

# === Step 5: Survival Rate Analysis ===
print("🟩 Survival Rate by Key Variables:")
print("By Pclass:")
print(df.groupby('Pclass')['Survived'].mean(), "\n")
print("By Sex:")
print(df.groupby('Sex')['Survived'].mean(), "\n")
print("By Embarked:")
print(df.groupby('Embarked')['Survived'].mean(), "\n")

print(f"🟩 Plots saved to: {output_dir}")