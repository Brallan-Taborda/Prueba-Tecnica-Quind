import os
import time
import pandas as pd
from config import REQUEST_TIME, DATA_VOLUME, ERROR_COUNT
from utils.logger import logger

#clase para extraer las hojas validas de un excel y guardarlas en formato csv
class ExcelExtractor:
    def __init__(self, output_format="csv"):
        self.output_format = output_format
        self.output_dir = "data/csv"
        os.makedirs(self.output_dir, exist_ok=True)

    @REQUEST_TIME.time()
    def extract(self, file_path):
        start_time = time.time()
        try:
            sheets_dict = pd.read_excel(file_path, sheet_name=None)
            output_paths = {}

            for sheet_name, df in sheets_dict.items():
                if df.empty or df.dropna(how="all").empty or df.shape[1] < 2:
                    logger.warning(f"✖ Hoja descartada: {sheet_name} (vacía o no estructurada)")
                    ERROR_COUNT.inc()
                    continue

                output_path = os.path.join(self.output_dir, f"{sheet_name}.{self.output_format}")
                df.to_csv(output_path, index=False)
                output_paths[sheet_name] = output_path
                DATA_VOLUME.inc(df.memory_usage(deep=True).sum())
                logger.info(f"✔ Hoja guardada: {sheet_name} → {output_path}")

            logger.info(f"🔹 Extracción completada en {time.time() - start_time:.2f} segundos.")
            return output_paths
        except Exception as e:
            logger.error(f"Error en la extracción: {e}")
            ERROR_COUNT.inc()
            raise
