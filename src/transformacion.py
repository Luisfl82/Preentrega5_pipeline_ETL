"""Etapa 2 - TRANSFORMACIÓN: limpieza modular (cada paso es una función independiente)."""
import pandas as pd


def normalizar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    """Nombres en minúscula, sin espacios en los bordes y con guion bajo."""
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)
    return df


def eliminar_duplicados(df: pd.DataFrame) -> pd.DataFrame:
    antes = len(df)
    df = df.drop_duplicates().reset_index(drop=True)
    print(f"[Transformación] Duplicados eliminados: {antes - len(df)}")
    return df


def tratar_nulos(df: pd.DataFrame) -> pd.DataFrame:
    """Imputación justificada:
    - Numéricas: mediana (no la distorsionan los valores extremos).
    - Categóricas: 'Desconocido' (no inventamos una ciudad que no sabemos)."""
    df = df.copy()
    for col in df.select_dtypes(include="number").columns:
        nulos = df[col].isna().sum()
        if nulos:
            df[col] = df[col].fillna(df[col].median())
            print(f"[Transformación] '{col}': {nulos} nulos imputados con la mediana")
    for col in df.select_dtypes(include=["object", "category"]).columns:
        nulos = df[col].isna().sum()
        if nulos:
            if str(df[col].dtype) == "category":
                df[col] = df[col].cat.add_categories("Desconocido")
            df[col] = df[col].fillna("Desconocido")
            print(f"[Transformación] '{col}': {nulos} nulos imputados con 'Desconocido'")
    return df


def limpiar(df: pd.DataFrame) -> pd.DataFrame:
    """Función de limpieza completa: encadena los pasos anteriores."""
    df = normalizar_columnas(df)
    df = eliminar_duplicados(df)
    df = tratar_nulos(df)
    return df
