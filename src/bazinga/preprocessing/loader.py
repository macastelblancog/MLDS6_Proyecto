import pandas as pd
import path
import os

directory = path.Path(os.getcwd()).abspath().dirname().parent

def load_raw_data(route : str = None):
    if route  is None:
        route = str(directory) + '/src/bazinga/database/Sarcasm_Headlines_Dataset.json'
        print(route)
    try:
        return pd.read_json(route, lines=True)
    except:
        raise FileNotFoundError('Error en archivo de datos.')