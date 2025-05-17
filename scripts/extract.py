# extract.py

import pandas as pd

def extract_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv("Data-Science-Jobs-Trends-Analysis/Data/Uncleaned_DS_jobs.csv")
    return df
