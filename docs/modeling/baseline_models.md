# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

El modelo baseline es el primer modelo construido y se utiliza para establecer una línea base para el rendimiento de los modelos posteriores. Para el desarrollo de este proyecto, al ser un problema de clasificacion se optó por un modelo de tipo DummyClassifier, además, ya que la clasificación abordaba el texto completo de cada entrada y no palabras o tokens especificos como tal, se hizo uso de un embedding de tipo Doc2Vec para los headlines del corpus.

## Variables de entrada

**Headline**: Los titulares de noticias son la única variable de entrada utilizada en el modelo. Cada titular se convierte en un vector numérico utilizando Doc2Vec, lo que permite que el modelo procese los datos textuales de manera eficiente.

## Variable objetivo

**is_sarcastic label**:: La variable objetivo es una etiqueta de tipo binaria que indica si un titular de noticia es sarcástico (1) o no sarcástico (0).


## Evaluación del modelo

Ya que el modelo entrenado cumple una tarea de clasificación, para evaluar su desempeño haremos uso de la metrica de precision (accuracy), esta mide la proporción de predicciones correctas sobre el total de predicciones realizadas. El modelo entrenado obtuvo una precisión del 50%, lo que indica que al predecir una etiqueta de sarcasmo el modelo acertará en la mitad de las ocasiones.

## Análisis de los resultados

**Fortalezas del modelo baseline:**

**-Simplicidad:** El DummyClassifier es fácil de implementar y sirve como un punto de partida claro para evaluar modelos más complejos.

**-Rápido de entrenar:** Debido a su simplicidad, el modelo se entrena rápidamente, permitiendo una rápida iteración y comparación con modelos posteriores.

**Debilidades del modelo baseline:**

**-Bajo rendimiento:** Una precisión de 0.50 indica que el modelo apenas supera la precisión del azar (50%), lo que sugiere que no es efectivo para la tarea de detección de sarcasmo.

**-Falta de sofisticación:** El DummyClassifier no aprovecha las características complejas de los datos textuales y no tiene capacidad para aprender patrones significativos.

## Conclusiones

**-Rendimiento general:** El modelo baseline, con una precisión de 0.50, establece una línea base que supera el rendimiento de un clasificador aleatorio. Esto subraya la necesidad de desarrollar modelos más avanzados para mejorar significativamente la detección de sarcasmo.

**-Áreas de mejora:** Para mejorar el rendimiento, se considerarán modelos más sofisticados como Support Vector Machines (SVM) ó Random Forests. También se explorarán técnicas de preprocesamiento de texto más avanzadas y la utilización de embeddings preentrenados más complejos.

**-Próximos pasos:** El siguiente paso es entrenar y evaluar modelos más complejos utilizando técnicas avanzadas de procesamiento del lenguaje natural y machine learning, comparando sus rendimientos con la línea base establecida por el DummyClassifier.
