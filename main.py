"""Preentrega 5 - Pipeline ETL modular. Ejecutar con: python main.py"""
from src.extraccion import extraer
from src.transformacion import limpiar
from src.carga import cargar

RUTA_ENTRADA = "data/dataset_crudo.csv"
RUTA_SALIDA = "output/dataset_limpio.parquet"


def main():
    df = extraer(RUTA_ENTRADA)
    df = limpiar(df)
    cargar(df, RUTA_SALIDA)
    print("Pipeline terminado OK")


if __name__ == "__main__":
    main()
