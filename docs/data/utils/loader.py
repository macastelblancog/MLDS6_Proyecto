import pandas as pd

def load_raw_data(path : str = None):
    if path is None:
        path = '../inputs/Sarcasm_Headlines_Dataset.json'
    try:
        return pd.read_json(path, lines=True)
    except:
        raise FileNotFoundError('Error en archivo de datos.')