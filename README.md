
This repository demonstrates basic data-cleaning steps on the Kaggle Titanic dataset.


## Commit 1: Environment Setup & Initial Data Inspection

- **Environment**  
  - Created and activated a Python virtual environment:  
    ```bash
    python -m venv venv
    # PowerShell:
    .\venv\Scripts\Activate
    # macOS/Linux:
    source venv/bin/activate
    ```
  - Installed `pandas` and froze exact versions to `requirements.txt` via:
    ```bash
    pip install pandas
    pip freeze > requirements.txt
    ```
  - Added `.gitignore` to exclude:
    ```
    venv/
    __pycache__/
    *.pyc
    ```

- **Raw Data**  
  - Committed the original Titanic CSV under `data/train.csv` so no external download is required.

- **Inspection Script** (`titanic_clean.py`)  
  - Loaded the data and ran:
    ```python
    import pandas as pd
    df = pd.read_csv("data/train.csv")
    print(df.shape)           # → (891, 12)
    print(df.columns)         # → list of 12 column names
    print(df.isnull().sum())  # → missing-value counts
    df.info()                 # → types & non-null counts
    ```
  - Executed with:
    ```bash
    python titanic_clean.py
    ```

- **Key Findings**  
  - **Age**: 177 missing values (~20%)  
  - **Cabin**: 687 missing values (~77%)  
  - **Embarked**: 2 missing values (<1%)

> This initial commit sets up our environment, brings in the raw data, and identifies which fields need cleaning or imputation.  


## Commit 2: Exploratory Data Analysis

**EDA Script**  
Created `titanic_eda.py` to explore data distributions, missingness, and feature relationships.

- **Dependencies:**  
  ```bash
  pip install matplotlib seaborn missingno

- Executed with:
    ```bash
    python titanic_eda.py
    ```
![image](https://github.com/user-attachments/assets/4d83215f-8caa-4b06-8ce2-ef427fac22cc)






## Commit 3: Missing-Value Imputation & EDA Integration

- **Imputation Script** (`titanic_imputation.py`)  
  - Created a standalone imputation module with `argparse` support:  
    ```bash
    python titanic_imputation.py --input data/train.csv --output data/train_imputed.csv
    ```  
  - Applies simple strategies:  
    - Fills missing `Age` with the median  
    - Fills missing `Embarked` with the mode  
    - Drops the `Cabin` column entirely  
  - Prints null-count summaries before and after imputation:
    ```bash
    Before imputation:
      PassengerId      0
      Survived         0
      Pclass           0
      Name             0
      Sex              0
      Age            177
      SibSp            0
      Parch            0
      Ticket           0
      Fare             0
      Cabin          687
      Embarked         2

    After imputation:
      PassengerId    0
      Survived       0
      Pclass         0
      Name           0
      Sex            0
      Age            0
      SibSp          0
      Parch          0
      Ticket         0
      Fare           0
      Embarked       0
    ```

- **EDA Script Update** (`titanic_eda.py`)  
  - Changed the default data source to the imputed file:
    ```diff
    - df = pd.read_csv("data/train.csv")
    + df = pd.read_csv("data/train_imputed.csv")
    ```
  - Added an optional `--input` argument for flexibility:
    ```bash
    python titanic_eda.py --input data/train.csv
    ```

    <img width="1916" height="974" alt="image" src="https://github.com/user-attachments/assets/75d588d0-b7ba-4497-a057-04e5b0860111" />


> This commit adds a reproducible imputation step, integrates the cleaned dataset into the EDA pipeline, and updates documentation accordingly.
