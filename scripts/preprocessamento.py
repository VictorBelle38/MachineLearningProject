import pandas as pd

def load_data(data):
    """Carrega o dataset a partir de um arquivo CSV."""
    return pd.read_csv(filepath)

def clean_data(df):
    """Remove linhas com valores faltantes."""
    return df.dropna()

def normalize_data(df):
    return (df - df.mean()) / df.std()