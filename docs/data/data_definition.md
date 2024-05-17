# Definición de los datos

## Origen de los datos

El dataset original, llamado [`Sarcasm_Headlines_Dataset`](../../src/bazinga/database/Sarcasm_Headlines_Dataset.json), se descargó de [Kaggle](https://www.kaggle.com/datasets/rmisra/news-headlines-dataset-for-sarcasm-detection/data), y se encuentra en la carpeta de [database](../../src/bazinga/database/). 

## Especificación de los scripts para la carga de datos

En la carga de datos se hace mediante el modulo de [`preprocessing`](../../src/bazinga/preprocessing/) empleando la función `load_raw_data`. La función por defecto carga los datos crudos, pero se pueden especificar nombres de archivos presentes dentro de [`database`](../../src/bazinga/database/).

## Referencias a rutas o bases de datos origen y destino

La carpeta padre de la liberia es [src](../../src), por lo que en los códigos de [scripts](../../scripts) se especifica, usando la libreria `sys`, que se pueden cargar librerias desde la carpeta principal del proyecto. `load_raw_data`, de [`preprocessing`](../../src/bazinga/preprocessing/), se enruta yendo desde la carpeta del proyecto a [`database`](../../src/bazinga/database/) para cargar la información.

### Rutas de origen de datos

- Los datos crudos se traen de [database](../../src/bazinga/database/), y los procesados se guardan alli también.

- Los datos se guardan como un `json` seperado por lineas, donde las llaves en cada entrada corresponde a los atributos presentad oen el [diccionario de datos](./data_dictionary.md).

- La función principal de [preprocessing](../../src/bazinga/preprocessing/) es `text_preprocessing`, la cual  toma una cadena de texto y:

    1.  Quita caracteres especiales (a excpecion de comillas, dado que pueden sugerir sarcasmo).
        
    2. Puede filtrar por stopwords y longitud de los tokens.

    3. Tiene opción para lematizar, o retornar el texto.

    3. Devuelve el texto en minusculas (sin acentos).

