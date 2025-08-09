# Titanic Dataset Preprocessing Pipeline
<p align="center">
  <a href="https://youtu.be/QRCH1OExo5c">
    <img src="https://img.youtube.com/vi/QRCH1OExo5c/maxresdefault.jpg" alt="Titanic Dataset Preprocessing Pipeline Video">
  </a>
  <br/>
  <em>Click the thumbnail to watch on YouTube</em>
</p>

## Overview
This project provides a comprehensive pipeline for cleaning, exploring, and preprocessing the Titanic dataset to prepare it for machine learning tasks. The pipeline consists of six Python scripts that handle data inspection, cleaning, exploratory data analysis (EDA), processing, encoding, and scaling. Each script performs specific tasks to transform the raw dataset into a clean, machine-learning-ready format.

The Titanic dataset contains information about passengers aboard the Titanic, including features like age, sex, passenger class, and survival status. The goal of this pipeline is to clean and preprocess this data to ensure it is consistent, complete, and suitable for predictive modeling.

## Dataset
The dataset used is the Titanic dataset (`train.csv`), typically sourced from Kaggle. It contains 891 rows and 12 columns:
- **PassengerId**: Unique identifier for each passenger
- **Survived**: Survival status (0 = No, 1 = Yes)
- **Pclass**: Passenger class (1 = 1st, 2 = 2nd, 3 = 3rd)
- **Name**: Passenger's name
- **Sex**: Gender (male, female)
- **Age**: Age in years
- **SibSp**: Number of siblings/spouses aboard
- **Parch**: Number of parents/children aboard
- **Ticket**: Ticket number
- **Fare**: Ticket fare
- **Cabin**: Cabin number
- **Embarked**: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)

## Prerequisites
To run the scripts, you need:
- Python 3.6 or higher
- A virtual environment (recommended)
- Required Python libraries:
  ```bash
  pip install pandas seaborn matplotlib scikit-learn
  ```
- The Titanic dataset (`train.csv`) placed in the directory:
  ```
  C:\Users\ri\OneDrive\ai project\data cleaning\titanic\data\
  ```

## Directory Structure
The project is organized as follows:
```
titanic/
├── data/
│   ├── train.csv               # Raw dataset
│   ├── train_cleaned.csv       # Output from clean.py
│   ├── train_processed.csv     # Output from process_data.py
│   ├── train_encoded_complete.csv # Output from encode_data.py
│   ├── train_scaled.csv        # Output from scale_data.py
│   ├── plots/                  # Directory for EDA visualizations
├── cleaning and preprocessing/
│   ├── diagnose.py             # Initial dataset inspection
│   ├── clean.py               # Data cleaning
│   ├── EDA.py                 # Exploratory data analysis
│   ├── process_data.py        # Remove unnecessary columns and count frequencies
│   ├── encode_data.py         # Categorical encoding
│   ├── scale_data.py          # Numeric feature scaling
├── README.md                  # This file
```

## Scripts and Their Functionality

### 1. diagnose.py
**Purpose**: Inspect the raw dataset to understand its structure and identify issues.
- **Actions**:
  - Loads `train.csv`.
  - Displays dataset shape, column names, missing values, data types, and the first 5 rows.
- **Output**:
  - Console output summarizing dataset properties.
  - Key findings: 177 missing `Age` values, 687 missing `Cabin` values, 2 missing `Embarked` values.

### 2. clean.py
**Purpose**: Clean the dataset by handling missing values, standardizing data, and removing inconsistencies.
- **Actions**:
  - Imputes missing `Age` values with the median grouped by `Sex` and `Pclass`.
  - Imputes missing `Embarked` values with the mode.
  - Extracts `Deck` from `Cabin` (first letter) and imputes missing as 'Unknown'; drops `Cabin`.
  - Converts `Sex` and `Embarked` to lowercase.
  - Validates categorical columns (`Sex`: male/female, `Embarked`: c/q/s).
  - Clips negative values in `Age`, `Fare`, `SibSp`, `Parch` to 0.
  - Caps `Fare` outliers at the 99th percentile.
- **Output**:
  - Saves cleaned dataset to `train_cleaned.csv`.
  - Console output showing no missing values, unique categorical values, numeric statistics, and the first 5 rows.

### 3. EDA.py
**Purpose**: Perform exploratory data analysis to understand data distributions and relationships.
- **Actions**:
  - Loads `train_cleaned.csv`.
  - Verifies no missing values and validates categorical and numeric columns.
  - Generates visualizations saved to `data/plots/`:
    - Histograms: `Age`, `Fare`
    - Bar plots: `Survived`, `Pclass`, `Sex`, `Embarked`, `Deck`
    - Correlation heatmap: Numeric columns
    - Survival rate by `Pclass` and `Sex`
  - Computes survival rates by `Pclass`, `Sex`, and `Embarked`.
- **Output**:
  - Visualizations saved as PNG files in `data/plots/`.
  - Console output with missing value checks, unique values, numeric statistics, and survival rates.

### 4. process_data.py
**Purpose**: Remove unnecessary columns and summarize categorical feature frequencies.
- **Actions**:
  - Loads `train_cleaned.csv`.
  - Drops `Name` and `Ticket` columns (not useful for modeling).
  - Counts unique values and frequencies for `Sex`, `SibSp`, `Parch`, `Embarked`, and `Deck`.
- **Output**:
  - Saves processed dataset to `train_processed.csv`.
  - Console output with unique value counts, dataset shape, column names, and missing value checks.

### 5. encode_data.py
**Purpose**: Encode categorical variables for machine learning.
- **Actions**:
  - Loads `train_processed.csv`.
  - Applies one-hot encoding to `Sex`, `Embarked`, and `Deck`, dropping the first category to avoid multicollinearity:
    - `Sex`: Encoded as `Sex_male` (reference: female)
    - `Embarked`: Encoded as `Embarked_q`, `Embarked_s` (reference: c)
    - `Deck`: Encoded as `Deck_B`, `Deck_C`, etc. (reference: A)
- **Output**:
  - Saves encoded dataset to `train_encoded_complete.csv`.
  - Console output with encoded column details, dataset shape, column names, missing values, data types, and the first 5 rows.

### 6. scale_data.py
**Purpose**: Scale numeric features to standardize them for machine learning.
- **Actions**:
  - Loads `train_encoded_complete.csv`.
  - Applies `StandardScaler` to `Age`, `Fare`, `SibSp`, and `Parch` (mean=0, std=1).
- **Output**:
  - Saves scaled dataset to `train_scaled.csv`.
  - Console output with scaled statistics, dataset shape, column names, missing values, data types, and the first 5 rows.

## How to Run the Pipeline
1. **Set up the environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   pip install pandas seaborn matplotlib scikit-learn
   ```
2. **Place the dataset**:
   - Ensure `train.csv` is in `C:\Users\ri\OneDrive\ai project\data cleaning\titanic\data\`.
3. **Run the scripts in order**:
   ```bash
   python diagnose.py
   python clean.py
   python EDA.py
   python process_data.py
   python encode_data.py
   python scale_data.py
   ```
4. **Check outputs**:
   - Intermediate datasets in `data/`.
   - Visualizations in `data/plots/`.
   - Console outputs for diagnostics and summaries.

## Key Outputs
- **Final Dataset**: `train_scaled.csv` is ready for machine learning, with:
  - No missing values.
  - Encoded categorical variables (`Sex`, `Embarked`, `Deck`).
  - Standardized numeric features (`Age`, `Fare`, `SibSp`, `Parch`).
  - Columns: `PassengerId`, `Survived`, `Pclass`, `Age`, `SibSp`, `Parch`, `Fare`, `Sex_male`, `Embarked_q`, `Embarked_s`, `Deck_B`, `Deck_C`, `Deck_D`, `Deck_E`, `Deck_F`, `Deck_G`, `Deck_T`, `Deck_Unknown`.
- **Visualizations**: Plots in `data/plots/` for data exploration.
- **Console Outputs**: Detailed diagnostics from each script.

## Notes
- The pipeline assumes the dataset is in the specified path. Update file paths in the scripts if your directory structure differs.
- The `EDA.py` script generates visualizations that help understand data distributions and survival patterns (e.g., higher survival rates for females and 1st-class passengers).
- The final dataset (`train_scaled.csv`) is suitable for training machine learning models, such as logistic regression or random forests.

## Future Improvements
- Add feature engineering (e.g., create family size from `SibSp` + `Parch`).
- Include additional visualizations (e.g., box plots, pair plots).
- Handle rare categories in `Deck` (e.g., merge low-frequency decks).
- Add error handling for missing files or unexpected data formats.

## Contact
For questions or suggestions, please reach out to the project maintainer.