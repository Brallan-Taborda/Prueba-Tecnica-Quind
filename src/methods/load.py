import os
import shutil
import logging

#clase para guardar los datos en formato .parquet
class DataLoader:
    def __init__(self, output_dir=None):
        # Guardar en `src/data/processed_data/`
        base_dir = os.path.dirname(__file__)  # Directorio actual (methods/)
        self.output_dir = output_dir if output_dir else os.path.join(base_dir, "../data/processed_data")
        os.makedirs(self.output_dir, exist_ok=True)

    def load(self, transformed_dfs):
        for sheet_name, df in transformed_dfs.items():
            sheet_output_dir = os.path.join(self.output_dir, sheet_name)
            temp_path = sheet_output_dir + "_temp"

            # Guardar en formato Parquet en un directorio temporal
            df.coalesce(1).write.parquet(temp_path, mode="overwrite")

            # Renombrar el archivo Parquet resultante
            self.rename_parquet(temp_path, sheet_output_dir, sheet_name)

    def rename_parquet(self, temp_path, output_path, sheet_name):
        try:
            for file in os.listdir(temp_path):
                if file.endswith(".parquet"):
                    final_path = os.path.join(self.output_dir, f"{sheet_name}.parquet")
                    shutil.move(os.path.join(temp_path, file), final_path)
                    break

            # Eliminar el directorio temporal
            shutil.rmtree(temp_path)

            logging.info(f"✔ Archivo {sheet_name}.parquet guardado en {self.output_dir}")
        except Exception as e:
            logging.error(f"Error al renombrar {sheet_name}: {e}")
