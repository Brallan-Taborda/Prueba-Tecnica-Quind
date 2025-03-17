from prometheus_client import start_http_server, Summary, Counter

# Métricas Prometheus
REQUEST_TIME = Summary('request_processing_seconds', 'Tiempo de procesamiento')
DATA_VOLUME = Counter('data_volume_bytes', 'Volumen de datos procesados')
ERROR_COUNT = Counter('error_count', 'Errores durante el ETL')

# Iniciar servidor Prometheus
start_http_server(8000)