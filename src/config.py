import os
from pyspark.sql import SparkSession
from prometheus_client import start_http_server, Summary, Counter

# 🔹 Métricas Prometheus (para los reportes)
REQUEST_TIME = Summary('request_processing_seconds', 'Tiempo de procesamiento')
DATA_VOLUME = Counter('data_volume_bytes', 'Volumen de datos procesados')
ERROR_COUNT = Counter('error_count', 'Errores durante el ETL')

# 🔹 Iniciar servidor Prometheus
start_http_server(8000)

# 🔹 Configuración de Spark
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

spark = SparkSession.builder \
    .appName("ETL") \
    .config("spark.driver.memory", "2g") \
    .config("spark.eventLog.enabled", "true") \
    .config("spark.eventLog.dir", logs_dir) \
    .getOrCreate()
