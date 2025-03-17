import logging
from logging.handlers import SysLogHandler

"""
Configura y devuelve un logger personalizado para el proceso ETL (Extract, Transform, Load).

Este logger registra mensajes en dos destinos:
1. La consola (stdout) para visualización en tiempo de ejecución.
2. Un servidor syslog en 'localhost' en el puerto 514 para almacenamiento centralizado de logs.

El formato de los mensajes incluye la fecha y hora, el nombre del logger, el nivel de severidad y el mensaje.
"""

def setup_logger():
    logger = logging.getLogger("ETL")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    syslog_handler = SysLogHandler(address=('localhost', 514))
    syslog_handler.setFormatter(formatter)
    logger.addHandler(syslog_handler)

    return logger

# Crear logger global
logger = setup_logger()
