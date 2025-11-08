# 📈 Proyecto de Métodos Numéricos: Interpolación Polinómica de Datos Históricos

## 1. Descripción del Proyecto

En este proyecto para el curso de Métodos Numéricos, seleccionamos un método de la unidad de **Ajuste de Curvas** para aplicarlo a un problema del mundo real. El objetivo es aplicar los conocimientos teóricos para resolver un problema usando técnicas computacionales.

* **Método Seleccionado:** Interpolación Polinómica (implementando el Polinomio de Lagrange).
* **Problema Real:** Analizar el comportamiento de los precios históricos de una acción, tratando los datos como un conjunto de puntos (día, precio).

## 2. El Problema: Interpolación de Puntos de Datos

El objetivo es construir un modelo matemático (un polinomio) que pase exactamente por un conjunto de puntos de datos históricos.

Usaremos `N+1` puntos (días) de los datos de una acción para construir un polinomio de interpolación de grado `N`. Luego, analizaremos visualmente qué tan bien este polinomio describe la tendencia general de los datos, o si sufre de oscilaciones no deseadas (Fenómeno de Runge).

**Este proyecto NO busca predecir el futuro**, sino analizar críticamente las propiedades matemáticas y las limitaciones de la interpolación polinómica cuando se aplica a datos con variaciones.

## 3. Instalación y Dependencias

Para ejecutar este proyecto, necesitas Python 3.x y las siguientes bibliotecas. Puedes instalarlas usando `pip`:

```bash
pip install -r requirements.txt