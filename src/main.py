from config import spark
from methods.extract import ExcelExtractor
from methods.transform import SparkTransformer
from methods.load import DataLoader
from utils.logger import logger

def main():
    file_path = "../Films_2 .xlsx"
    logger.info("Iniciando ETL...")

    extractor = ExcelExtractor()
    transformer = SparkTransformer(spark)
    loader = DataLoader()

    extracted_data = extractor.extract(file_path)
    transformed_data = transformer.transform(extracted_data)
    loader.load(transformed_data)

    logger.info("ETL finalizado correctamente.")
    spark.stop()
    logger.info("Spark detenido.")

if __name__ == "__main__":
    main()
