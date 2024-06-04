# Informe de salida

## Resumen Ejecutivo

Este informe describe los resultados del proyecto de machine learning y presenta los principales logros y lecciones aprendidas durante el proceso.

## Resultados del proyecto

- Resumen de los entregables y logros alcanzados en cada etapa del proyecto.
- Evaluación del modelo final y comparación con el modelo base.
- Descripción de los resultados y su relevancia para el negocio.

## Lecciones aprendidas

1. **Identificación de los principales desafíos y obstáculos encontrados durante el proyecto:**

- Embebido de los datos de entrenamiento: Encontrar una forma adecuada de embedder los datos de entrenamiento fue un gran desafío. Probamos tres diferentes tipos de embeddings (w2v, d2v y BERT). Los dos primeros no produjeron buenos resultados en las métricas utilizadas para evaluar los modelos (precisión, puntuación F1, recall, precisión), sin superar el 70%. Con BERT, tuvimos el problema de que las máquinas se quedaban sin memoria antes de poder procesar los datos.
- Optimización del modelo: Otro problema importante fue encontrar el modelo con los mejores resultados. Queríamos obtener un modelo que ofreciera métricas altas y que también fuera rápido. Sin embargo, los modelos base y la mayoría de las redes neuronales que probamos no cumplieron con estas expectativas.

2. **Lecciones aprendidas en relación al manejo de los datos, el modelamiento y la implementación del modelo:**

- Es fundamental tener en cuenta los recursos disponibles para el proyecto, ya que esto determinará qué enfoques se pueden utilizar.
- Durante la fase de modelado, es crucial probar todo tipo de modelos y ajustar los hiperparámetros para encontrar el modelo que ofrezca el mejor rendimiento en las métricas medidas y también en el tiempo que tarda en generar un resultado.
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

    - Mejora de la precisión: Se puede trabajar en la precisión del modelo para alcanzar niveles más altos, cercanos al 95%.
    - Optimización del tiempo de respuesta: Se podría explorar otras estructuras de redes neuronales y optimizar el preprocesamiento de las entradas sin procesar para lograr que el tiempo de respuesta sea simultáneo.
    - Actualización del conjunto de datos: Actualizar el conjunto de datos a uno más reciente podría mejorar la pertinencia y la precisión del modelo, asegurando que las etiquetas y los conceptos no hayan cambiado significativamente con el tiempo.
    - Exploración de nuevas tecnologías: Investigar y probar nuevas técnicas y tecnologías en NLP que puedan ofrecer mejoras adicionales en el rendimiento y la velocidad del modelo.

## Conclusiones

- Resumen de los resultados y principales logros del proyecto.
- Conclusiones finales y recomendaciones para futuros proyectos.

## Agradecimientos

- Agradecimientos al equipo de trabajo y a los colaboradores que hicieron posible este proyecto.
- Agradecimientos especiales a los patrocinadores y financiadores del proyecto.
