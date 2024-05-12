# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Análisis de sentimientos (sarcasmo) para noticias en inglés con ML

## Objetivo del Proyecto

El objetivo de este proyecto es desarrollar un modelo de machine learning que pueda detectar automáticamente si un titular de noticia es sarcástico o no. Esto implica construir y entrenar un modelo de clasificación de texto que pueda generalizar correctamente a partir de los datos disponibles.

La detección de sarcasmo en texto es un desafío importante en el procesamiento del lenguaje natural, ya que el sarcasmo a menudo se basa en el contexto y en las sutilezas del lenguaje que pueden ser difíciles de capturar para los modelos de manera convencional. Un modelo preciso de detección de sarcasmo puede tener aplicaciones en la mejora de la comprensión automática del lenguaje, la detección de emociones y actitudes en el texto, y la creación de sistemas de diálogo más avanzados y sensibles al contexto.

## Alcance del Proyecto

El dataset "News Headlines Dataset For Sarcasm Detection" contiene titulares de noticias etiquetados como sarcásticos o no sarcásticos. Se compone de dos conjuntos de datos: uno con titulares sarcásticos obtenidos del sitio web TheOnion y otro con titulares no sarcásticos obtenidos de HuffPost. Cada instancia incluye el titular de la noticia y la etiqueta de sarcasmo.

Se espera desarrollar un modelo de machine learning basado en procesamiento del lenguaje natural (NLP) que pueda clasificar correctamente si un titular de noticia es sarcástico o no. El modelo debería tener un desempeño sólido en términos de precisión, recall y F1-score en un conjunto de datos de prueba.
El proyecto se considerará exitoso si se logran los siguientes objetivos:

•	Desarrollar un modelo de detección de sarcasmo en titulares de noticias con una precisión mínima del 80% en un conjunto de datos de prueba.

•	Demostrar la capacidad del modelo para generalizar a nuevos titulares de noticias y detectar sarcasmo con precisión.

•	Proporcionar análisis e interpretación de los resultados para entender qué características o palabras clave son importantes para la detección de sarcasmo en el texto.

## Metodología

En nuestro proyecto de detección de sarcasmo en titulares de noticias, comenzaremos cargando y explorando un dataset de Kaggle para familiarizarnos con sus características. Luego, procederemos a preprocesar los textos mediante técnicas de limpieza y tokenización, utilizando embeddings pre-entrenados para transformar los titulares en vectores numéricos. 

Desarrollaremos un modelo con redes neuronales varias para aprovechar sus fortalezas en la captura de patrones locales y dependencias de largo alcance. Tras entrenar y optimizar nuestro modelo con técnicas como la validación cruzada, evaluaremos su desempeño usando métricas como precisión y recall, y finalmente lo prepararemos para despliegue en un entorno de producción, asegurando su capacidad de clasificar nuevos titulares.

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1.5 semanas | del 2 de mayo al 11 de mayo |
| Preprocesamiento, análisis exploratorio | 1 semana | del 9 de mayo al 16 de mayo |
| Modelamiento y extracción de características | 1 semana | del 16 de mayo al 23 de mayo |
| Despliegue | 1 semana | del 23 de mayo al 30 de mayo |
| Evaluación y entrega final | 1 semana | del 30 de mayo al 4 de junio |

## Equipo del Proyecto

* Lider de equipo
    - Miguel Castelblanco
* Científico de datos
    - Santiago Correa 
    - Juan Sebastian Valdes Fuentes

## Presupuesto

[Descripción del presupuesto asignado al proyecto]

## Stakeholders

Para la implementación del proyecto en un posible mercado laboral real propondremos 2 potenciales stakeholders.

*Stakeholder 1:* Director de Tecnología (CTO) de una empresa de análisis de medios de comunicación

 Está interesado en mejorar las capacidades de análisis de texto de la empresa para ofrecer servicios más avanzados a sus clientes. Busca soluciones tecnológicas que puedan detectar el sarcasmo en los titulares de noticias para mejorar la precisión de los análisis de medios de comunicación. Espera que el proyecto proporcione un modelo de detección de sarcasmo en titulares de noticias que pueda integrarse en los sistemas de análisis de medios de comunicación de la empresa. Busca un modelo preciso y eficiente que mejore la calidad de los análisis realizados.

*Stakeholder 2:* Gerente de Producto de una empresa de tecnología que desarrolla herramientas de análisis de texto

 Busca incorporar funcionalidades de detección de sarcasmo en las herramientas de análisis de texto de la empresa para hacerlas más atractivas para clientes potenciales y mejorar la competitividad en el mercado. Espera que el proyecto genere resultados tangibles que puedan incorporarse rápidamente en las herramientas de análisis de texto existentes de la empresa. Busca una solución innovadora que mejore la funcionalidad de las herramientas y atraiga a nuevos clientes.


## Aprobaciones

Para los 2 stakeholders presentados el cargo de quien aprueba el proyecto será el Director de Operaciones (COO) de la empresa. 

*Stakeholder 1:* Juan Miguel Valdes. 04/07/2024

*Stakeholder 2:* Santiago Castelblanco Correa. 04/07/2024
