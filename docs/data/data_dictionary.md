# Diccionario de datos

## Base de datos 1

* **Nombre**:  Sarcasm_Headlines_Dataset
* **Extensión**: `.json`
* **Referencia**: [Kaggle](https://www.kaggle.com/datasets/rmisra/news-headlines-dataset-for-sarcasm-detection/data)

Archivo de texto que contiene diccionarios por cada noticia registrada en la base de datos. Las entradas están separadas por una lína para cada una, en vez de caracteres especiales como `,` o `.`.

Se recomienda cargarlo como tabla para que cada atributo registrado quede como columna y visualizar las 26709 entradas disponibles.

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
| --- | --- | --- | --- | --- |
| article_link | URL de la noticia | Texto `str` | Cualquier texto en formato de URL para sitio web, incluyendo el protocolo | kaggle |
| headline | Titular de la notica a análizar | Texto `str` | Rango/Valores posibles | kaggle|
| is_sarcastic | Clasificación de si el texto es sarcástico o no | Categoría binaria `int` o `bool`| 1 para sarcasmo, 0 cuando no. | kaggle |

- **Variable**: nombre de la variable.
- **Descripción**: breve descripción de la variable.
- **Tipo de dato**: tipo de dato que contiene la variable.
- **Rango/Valores posibles**: rango o valores que puede tomar la variable.
- **Fuente de datos**: fuente de los datos de la variable.


