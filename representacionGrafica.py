import matplotlib.pyplot as plt
import numpy as np

intervalos = ["[0,10)", "[10,20)", "[20,30)", "[30,45)", "[45,60)", "[60,90)", "[90,120)"]

drive = [39, 462, 435, 85, 24, 49, 22]
transit = [19, 95, 236, 326, 203, 174, 137]

x = np.arange(len(intervalos))
width = 0.35

# -------- GRAFICO DE BARRAS --------
plt.figure()

plt.bar(x - width/2, drive, width, label="DRIVE")
plt.bar(x + width/2, transit, width, label="TRANSIT")

plt.xlabel("Duración del viaje (min)")
plt.ylabel("Frecuencia")
plt.title("Comparación DRIVE vs TRANSIT (Barras)")

plt.xticks(x, intervalos)

max_val = max(max(drive), max(transit))
plt.yticks(np.arange(0, max_val + 50, 50))

plt.legend()
plt.grid(axis="y")

plt.show()


# -------- GRAFICO DE LINEAS --------
plt.figure()

plt.plot(x, drive, marker="o", label="DRIVE")
plt.plot(x, transit, marker="o", label="TRANSIT")

plt.xlabel("Duración del viaje (min)")
plt.ylabel("Frecuencia")
plt.title("Comparación DRIVE vs TRANSIT (Líneas)")

plt.xticks(x, intervalos)
plt.yticks(np.arange(0, max_val + 50, 50))

plt.legend()
plt.grid(True)

plt.show()