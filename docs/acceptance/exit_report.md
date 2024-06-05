# Informe de salida

## Resumen Ejecutivo

Este proyecto plantea el diseño y desarrollo de una aplicación para la clasificación binaria de titulares de noticias en inglés, en sarcástico o no. Los usuarios pueden cargar un texto o una lista de textos y obtener con la clasificación un porcentaje con la probabilidad de que cada uno de los titulares sea sarcástico. Los modelos se pueden acceder mediante una aplicación en ML Flow o através de este repositorio, copiando la carpeta de src e importanto el módulo Bazinga para importar modelos o generar uno nuevo.

## Resultados del proyecto

- Se desarrolló una runtina personalizada para la limpieza del texto, para posteriormente usar BERT para tokernizar y hacer embbedings del texto, con el objetivo de extraer las características de los titulares de entrada.
- Para resolver el problema de clasificación de sarcasmo en titulares de noticias, se desarrolló un modelo basado en una red multicapa compuesta de capas densas. Este modelo y sus respectivas metrícas está guardado en MLflow con el nombre de 'NN-BinaryCross-RMSprop'.
- El modelo obtenido permite hacer las clasificación de un texto o una lista de textos, donde se retorna por cada titular la probabilidad de que sea sarcástico. Aunque se obtuvo un F1 de más del 90% al entrenar, con los datos de validación no se obtuvieron resultados similares, lo que sugiere posibles problemas de generalización del modelo.

## Lecciones aprendidas

1. **Identificación de los principales desafíos y obstáculos encontrados durante el proyecto:**

- **Embebido de los datos de entrenamiento:** Encontrar una forma adecuada de embedder los datos de entrenamiento fue un gran desafío. Probamos tres diferentes tipos de embeddings (w2v, d2v y BERT). Los dos primeros no produjeron buenos resultados en las métricas utilizadas para evaluar los modelos (precisión, puntuación F1, recall, precisión), sin superar el 70%. Con BERT, tuvimos el problema de que las máquinas se quedaban sin memoria antes de poder procesar los datos.
- **Optimización del modelo:** Otro problema importante fue encontrar el modelo con los mejores resultados. Queríamos obtener un modelo que ofreciera métricas altas y que también fuera rápido. Sin embargo, los modelos base y la mayoría de las redes neuronales que probamos no cumplieron con estas expectativas, ya que se obtenian buenas métricas al entrenar, pero no al validar; por lo que los modelos podrían presentar problemas de generalización.

2. **Lecciones aprendidas en relación al manejo de los datos, el modelamiento y la implementación del modelo:**

- Las operaciones de embeddings apoyadas de BERT requieren del apoyo de una GPU, en especial para la fase de entrenamiento del modelo. Para esto, fue muy útil plantear una rutina apoyada en PyTorch para optimizar tiempos en el desarrollo.
- Los paquetes de instalación de PyTorch y Keras para GPU, apoyados en CUDA, no son compatibles, por lo que la optimización de la rutina de procesamiento de BERT no se podia usar en un Pipeline para hacer un entrenamiento con Tensorflow optimizado con GPU simultaneamente.
- Para la implementación, es muy importante guardar correctamente el modelo en MLflow y considerar en qué formato se deben administrar los datos de entrada para que los datos sin procesar proporcionados por el usuario puedan preprocesarse y dejarse en un formato que el modelo pueda usar.

3. **Recomendaciones para futuros proyectos de machine learning:**

- Evaluar los recursos disponibles: Asegúrate de evaluar los recursos disponibles al inicio del proyecto, ya que esto influirá en la elección de métodos y herramientas, evitando problemas como la falta de memoria al usar embeddings complejos como BERT.
- Probar y ajustar múltiples modelos y configuraciones: Durante la fase de modelado, prueba diversos tipos de modelos y configuraciones de hiperparámetros para encontrar la combinación óptima que ofrezca un buen equilibrio entre rendimiento y velocidad.
- Preprocesamiento adecuado de datos: Invierte tiempo suficiente en el preprocesamiento de datos para garantizar que estén en el formato adecuado y sean de alta calidad antes de alimentar el modelo.
- Documentar y versionar el modelo: Guarda y documenta correctamente el modelo en una plataforma como MLflow, incluyendo detalles sobre el formato de entrada y el preprocesamiento necesario para asegurar una implementación y mantenimiento fluidos.
- Planificación y evaluación continuas: Realiza evaluaciones y ajustes continuos del modelo para mejorar su rendimiento, y fomenta una colaboración interdisciplinaria para aprovechar diferentes perspectivas y conocimientos.

## Impacto del proyecto

- **Descripción del impacto del modelo en el negocio o en la industria:**

    Este modelo puede ayudar en la detección y filtrado de datos sarcásticos, evitando que los modelos de procesamiento de lenguaje natural (NLP) utilicen datos sarcásticos como datos directos, lo que podría introducir sesgos en el entrenamiento, como es el caso de la búsqueda de IA de Google.

- **Identificación de las áreas de mejora y oportunidades de desarrollo futuras:**

    - Mejora de la precisión: Se puede trabajar en la precisión del modelo para alcanzar niveles más altos, cercanos al 95% que además se puedan generalizar para datos nuevos por fuera del conjunto de datos del entrenamiento.
    - Optimización del tiempo de respuesta: Se podría explorar otras estructuras de redes neuronales y optimizar el preprocesamiento de las entradas sin procesar para lograr que el tiempo de respuesta sea simultáneo.
    - Actualización del conjunto de datos: Actualizar el conjunto de datos a uno más reciente podría mejorar la pertinencia y la precisión del modelo, asegurando que las etiquetas y los conceptos no hayan cambiado significativamente con el tiempo. A su vez, usar otros titulares que no se enfoquen en hechos de Estados Unidos e incluso estén en otros idiomas.
    - Exploración de nuevas tecnologías: Investigar y probar nuevas técnicas y tecnologías en NLP que puedan ofrecer mejoras adicionales en el rendimiento y la velocidad del modelo.

## Conclusiones

- Se desarrolló una red neuronal secuencial para la clasificación de titulares de noticiar en sarcásticos o no sarcásticos con un F1 del 90%, accesible mediante un módulo importable o MLFlow.
- Se empleó el modelo BERT para el tokenizado y embeddings de los texto, apoyado de una rutina previa para procesamiento del texto que permite garantizar una buena extracción de características antes del modelamiento.

## Agradecimientos

- Agradecimientos al equipo de trabajo y a los colaboradores que hicieron posible este proyecto.
- Agradecimientos especiales a los patrocinadores y financiadores del proyecto.
