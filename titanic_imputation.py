"""
titanic_imputation.py

Apply simple imputation strategies to the Titanic dataset:
- Fill missing Age values with the median age
- Fill missing Embarked values with the mode (most frequent port)
- Drop the Cabin column entirely

Usage:
    python titanic_imputation.py --input data/train.csv --output data/train_imputed.csv

Defaults:
    input:  data/train.csv
    output: data/train_imputed.csv
"""

import argparse
import pandas as pd

def impute_data(df: pd.DataFrame) -> pd.DataFrame:
    # Work on a copy to avoid chained-assignment warnings
    df = df.copy()
    # Fill missing Age with median
    df['Age'] = df['Age'].fillna(df['Age'].median())
    # Fill missing Embarked with mode
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    # Drop Cabin column entirely
    df = df.drop(columns=['Cabin'])
    return df

def main(input_path: str, output_path: str):
    # Load dataset
    df = pd.read_csv(input_path)
    print("Before imputation:\n", df.isnull().sum())

    # Apply imputation
    df_imputed = impute_data(df)
    print("After imputation:\n", df_imputed.isnull().sum())

    # Save imputed dataset
    df_imputed.to_csv(output_path, index=False)
    print(f"Imputed dataset saved to {output_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Impute missing values in Titanic dataset."
    )
    parser.add_argument(
        '--input',
        type=str,
        default='data/train.csv',
        help='Path to input CSV file'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='data/train_imputed.csv',
        help='Path to save imputed CSV file'
    )
    args = parser.parse_args()
    main(args.input, args.output)
