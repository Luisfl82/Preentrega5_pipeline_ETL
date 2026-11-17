"""Etapa 1 - EXTRACCIÓN: lectura del CSV optimizando memoria con tipos de datos."""
import pandas as pd


def extraer(ruta_csv: str) -> pd.DataFrame:
    """Lee el CSV. Las columnas de texto con pocas categorías se leen como 'category'
    para usar menos memoria."""
    df = pd.read_csv(
        ruta_csv,
        dtype={"Ciudad": "category", "Plan": "category"},
    )
    memoria_mb = df.memory_usage(deep=True).sum() / 1024**2
    print(f"[Extracción] {df.shape[0]} filas, {df.shape[1]} columnas, {memoria_mb:.3f} MB")
    return df
