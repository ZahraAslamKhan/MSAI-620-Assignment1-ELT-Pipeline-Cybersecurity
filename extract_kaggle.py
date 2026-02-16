import pandas as pd
from config import kaggle_file_path

def get_kaggle_data():
    table = pd.read_csv(kaggle_file_path)
    table.to_csv("data/raw/kaggle.csv", index=False)
    table.to_json("data/raw/kaggle.json", orient="records")
    return table
