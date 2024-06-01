# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** NN-BinaryCross-RMSprop
- **Plataforma de despliegue:** MLflow (local)
- **Requisitos técnicos:** 

### Bibliotecas y Versiones
- mlflow==2.13.0
- keras==3.3.3
- tensorflow==2.16.1
- torch==2.3.0
- transformers==4.41.2
- scikit-learn==1.5.0
- gensim==4.3.2
- spacy==3.7.4
- matplotlib==3.9.0
- pandas==2.2.2
- numpy==1.26
### Descripción
El modelo de despliegue requiere las siguientes bibliotecas y versiones para su funcionamiento. Estas bibliotecas son utilizadas para el preprocesamiento de texto, extracción de características y visualización de datos. Además, se incluyen las bibliotecas necesarias para el uso de MLflow como plataforma de despliegue.

Se recomienda instalar estas bibliotecas utilizando un entorno virtual para evitar conflictos con otras bibliotecas o versiones de Python.

## Requisitos de Seguridad

No se requieren requisitos especiales de seguridad, ya que el modelo se utilizará localmente y no se trabajarán con datos confidenciales.

## Diagrama de Arquitectura

El modelo se desplegará y ejecutará localmente desde una terminal. La arquitectura es simple y consta de los siguientes componentes:

- **Entorno Local:** Incluye el entorno de desarrollo donde se encuentra instalado MLflow y las bibliotecas necesarias para el modelo.
- **MLflow Local:** MLflow se ejecuta localmente y permite gestionar y desplegar el modelo.
- **Terminal:** Se utiliza para interactuar con MLflow y el modelo, permitiendo realizar solicitudes y recibir predicciones.

## Código de despliegue

- **Archivo principal:** (nombre del archivo principal que contiene el código de despliegue)
- **Rutas de acceso a los archivos:** (lista de rutas de acceso a los archivos necesarios para el despliegue)
- **Variables de entorno:** (lista de variables de entorno necesarias para el despliegue)

## Documentación del despliegue

### Instrucciones de Instalación

1. **Crear y activar un entorno virtual (opcional pero recomendado):**
   - Para crear un entorno virtual con `venv` en Unix/macOS:
     ```bash
     python3 -m venv myenv
     source myenv/bin/activate
     ```
   - Para crear un entorno virtual con `venv` en Windows:
     ```bash
     python -m venv myenv
     myenv\Scripts\activate
     ```
   - Para crear un entorno virtual con `conda`:
     ```bash
     conda create --name myenv
     conda activate myenv
     ```

2. **Instalar MLflow:**
   ```bash
   pip install mlflow==2.13.0
   ```
3. **Instalar las bibliotecas necesarias:**
    ```bash
    pip install keras==3.3.3 tensorflow==2.16.1 torch path os re pandas unidecode numpy scikit-learn gensim transformers spacy matplotlib
    ```
4. **Clonar el Repositorio:** 
    ```bash
    git clone https://github.com/macastelblancog/MLDS6_Proyecto
    ```
5. **Navegar al Directorio del Repositorio:**

    ```bash
    cd MLDS6_Proyecto
    ```
6. **Cargar el Modelo:** Ir a la carpeta de [visualización](../../src/bazinga/visualization/) en la terminal y arrancar el servicio CLI de MLflow:
    ```bash
    mlflow models serve -m "models:/sarcasm_detector_model/2" -p <puerto> --no-conda
    ```
    Reemplaza <puerto> por el puerto que deseas utilizar para acceder al modelo.

 ### Instrucciones de uso 

**Realizar una Predicción:**
En la misma carpeta de [visualización](../../src/bazinga/visualization/) usar el script deployment.py de la siguiente manera

     python3 deployment.py "<titular>" <puerto>

este dará como resultado lo siguiente

    Prediction: {'predictions': [[<float>,<float>]]}

En donde el primer float representa la probabilidad de que no sea sarcástico, y el segundo de que sea sarcástico

### Instrucciones de Mantenimiento para Usuarios

1. **Actualizar el Repositorio:**
Para obtener las últimas actualizaciones del modelo y del código de la aplicación, asegúrate de tener la última versión del repositorio clonado en tu máquina local:
```
    git pull origin main
```
2. **Instalar las Dependencias Actualizadas:**

Si hay cambios en las dependencias del proyecto, instala las nuevas versiones

3. **Ejecutar la Aplicación:**

Inicia la aplicación localmente para comprobar que todo funcione correctamente con las actualizaciones realizadas.

4. **Reportar Problemas o Bugs (Opcional):**

Si encuentras algún problema o bug durante el uso de la aplicación, repórtalo a los desarrolladores para que puedan solucionarlo en futuras actualizaciones.
