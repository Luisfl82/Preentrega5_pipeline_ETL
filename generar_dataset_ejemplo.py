"""Crea un CSV de ejemplo con duplicados, nulos y nombres de columnas desprolijos."""
import numpy as np
import pandas as pd

rng = np.random.default_rng(7)
n = 500
df = pd.DataFrame({
    "ID Cliente": np.arange(1, n + 1),
    "Edad ": rng.integers(18, 80, n).astype(float),
    "Ciudad": rng.choice(["La Plata", "CABA", "Rosario", None], n, p=[0.35, 0.35, 0.25, 0.05]),
    "Gasto Mensual": rng.normal(15000, 4000, n).round(2),
    "Plan": rng.choice(["Basico", "Premium", "Full"], n),
})
df.loc[rng.choice(n, 25, replace=False), "Edad "] = np.nan
df.loc[rng.choice(n, 15, replace=False), "Gasto Mensual"] = np.nan
df = pd.concat([df, df.sample(20, random_state=1)], ignore_index=True)  # duplicados
df.to_csv("data/dataset_crudo.csv", index=False)
print("Creado data/dataset_crudo.csv")
