# load.py

def save_to_csv(df, output_path):
    """
    Saves the cleaned DataFrame to a CSV file.

    Parameters:
        df (pd.DataFrame): The cleaned DataFrame.
        output_path (str): Destination file path for CSV.
    """
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to: {output_path}")
