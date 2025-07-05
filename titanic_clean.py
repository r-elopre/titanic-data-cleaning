import pandas as pd

df = pd.read_csv(r"C:\Users\ri\OneDrive\ai project\data cleaning\titanic\train.csv")

print("Shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nMissing values:\n", df.isnull().sum())
print("\nInfo:")
df.info()
