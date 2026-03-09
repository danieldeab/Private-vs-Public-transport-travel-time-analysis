import pandas as pd
import numpy as np
import glob

# ==========================
# 1. Leer todos los CSV
# ==========================

archivos = glob.glob("*.csv")

df = pd.concat([pd.read_csv(f) for f in archivos], ignore_index=True)

print("Filas originales:", len(df))


# ==========================
# 2. Crear variable minutos por km
# ==========================

df["min_por_km"] = df["duracion_con_trafico_min"] / df["distancia_km"]


# ==========================
# 3. Calcular cuartiles
# ==========================

Q1 = df["min_por_km"].quantile(0.25)
Q3 = df["min_por_km"].quantile(0.75)

IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)


# ==========================
# 4. Filtrar outliers
# ==========================

df_limpio = df[
    (df["min_por_km"] >= limite_inferior) &
    (df["min_por_km"] <= limite_superior)
]

print("Filas después de limpiar:", len(df_limpio))


# ==========================
# 5. Guardar CSV limpio
# ==========================

df_limpio.to_csv("datos_limpios.csv", index=False)

print("Archivo guardado: datos_limpios.csv")