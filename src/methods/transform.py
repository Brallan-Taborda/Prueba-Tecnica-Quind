import time
from pyspark.sql import SparkSession
from utils.logger import logger
from config import ERROR_COUNT
from pyspark.sql.functions import col, regexp_replace, when, length, trim, lit


# Clase para limpiar datos de formato: x299, 29aaa, 2*$#" se excluyen las columnas que no son numericas
class DataCleaner:
    def __init__(self, df):
        self.df = df
        self.columnas_varchar = [
            "first_name", "last_name", "email", "title", "description", "rating", "special_features",
            "customer_id_old", "segment","create_date", "last_update", "rental_date", "return_date"
        ]

    def clean_data(self):
        columnas_a_filtrar = [col_name for col_name in self.df.columns if col_name not in self.columnas_varchar]
        for col_name in columnas_a_filtrar:
            self.df = (
                self.df.withColumn(col_name, regexp_replace(col(col_name), "[^0-9.]", ""))  # Eliminar todo excepto números y punto
                        .withColumn(col_name, when(length(trim(col(col_name))) == 0, lit(0)).otherwise(col(col_name)))
            )
        return self.df

#clase para un filtrado general para toda tabla (eliminar repetidos y dejar no nulos)
class SparkTransformer:
    def __init__(self, spark: SparkSession):
        self.spark = spark

    def transform(self, input_paths):
        start_time = time.time()
        transformed_dfs = {}

        for name, path in input_paths.items():
            try:
                df = self.spark.read.csv(path, header=True, inferSchema=True)
                df = df.toDF(*[col_name.strip() for col_name in df.columns])

                cleaner = DataCleaner(df)
                df = cleaner.clean_data()

                original_count = df.count()
                df = df.dropna().dropDuplicates()
                transformed_count = df.count()

                logger.info(f"🔹 {name}: {original_count} → {transformed_count} registros después de limpieza.")
                transformed_dfs[name] = df
            except Exception as e:
                logger.error(f"Error al transformar {name}: {e}")
                ERROR_COUNT.inc()
                continue

        logger.info(f"🔹 Transformación completada en {time.time() - start_time:.2f} segundos.")
        return transformed_dfs
