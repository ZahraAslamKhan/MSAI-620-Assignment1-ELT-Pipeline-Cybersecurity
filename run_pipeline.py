from extract_api import get_cve_data
from extract_kaggle import get_kaggle_data
from extract_trends import get_trends_data
from load_data import save_processed

def run_pipeline():
    cve_table = get_cve_data()
    kaggle_table = get_kaggle_data()
    trends_table = get_trends_data()

    save_processed(cve_table, "cve_processed")
    save_processed(kaggle_table, "kaggle_processed")
    save_processed(trends_table, "trends_processed")

if __name__ == "__main__":
    run_pipeline()
