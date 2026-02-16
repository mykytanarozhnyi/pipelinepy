import pandas as pd

def extract_data(file_path):
    """Load data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        raise
