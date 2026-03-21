import os

import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Loads a CSV file from the specified path and returns its content
    as a pandas DataFrame.

    This function verifies the existence of the file at the given path
    before attempting to read it. If the file does not exist, a
    FileNotFoundError is raised. The contents of the file are read
    into a pandas DataFrame and returned.

    Args:
        path (str): The file path to the CSV file to be loaded.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the data from the CSV file.

    Raises:
        FileNotFoundError: If the file does not exist at the specified path.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(path)
    print(f"Loading dataset dimensions: ({df.shape[0]}, {df.shape[1]})")

    return df
