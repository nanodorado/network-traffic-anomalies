import pandas as pd

def load_data(file_path):
    """
    Load and preprocess data from a CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    DataFrame: Preprocessed data.
    """
    try:
        data = pd.read_csv(file_path)
        data['timestamp'] = pd.to_datetime(data['timestamp'])
        return data
    except Exception as e:
        raise Exception(f"Error loading data: {e}")
