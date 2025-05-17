# run_pipeline.py

from extract import extract_data
from transform import transform_data
from load import save_to_csv

# File paths
input_file = 'data/Uncleaned_DS_jobs.csv'
output_file = 'data/Cleaned_DS_jobs.csv'

def run_etl():
    print("Starting ETL pipeline...\n")
    raw_df = extract_data(input_file)
    print("Data extracted.")

    cleaned_df = transform_data(raw_df)
    print("Data transformed.")

    save_to_csv(cleaned_df, output_file)
    print("Data loaded and pipeline completed successfully.")

if __name__ == '__main__':
    run_etl()
