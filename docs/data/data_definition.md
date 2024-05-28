
# Definición de los datos

## Origen de los datos

El dataset original, llamado [`Sarcasm_Headlines_Dataset`](../../src/bazinga/database/Sarcasm_Headlines_Dataset.json), se descargó de [Kaggle](https://www.kaggle.com/datasets/rmisra/news-headlines-dataset-for-sarcasm-detection/data), y se encuentra en la carpeta de [database](../../src/bazinga/database/).

## Especificación de los scripts para la carga de datos

En la carga de datos se hace mediante el modulo de [`preprocessing`](../../src/bazinga/preprocessing/) empleando la función `load_raw_data`. La función por defecto carga los datos crudos, pero se pueden especificar nombres de archivos presentes dentro de [`database`](../../src/bazinga/database/).

## Referencias a rutas o bases de datos origen y destino

La carpeta padre de la librería es [src](../../src), por lo que en los códigos de [scripts](../../scripts) se especifica, usando la librería `sys`, que se pueden cargar librerías desde la carpeta principal del proyecto. `load_raw_data`, de [`preprocessing`](../../src/bazinga/preprocessing/), se enruta yendo desde la carpeta del proyecto a [`database`](../../src/bazinga/database/) para cargar la información.

### Rutas de origen de datos

- Los datos crudos se traen de [database](../../src/bazinga/database/), y los procesados se guardan allí también.

- Los datos se guardan como un `json` separado por líneas, donde las llaves en cada entrada corresponden a los atributos presentados en el [diccionario de datos](./data_dictionary.md).

- La función principal de [preprocessing](../../src/bazinga/preprocessing/) es `text_preprocessing`, la cual toma una cadena de texto y:
    1. Quita caracteres especiales (a excepción de comillas, dado que pueden sugerir sarcasmo).
    2. Puede filtrar por stopwords y longitud de los tokens.
    3. Tiene opción para lematizar, o retornar el texto.
    4. Devuelve el texto en minúsculas (sin acentos).

## Extracción de Características

Para la extracción de características se utilizaron embeddings de BERT y Word2Vec debido a sus capacidades complementarias en la representación de texto.

### BERT

BERT (Bidirectional Encoder Representations from Transformers) es un modelo de lenguaje preentrenado que captura relaciones contextuales entre palabras en un texto. Se utilizó el modelo preentrenado `bert-base-uncased` para generar embeddings de los titulares. Cada titular se codificó en una representación de tamaño 768. BERT fue elegido por las siguientes razones:

1. **Comprensión Contextual Bidireccional**: BERT analiza el contexto de una palabra considerando tanto su lado izquierdo como su lado derecho en una oración, lo cual es crucial para detectar el sarcasmo que depende de un contexto más amplio y sutil.

2. **Rendimiento en Tareas de Lenguaje Natural**: BERT ha demostrado un rendimiento superior en una variedad de tareas de procesamiento del lenguaje natural, lo que lo hace adecuado para la clasificación de textos complejos como los titulares sarcásticos.

- **Código de Preprocesamiento y Generación de Embeddings BERT**: [Embeddings.ipynb](../../scripts/training/)
- **Embeddings BERT Guardados**: [bert_embeddings.npy](../../src/bazinga/database/)

### Word2Vec

Word2Vec es un modelo basado en redes neuronales que genera embeddings continuos para palabras, entrenado en el contexto local de las palabras. Se entrenó un modelo Word2Vec en los titulares tokenizados y se generaron embeddings promediados para cada titular. Las representaciones tienen un tamaño de 300. Word2Vec fue elegido por las siguientes razones:

1. **Simplicidad y Eficiencia**: Word2Vec es menos complejo y más eficiente en términos computacionales en comparación con modelos más avanzados, lo que facilita el procesamiento rápido y eficiente de grandes conjuntos de datos.

2. **Captura de Relaciones Semánticas**: Word2Vec es eficaz para capturar relaciones semánticas entre palabras, lo que puede ser beneficioso para identificar patrones de palabras comunes en titulares sarcásticos.

- **Código de Preprocesamiento y Generación de Embeddings Word2Vec**: [Embeddings.ipynb](../../scripts/training/)
- **Embeddings Word2Vec Guardados**: [w2v_embeddings.npy](../../src/bazinga/database/)
