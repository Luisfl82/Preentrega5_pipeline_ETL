"""Etapa 3 - CARGA: exporta el resultado a Parquet."""
import os

import pandas as pd


def cargar(df: pd.DataFrame, ruta_salida: str) -> None:
    """Guarda en Parquet. ¿Por qué Parquet para Machine Learning?
    - Es columnar: lee solo las columnas que se necesitan.
    - Está comprimido: pesa mucho menos que un CSV.
    - Guarda los tipos de datos (fechas, categorías), no hay que reconvertirlos.
    - Es mucho más rápido de leer en pandas, Spark, DuckDB, etc."""
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    df.to_parquet(ruta_salida, index=False)
    print(f"[Carga] Guardado en {ruta_salida} ({len(df)} filas)")
