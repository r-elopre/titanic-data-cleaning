
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

