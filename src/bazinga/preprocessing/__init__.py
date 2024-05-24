'''
    Este modulo contiene funciones para cargar y preprocesar datos de texto.
    El preprocesamiento incluye la eliminacion de caracteres especiales, stopwords,
    lematizacion y eliminacion de acentos; ademas de funciones para la extraccion
    de caracteristicas de texto.
'''


# Manejo de rutas 
import path
import os

# Preprocesamiento de texto
import re
import en_core_web_sm
import pandas as pd
from unidecode import unidecode

# Extraccion de caracteristicas
from sklearn.feature_extraction.text import CountVectorizer
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from wordcloud import WordCloud

# Visualizacion
import matplotlib.pyplot as plt

directory = path.Path(os.getcwd()).abspath().dirname().parent

def load_data(filename: str = None):
    '''
        Esta funcion carga datos tipo json como un DataFrame de padnas.
        La carpeta  de carga es src/bazinga/database, y el archivo por defecto
        es Sarcasm_Headlines_Dataset.json.

        ## Argumentos
            filename : str : nombre del archivo a cargar. Si es None, se carga el archivo por defecto.

        ## Returns
            pd.DataFrame : DataFrame con los datos cargados
    
    '''
    
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
                ,min_length : int = 3, max_length : int = 45):
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

def data_preprocess(df,column_name,save = False
                ,stopword_filter  : bool = True, length_filter : bool = True
                ,lemmatize : bool = True
                ,min_length : int = 3, max_length : int = 45):
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
    df['clean_text'] = df[column_name].apply(
                            lambda x: text_preprocess(x
                                        ,stopword_filter,length_filter
                                        ,lemmatize
                                        ,min_length,max_length
                                    )
                        )
    if save:
        route = str(directory) + f'/src/bazinga/database/Clean_Headlines.json'
        df.to_json(route, orient='records', lines=True)
    return df


def vectorizar_Texto(corpus, max_features = 500):
    '''
        Esta funcion toma un corpus de texto y devuelve una matriz de texto
        vectorizada. El metodo de vectorizacion es CountVectorizer, de
        sklearn.feature_extraction.text, y se extraen max_features caracteristicas.

        # Argumentos
            corpus : List[str] : lista de textos a vectorizar
            max_feature : int : maximo numero de caracteristicas a extraer
        # Retorno
            np.ndarray : matriz de texto vectorizada
            CountVectorizer : vectorizador de texto
    
    '''
    vect = CountVectorizer(max_features = max_features)
    X = vect.fit_transform(corpus)
    X = X.toarray()
    return X, vect

def conteo_Palabras(X, vect):

    '''
        Esta funcion toma una matriz de texto y un vectorizador, y devuelve
        un DataFrame con el conteo de palabras en el texto.

        # Argumentos
            X : np.ndarray : matriz de texto
            vect : CountVectorizer : vectorizador de texto

        # Retorno
            pd.DataFrame : DataFrame con el conteo de palabras
    '''
    words = vect.get_feature_names_out()
    words = pd.DataFrame({"word": words, "count": X.sum(axis=0)})
    words = words.sort_values("count", ascending = False, kind = 'stable')
    return words

def nube_Palabras(X, vect):

    '''
    
    '''
    wc = (WordCloud(width = 800, height = 400, max_words = 100, background_color = "#FFFFFF")
            .generate_from_frequencies(dict(zip(vect.get_feature_names_out(), X.sum(axis=0)))))
    return wc


def analisisVectorizado(corpus, get_table = True, get_wc = True, get_graph = True, max_features = 500):

    X, vect = vectorizar_Texto(corpus, max_features)
    words = conteo_Palabras(X, vect)
    ans = [words]
    if get_table:
        display(words.head(10))
    if get_wc:
        wc = nube_Palabras(X, vect)
        ans.append(wc)
        if get_graph:
                fig, ax = plt.subplots()
                ax.imshow(wc)
                ax.axis("off")
                plt.show()
    return ans
    


    
    

