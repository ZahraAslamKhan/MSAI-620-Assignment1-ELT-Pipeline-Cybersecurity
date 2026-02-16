import pandas as pd

kaggle = pd.read_csv("data/raw/kaggle.csv")
cve = pd.read_csv("data/raw/cve.csv")

print("Kaggle missing values:", kaggle.isnull().sum().sum())
print("Kaggle duplicates:", kaggle.duplicated().sum())
print("CVE missing values:", cve.isnull().sum().sum())
print("CVE duplicates:", cve.duplicated().sum())

kaggle = kaggle.drop_duplicates()
kaggle = kaggle.fillna("Unknown")
if "Date" in kaggle.columns:
    kaggle["Date"] = pd.to_datetime(kaggle["Date"], errors="coerce")

cve = cve.drop_duplicates()
cve = cve.fillna("Unknown")
if "published" in cve.columns:
    cve["published"] = pd.to_datetime(cve["published"], errors="coerce")

print("Kaggle summary:\n", kaggle.describe(include="all"))
print("CVE summary:\n", cve.describe(include="all"))

kaggle.to_csv("data/cleaned/kaggle_clean.csv", index=False)
cve.to_csv("data/cleaned/cve_clean.csv", index=False)
