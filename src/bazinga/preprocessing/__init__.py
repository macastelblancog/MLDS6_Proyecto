import pandas as pd
import path
import os
import re
from unidecode import unidecode
import en_core_web_sm

directory = path.Path(os.getcwd()).abspath().dirname().parent

def load_raw_data(filename: str = None):
    
    route = str(directory) + '/src/bazinga/database/Sarcasm_Headlines_Dataset.json'
    if not filename is None:
        route = str(directory) + f'/src/bazinga/database/{filename}'
    try:
        return pd.read_json(route, lines = True)
    except:
        raise FileNotFoundError('Error en archivo de datos.')
    


# Load the spaCy model
nlp = en_core_web_sm.load()

def text_preprocess(text
                ,stopword_filter  : bool= True, length_filter : bool = True
                ,lemmatize : bool = True
                ,min_length : int = 1, max_length : int = 45):
    '''
        Esta funcion toma una cadena de texto y la preprocesa de acuerdo a
        los parametros de entrada. En general, quita caracteres especiales
        (a excpecion de comillas), puede quitar stopwords y lematizar, para 
        finalmente devolver el texto en minusculas (sin acentos).

        # Argumentos
            text : str : texto a preprocesar
            stopword_filter : bool : si se quieren quitar stopwords
            length_filter : bool : si se quiere filtrar por longitud
            lemmatize : bool : si se quiere lematizar. Si es False, se devuelve el texto tal cual
            min_length : int : longitud minima de palabra
            max_length : int : longitud maxima de palabra

        # Retorno
            str : texto preprocesado
    '''

    def token_filter(token):
        '''
            Funcion auxiliar para filtrar por stopwords o longitud.
        '''
        condition1, condition2 = True, True
        if stopword_filter: condition1 = (not token.is_stop)
        if length_filter: condition2 = (min_length <= len(token) <= max_length)
        return condition1 and condition2
    
    def tokenize(token):
        '''
            Funcion auxiliar para lematizar o devolver el texto tal cual.
        '''
        if lemmatize: return token.lemma_
        else: return token.text
    
    # Quitar espacios en blanco al inicio y final
    preprocess_text = text.strip(" ")
    # Quitar caracteres especiales, excepto comillas sencillas
    preprocess_text = re.sub(r"[^\w\s\"']", " ", preprocess_text)
    # Lematizacion y filtrado
    preprocess_text = " ".join([tokenize(token) for token in nlp(preprocess_text) if token_filter(token)])
    # Quitar espacios en blanco
    preprocess_text = re.sub(r"\s+", " ", preprocess_text)
    # Quitar acentos y pasar a minusculas
    preprocess_text = unidecode(preprocess_text).lower()
    return preprocess_text

def data_preprocess(df,column_name,save=True):
    '''
        Esta funcion escala la rutina de text_preprocess para aplicarlo a 
        múltiples textos en un DataFrame de pandas. Similar a un vectorizado,
        mediante el método apply.

        # Argumentos
            df : pd.DataFrame : DataFrame con los textos a preprocesar
            column_name : str : nombre de la columna con los textos
        # Retorno
            pd.DataFrame : DataFrame con los textos preprocesados
            La columna se llama clean_text
    '''
    df['clean_text'] = df[column_name].apply(lambda x: text_preprocess(x))
    if save:
        route = str(directory) + f'/src/bazinga/database/Clean_Headlines.json'
        df.to_json(route, orient='records', lines=True)
    return df