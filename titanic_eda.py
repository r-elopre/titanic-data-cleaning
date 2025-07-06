import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

# 1. Load & Inspect
df = pd.read_csv("data/train.csv")
print("Shape:", df.shape)
print(df.info())

# 2. Summary Statistics
print(df.describe())
print(df["Sex"].value_counts(dropna=False))

# 3. Missing-Value Overview
print(df.isnull().sum())
msno.matrix(df)
plt.show()

# 4. Distribution Plots
df["Age"].hist(bins=30)
plt.show()
sns.boxplot(x="Pclass", y="Fare", data=df)
plt.show()

# 5. Correlations / Cross-tabs
print(pd.crosstab(df["Sex"], df["Survived"], normalize="index"))
sns.heatmap(df.corr(), annot=True)
plt.show()
