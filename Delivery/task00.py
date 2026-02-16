import pandas as pd


def make_dataframe(path: str):
    df = pd.read_csv(path)

    df = df.dropna(subset=["Latitude", "Longitude"])

    return df