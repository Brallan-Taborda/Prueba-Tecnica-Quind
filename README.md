<h1>Programa de generación de facturas de comisiones </h1>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de Contenido</summary>
  <ol>
    <li>
      <a href="#about-the-project">Acerca del proyecto </a>
      <ul>
        <li><a href="#built-with">Tecnologías implementadas</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Configuraciones Iniciales</a>
      <ul>
        <li><a href="#prerequisites">Prerequisitos</a></li>
        <li><a href="#installation">Instalaciones</a></li>
      </ul>
    </li>   
    <li><a href="#contact">Autores</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## Acerca del Proyecto

El siguiente proyecto implementa una aplicación escalable y modular para gestionar y ejecutar procesos de ETL (Extract, Transform, Load) utilizando **Python 3.12** como lenguaje de programación y **Apache Spark 3.5.5** como framework de procesamiento de datos. El objetivo es proporcionar una solución robusta, eficiente y observable para el manejo de grandes volúmenes de datos, siguiendo las mejores prácticas de programación orientada a objetos (POO) y principios SOLID.

## Tecnologías Implementadas

<div align="center">
    <code><img width="50" src="https://user-images.githubusercontent.com/25181517/192108374-8da61ba1-99ec-41d7-80b8-fb2f7c0a4948.png" alt="GitHub" title="GitHub"/></code>
    <code><img width="50" src="https://w7.pngwing.com/pngs/585/822/png-transparent-python-scalable-graphics-logo-javascript-creative-dimensional-code-angle-text-rectangle-thumbnail.png" alt="Python" title="Python"/></code>
    <code><img width="50" src="https://w7.pngwing.com/pngs/1/687/png-transparent-apache-spark-apache-http-server-scala-apache-software-foundation-data-processing-others-miscellaneous-text-orange.png" alt="Apache Spark" title="Apache Spark"/></code>
</div>

---

<!-- GETTING STARTED -->
## Configuraciones Iniciales

Para poner en funcionamiento una copia local, siga estos sencillos pasos de ejemplo.

### Prerrequisitos

Asegúrese de tener instalados los siguientes programas y herramientas:

1. **Java Development Kit (JDK)**  
   Se recomienda usar una versión compatible de Java (JDK 8, JDK 11 o JDK 17).  
   Descargue JDK desde: [https://adoptium.net/es/](https://adoptium.net/es/)

2. **Apache Spark 3.5.5**  
   Descargue la versión 3.5.5 de Spark desde:  
   [https://spark.apache.org/downloads.html](https://spark.apache.org/downloads.html)

3. **Apache Hadoop**  
   Hadoop es necesario para el manejo de sistemas de archivos distribuidos (HDFS).  
   Descargue Hadoop desde: [https://hadoop.apache.org/releases.html](https://hadoop.apache.org/releases.html)

4. **Python 3.12**  
   Asegúrese de tener Python 3.12 instalado.  
   Descargue Python desde: [https://www.python.org/downloads/](https://www.python.org/downloads/)

5. **Gestor de Dependencias (Opcional)**  
   Se recomienda usar un gestor de dependencias como `pip` o `poetry` para manejar las bibliotecas de Python.

---

### Instalaciones

Realizar las siguientes instalaciones necesarias.

1. Clonar el repositorio
   ```sh
   git clone https://github.com/Brallan-Taborda/Prueba-Tecnica-Quind.git
   ```
   
2. Abrir la terminal del sistema operativo e ingresar a la dirrección de la carpeta del proyecto para instalar los requerimientos:
   ```sh
    pip install -r requirements.txt
   ```
2. Ingresar a la carpeta src, en mi caso es:
   ```sh
   C:\Users\Brallan\Desktop\Prueba_Tecnica_Brallan\src
   ```

4. Ejecutar el siguiente comando para inicializar el programa
   ```sh
   python main.py
   ```
5. Esto creará, dentro de la carpeta `src`, una nueva carpeta llamada `data` y, dentro de esta, se establecerán dos subcarpetas:  

- **`csv_raw`**: Aquí se almacenará un archivo `.csv` por cada hoja del archivo de Excel **"Films_2.xlsx"**, conteniendo los datos extraídos sin procesar.  
- **`processed_data`**: En esta carpeta se guardarán los archivos procesados en formato `.parquet`, ya depurados (sin duplicados, sin errores tipográficos y sin valores NaN), correspondientes a cada hoja del archivo de Excel.  

Estos archivos procesados se utilizarán para el análisis exploratorio de datos, cuyos resultados se encuentran en la carpeta **`Data_Analysis`**.




## Justificación del Diseño

### Estructura del Proyecto

```plaintext
proyecto_etl/
├── Data_Analysis/            # Análisis de datos (tablas, visualizaciones, etc.)
├── Informe/                  # Documentación relacionada con el informe
├── src/                      # Código fuente de la aplicación
│   ├── data/                 # Datos generados o utilizados por la aplicación
│   ├── logs/                 # Registros de la aplicación
│   ├── methods/              # Métodos principales para la manipulación de datos
│   │   ├── extract.py        # Lógica de extracción de datos
│   │   ├── load.py           # Lógica de carga de datos
│   │   └── transform.py      # Lógica de transformación de datos
│   ├── utils/                # Utilidades adicionales
│   │   ├── logger.py         # Módulo de observabilidad (logging)
│   │   ├── metric.py         # Métricas de la aplicación
│   │   └── config.py         # Configuraciones de la aplicación
│   └── main.py               # Punto de entrada de la aplicación
├── Films_2 .xlsx              # Archivo de datos utilizado en el proyecto
├── README.md                 # Documentación general del proyecto
└── requirements.txt          # Dependencias del proyecto
```



### Decisiones de Diseño

1. **Modularidad**:
   - El proyecto está dividido en módulos (`extract`, `transform`, `load`) para facilitar la escalabilidad y el mantenimiento. Cada módulo tiene una responsabilidad clara, lo que sigue el principio de **Single Responsibility** (SOLID).

2. **Observabilidad**:
   - Se implementó un módulo de logging (`logger.py`) para monitorear el comportamiento de la aplicación en tiempo real. Esto permite detectar y solucionar errores de manera más eficiente.

3. **Escalabilidad**:
   - El uso de **Apache Spark** permite procesar grandes volúmenes de datos de manera distribuida, lo que hace que la aplicación sea escalable y eficiente.

4. **Principios SOLID**:
   - Se aplicaron los principios de diseño SOLID para garantizar un código limpio, mantenible y extensible. Por ejemplo:
     - **Single Responsibility**: Cada módulo tiene una única responsabilidad.
     - **Open/Closed Principle**: El diseño permite extender la funcionalidad sin modificar el código existente.
     - **Dependency Inversion**: Los módulos dependen de abstracciones, no de implementaciones concretas.

5. **Uso de Python y Spark**:
   - **Python** fue elegido por su simplicidad y amplia adopción en el ámbito de la ciencia de datos.
   - **Apache Spark** fue seleccionado por su capacidad para procesar grandes volúmenes de datos de manera distribuida y su integración con Python a través de PySpark.


## Posibles mejoras

 - Se pueden añadir más clases en extract.py para trabajar con diferentes archivos (.csv, .JSON, etc).
 - Se puede hacer un seleccionador que pregunte antes de empezar en que formato se requieren los datos procesados.


## Desarrolladores

Brallan Taborda: [https://github.com/Brallan-Taborda](https://github.com/Brallan-Taborda)
