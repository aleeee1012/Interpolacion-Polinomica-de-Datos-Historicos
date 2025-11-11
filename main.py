import yfinance as yf # Para descargar datos reales
import numpy as np
import matplotlib.pyplot as plt
import os
from src.interpolacion_lagrange import polinomio_lagrange
from src.interpolacion_newton import polinomio_newton

# ----- Configuración ------
ACTIVO = 'DIS'
FECHA_INICIO = '2024-03-01'
FECHA_FIN = '2025-04-01'
CARPETA_GRAFICOS = 'graficos'

# Variables Análisis
print(f"Iniciando etapa de prueba")
# Analizar los primeros 270 días de datos
N_DIAS_ANALISIS = 270
# 11 puntos para crear polinomio de grado 10
N_PUNTOS_INTERPOLACION = 11

# Asegurarse de que la carpeta 'graficos' exista, crearla de lo contrario

if not os.path.exists(CARPETA_GRAFICOS):
    os.makedirs(CARPETA_GRAFICOS)

# ----- Obtener Datos -----

print(f"Descargando dato para {ACTIVO}...")
try:
    datos = yf.download(ACTIVO, start=FECHA_INICIO, end=FECHA_FIN)
    if datos.empty:
        print(f"No se pudieron descargar datos para el activo {ACTIVO}. Verifica que el ticker sea correcto y no privado.")
        exit()

    precios = datos['Close'].values
    # Crear eje x
    dias = np.arange(len(precios))
    print("Datos descargados exitosamente.")


# Verificar que tenemos suficientes datos
    if len(precios) < 270:
        print(f"Error: No se descargaron suficientes datos ({len(precios)} días).")
        print("Intenta con un rango de fechas más amplio (FECHA_INICIO).")
        exit()

except Exception as e:
    print(f"Error al descargar datos: {e}")
    exit()


# ----- Pruebas -----
print(f"\nGenerando prueba para el gráfico (Polinomio Grado {N_PUNTOS_INTERPOLACION - 1})...")

# 1.- Seleccionar puntos a interpolar usando linespace
indices_puntos = np.linspace(0, N_DIAS_ANALISIS - 1, N_PUNTOS_INTERPOLACION).astype(int)

x_interp = dias[indices_puntos]
y_interp = precios[indices_puntos]

# 2.- Generar curva del polinomio creando un eje X fino para dibujar la curva
dias_polinomio = np.arange(0, N_DIAS_ANALISIS)
precios_polinomio_lagrange = []
precios_polinomio_newton = []

# Evaluar polinomio en cada uno de esos dias
for dia in dias_polinomio:
    valor_y_lagrange = polinomio_lagrange(x_interp, y_interp, dia)
    valor_y_newton = polinomio_newton(x_interp, y_interp, dia)
    
    precios_polinomio_lagrange.append(valor_y_lagrange)
    precios_polinomio_newton.append(valor_y_newton)

print("Datos para los gráficos generados")

# --- Análisis de resultados (Graficar) ---
print(f"Generando gráficos de análisis...")

plt.figure(figsize=(14, 8))
plt.plot(dias[:N_DIAS_ANALISIS], precios[:N_DIAS_ANALISIS], 'k.', label='Datos Reales (Precio Cierre)', alpha=0.6)
plt.plot(x_interp, y_interp, 'ro', markersize=10, label=f'Puntos de Interpolación (N={N_PUNTOS_INTERPOLACION})')

plt.plot(dias_polinomio, precios_polinomio_lagrange, 'b-', label=f'Polinomio de Lagrange (Grado {N_PUNTOS_INTERPOLACION - 1})')
plt.plot(dias_polinomio, precios_polinomio_newton, color='orange', linestyle='--', linewidth=2, label=f'Polinomio de Newton (Grado {N_PUNTOS_INTERPOLACION - 1})')

plt.title(f'Comparación Lagrange vs Newton en Precios de {ACTIVO}', fontsize=16)
plt.xlabel('Días', fontsize=12)
plt.ylabel('Precio de Cierre (USD)', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True)

min_visible = np.min(precios[:N_DIAS_ANALISIS]) * 0.9
max_visible = np.max(precios[:N_DIAS_ANALISIS]) * 1.1
plt.ylim(min_visible, max_visible)

# Guardar el gráfico
ruta_salida = os.path.join(CARPETA_GRAFICOS, f'analisis_comparacion_L_vs_N_{ACTIVO}.png')
plt.savefig(ruta_salida)

print(f"¡Análisis completo! Gráfico guardado en: {ruta_salida}")
print("Abre el gráfico para ver los resultados.")
