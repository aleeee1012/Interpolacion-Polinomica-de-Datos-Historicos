import yfinance as yf # Para descargar datos reales
import numpy as np
import matplotlib.pyplot as plt
import os
from src.interpolacion import polinomio_lagrange

# ----- Configuración ------
ACTIVO = 'DIS'
FECHA_INICIO = '2024-03-01'
FECHA_FIN = '2025-04-01'
CARPETA_GRAFICOS = 'graficos'

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
    if len(precios) < 380:
        print(f"Error: No se descargaron suficientes datos ({len(precios)} días).")
        print("Intenta con un rango de fechas más amplio (FECHA_INICIO).")
        exit()

except Exception as e:
    print(f"Error al descargar datos: {e}")
    exit()


# ----- Pruebas -----
print(f"Iniciando etapa de prueba")
# Analizar los primeros 380 días de datos
N_DIAS_ANALISIS = 380
# 11 puntos para crear polinomio de grado 10
N_PUNTOS_INTERPOLACION = 11

print(f"\nGenerando prueba para el gráfico (Polinomio Grado {N_PUNTOS_INTERPOLACION - 1})...")

# 1.- Seleccionar puntos a interpolar usando linespace
indices_puntos = np.linspace(0, N_DIAS_ANALISIS - 1, N_PUNTOS_INTERPOLACION).astype(int)

x_interp = dias[indices_puntos]
y_interp = precios[indices_puntos]

# 2.- Generar curva del polinomio creando un eje X fino para dibujar la curva
dias_polinomio = np.arrange(0, N_DIAS_ANALISIS)
precios_polinomio = []

# Evaluar polinomio en cada uno de esos dias
for dia in dias_polinomio:
    valor_y = polinomio_lagrange(x_interp, y_interp, dia)
    precios_polinomio.append

print("Datos para el gráfico generados")

# --- Análisis de resultados (Graficar) ---
print(f"Generando gráfico de análisis...")

plt.figure(figsize=(14, 8))

# 1. Graficar TODOS los datos reales (como puntos pequeños)
plt.plot(dias[:N_DIAS_ANALISIS], precios[:N_DIAS_ANALISIS], 'k.', label='Datos Reales (Precio Cierre)', alpha=0.6)

# 2. Graficar los PUNTOS que usamos para interpolar (como círculos rojos)
plt.plot(x_interp, y_interp, 'ro', markersize=10, label=f'Puntos de Interpolación (N={N_PUNTOS_INTERPOLACION})')

# 3. Graficar la CURVA del polinomio resultante
plt.plot(dias_polinomio, precios_polinomio, 'b-', label=f'Polinomio de Lagrange (Grado {N_PUNTOS_INTERPOLACION - 1})')

# Configuración del gráfico
plt.title(f'Interpolación de Lagrange en Precios de {ACTIVO} (Fenómeno de Runge)', fontsize=16)
plt.xlabel('Días', fontsize=12)
plt.ylabel('Precio de Cierre (USD)', fontsize=12)
plt.legend(fontsize=10)
plt.grid(True)

# ¡IMPORTANTE! Ajustar el eje Y para poder ver las oscilaciones
min_visible = np.min(precios[:N_DIAS_ANALISIS]) * 0.9
max_visible = np.max(precios[:N_DIAS_ANALISIS]) * 1.1
plt.ylim(min_visible, max_visible)

# Guardar el gráfico
ruta_salida = os.path.join(CARPETA_GRAFICOS, f'analisis_lagrange_{ACTIVO}_380dias.png')
plt.savefig(ruta_salida)

print(f"¡Análisis completo! Gráfico guardado en: {ruta_salida}")
print("Abre el gráfico para ver los resultados.")
