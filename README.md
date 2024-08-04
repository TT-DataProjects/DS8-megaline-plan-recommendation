# Megaline Data Analysis Project

## Descripción General

Este proyecto se centra en el análisis de datos de los usuarios del servicio de telecomunicaciones Megaline. El objetivo principal es identificar patrones en el uso de los servicios y las diferencias en los ingresos entre diferentes regiones. El análisis incluye la limpieza de datos, el análisis exploratorio de datos y la aplicación de pruebas estadísticas para validar las hipótesis.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

```
├───notebooks
│   ├───1-data_wrangling.ipynb
│   └───2-data_analysis.ipynb
├───doc
│   └───Descripcion del proyecto.md
├───data
│   ├───clean
│   ├───raw
│   ├───interim
│   └───data_url.json
├───megaline
│   ├───__init__.py
│   └───data_processing.py
├───environment.yml
├───.gitignore
└───.idea
    └───inspectionProfiles
```

### Descripción de las Carpetas y Archivos

- **notebooks**: Contiene los notebooks de Jupyter utilizados para la limpieza y el análisis de datos.
    - `1-data_wrangling.ipynb`: Notebook para la limpieza y transformación de los datos.
    - `2-data_analysis.ipynb`: Notebook para el análisis exploratorio de datos y la aplicación de pruebas estadísticas.

- **doc**: Documentación del proyecto.
    - `Descripcion del proyecto.md`: Documento que describe el objetivo y el alcance del proyecto.

- **data**: Contiene los datos en diferentes etapas del proceso.
    - `clean`: Datos limpios y procesados.
    - `raw`: Datos crudos sin procesar.
    - `interim`: Datos en etapas intermedias de procesamiento.
    - `data_url.json`: Archivo JSON que contiene las URL de los datos utilizados.

- **megaline**: Módulo Python con scripts de procesamiento de datos.
    - `__init__.py`: Archivo de inicialización del módulo.
    - `data_processing.py`: Script con funciones para el procesamiento de datos.

- **environment.yml**: Archivo de configuración de Conda que especifica las dependencias del entorno del proyecto.

- **.gitignore**: Archivo que especifica los archivos y directorios que deben ser ignorados por Git.

- **.idea**: Directorio de configuración de PyCharm.
    - `inspectionProfiles`: Perfiles de inspección de código.

## Configuración del Entorno

Para configurar el entorno de este proyecto, sigue estos pasos:

1. Clona el repositorio:

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd megaline
    ```

2. Crea y activa el entorno Conda:

    ```bash
    conda env create -f environment.yml
    conda activate megaline
    ```

3. Ejecuta los notebooks de Jupyter en la carpeta `notebooks` para realizar la limpieza y análisis de los datos.

## Contribuciones

Las contribuciones a este proyecto son bienvenidas. Para contribuir, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una rama con tu nueva funcionalidad o corrección de errores (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -am 'Agrega nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Crea un nuevo Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto

Para cualquier duda o consulta sobre este proyecto, por favor contacta a:

- Nombre: Guillermo Alcantara
- Discord: guillermoalcantara_26959