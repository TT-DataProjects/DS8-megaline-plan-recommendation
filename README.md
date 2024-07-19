# Megaline Plan Recommendation

## Descripción

Este proyecto de machine learning está diseñado para ayudar a la compañía móvil Megaline a recomendar planes de servicios a sus clientes. Utilizando datos históricos de comportamiento de los clientes, se entrena un modelo de clasificación para predecir y sugerir uno de los nuevos planes: Smart o Ultra.

## Estructura del Proyecto

```
megaline-plan-recommendation/
│
├── data/
│   ├── users_behavior.csv        # Dataset proporcionado
│   └── processed_data.csv        # Dataset procesado (opcional)
│
├── notebooks/
│   ├── 01_data_exploration.ipynb # Exploración y análisis inicial de los datos
│   ├── 02_data_preprocessing.ipynb # Preprocesamiento de los datos
│   ├── 03_model_training.ipynb   # Entrenamiento y validación de modelos
│   └── 04_model_optimization.ipynb # Optimización de hiperparámetros
│
├── scripts/
│   ├── data_preprocessing.py     # Script para el preprocesamiento de los datos
│   ├── train_model.py            # Script para entrenar el modelo
│   ├── optimize_model.py         # Script para optimizar el modelo
│   └── evaluate_model.py         # Script para evaluar el modelo en el conjunto de prueba
│
├── models/
│   └── best_model.pkl            # Modelo entrenado y optimizado guardado
│
├── reports/
│   ├── model_performance.md      # Informe de rendimiento del modelo
│   └── feature_importance.md     # Informe de importancia de características
│
├── requirements.txt              # Lista de dependencias del proyecto
├── README.md                     # Descripción del proyecto y guía de uso
└── LICENSE                       # Licencia del proyecto

```
## Requisitos

- Python 3.7 o superior
- Bibliotecas listadas en `requirements.txt`

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/megaline-plan-recommendation.git
    cd megaline-plan-recommendation
	```
2. Crea y activa un entorno virtual:
	```bash
    python3 -m venv env
    source env/bin/activate
	```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

### Exploración de Datos

Para explorar y analizar los datos, ejecuta el notebook `01_data_exploration.ipynb` en la carpeta `notebooks`.

### Preprocesamiento de Datos

Ejecuta el notebook `02_data_preprocessing.ipynb` o el script `scripts/data_preprocessing.py` para realizar el preprocesamiento de los datos.

### Entrenamiento del Modelo

Para entrenar el modelo, ejecuta el notebook `03_model_training.ipynb` o el script `scripts/train_model.py`.

### Optimización del Modelo

Ejecuta el notebook `04_model_optimization.ipynb` o el script `scripts/optimize_model.py` para optimizar los hiperparámetros del modelo.

### Evaluación del Modelo

Utiliza el script `scripts/evaluate_model.py` para evaluar el modelo entrenado y optimizado en el conjunto de prueba.

## Informes

Los informes sobre el rendimiento del modelo y la importancia de las características se pueden encontrar en la carpeta `reports`.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para discutir cualquier cambio que te gustaría realizar.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

