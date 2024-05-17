# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

Nuestro conjunto de datos se compone de un total de 26709 observaciones y cuenta con 3 variables: article_link, head_line y is_sarcastic.

Article_link es una variable de tipo String y corresponde al hipervínculo de la noticia original. La variable headline es tambien de tipo String e indica el titular de la noticia, por último, is_sarcastic es de tipo Integer y toma valores de 0 ó 1 indicando si el headline descrito es de carácter sarcástico o no. 

Por otro lado, el dataset no cuenta con valores faltantes en ninguna de sus columnas, aunque si se identificaron algunos valores repetidos (107 en total). Eliminando dichos valores, tanto en la columna article_link como head_line todos su valores son únicos mientras que la columna is_sarcastic cuenta con 14951 entradas con valor 0 y 11651 de valor 1, es decir, una distribución de 56%-41% lo que nos indica que hay una leve desproporción de los datos hacia aquellos headlines que no son considerados como sarcásticos.


## Resumen de calidad de los datos

El dataset parece estar bstante bien documentado en el sentido que no cuenta con valores faltantes en ninguna de sus columnas. Por otra parte, la columna headline la cual se espera que tenga únicamente valores únicos realmente cuenta con 107 valores duplicados, por lo que optamos por deshacernos de las filas donde se presenta dicha duplicidad. Por ultimo, la variable “is_sarcastic” confirmamos que únicamente cuenta con valores 0 y 1 como se espera, por lo que el dataset no contiene valores extremos o que se cataloguen como erróneos.

## Variable objetivo

la columna is_sarcastic la cual se toma como la variable objetivo cuenta con 26602 entradas (Después de eliminar duplicados) las cuales toman valor de 0 y 1 e indican si la entrada el headline de la noticia asociada es de carácter sarcástico o no. Al analizar la distribución de esta variable vemos que esta cuenta con 14591 filas con valor 0 y 11651 de valor 1, es decir, una distribución de 56%-41% lo que nos indica que hay una leve desproporción de los datos hacia aquellos headlines que no son considerados como sarcásticos.

![PlotDistribucion](../Images/Histogram.png)

## Variables individuales

En esta sección se presenta un análisis detallado de cada variable individual. Se muestran estadísticas descriptivas, gráficos de distribución y de relación con la variable objetivo (si aplica). Además, se describen posibles transformaciones que se pueden aplicar a la variable.

## Ranking de variables

En esta sección se presenta un ranking de las variables más importantes para predecir la variable objetivo. Se utilizan técnicas como la correlación, el análisis de componentes principales (PCA) o la importancia de las variables en un modelo de aprendizaje automático.

## Relación entre variables explicativas y variable objetivo

En esta sección se presenta un análisis de la relación entre las variables explicativas y la variable objetivo. Se utilizan gráficos como la matriz de correlación y el diagrama de dispersión para entender mejor la relación entre las variables. Además, se pueden utilizar técnicas como la regresión lineal para modelar la relación entre las variables.
