# Preentrega 5 - Pipeline de ingesta y limpieza (ETL)

Pipeline modular en Python/pandas: **Extrae** un CSV, lo **Transforma** (limpieza) y lo **Carga** en formato Parquet.

## Estructura
```
main.py                  -> ejecuta el pipeline completo
src/extraccion.py        -> lee el CSV optimizando tipos de datos
src/transformacion.py    -> normaliza columnas, quita duplicados, trata nulos
src/carga.py             -> exporta a Parquet
generar_dataset_ejemplo.py -> crea un dataset de ejemplo (data/dataset_crudo.csv)
requirements.txt
```

## Cómo ejecutarlo
1. `pip install -r requirements.txt`
2. Crear el dataset de ejemplo: `python generar_dataset_ejemplo.py`
   (o poner tu propio CSV de Kaggle en `data/dataset_crudo.csv`)
3. `python main.py`
4. El resultado queda en `output/dataset_limpio.parquet`

## Etapas del pipeline
1. **Extracción:** `pd.read_csv` con `dtype="category"` en columnas con pocas categorías para ahorrar memoria.
2. **Transformación** (funciones independientes):
   - `normalizar_columnas`: minúsculas, sin espacios, con `_`.
   - `eliminar_duplicados`.
   - `tratar_nulos`: numéricas con la **mediana** (resistente a valores extremos); categóricas con `"Desconocido"` (no se inventan datos).
3. **Carga:** Parquet, porque es columnar, comprimido, conserva los tipos de datos y se lee mucho más rápido que un CSV, lo que acelera el entrenamiento de modelos de Machine Learning.

## Notas
- El dataset original **no** se sube al repositorio (ver `.gitignore`).
