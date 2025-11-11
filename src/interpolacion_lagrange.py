"""
Implementación de Lagrange: calcula el valor del polinomio en un punto x_eval

Argumentos:
x_puntos -- (array) Coordenadas 'x' de los puntos conocidos.
y_puntos -- (array) Coordenadas 'y' de los puntos conocidos.
x_eval -- (float o int) El punto 'x' donde se quiere evaluar el polinomio.

Retorna:
float -- El valor 'y' del polinomio evaluado en 'x_eval'.
"""

import numpy as np

def polinomio_lagrange(x_puntos, y_puntos, x_eval):
    """
    Calcula el valor del polinomio de interpolación de Lagrange
    en un punto específico 'x_eval'.
    """
    
    # N es el número de puntos que estamos usando
    N = len(x_puntos)
    
    # P_x es el resultado final (el Yp). Lo iniciamos en 0.0
    P_x = 0.0
    
    # Bucle: Recorre cada punto (i) para calcular y_i * L_i(x)
    for i in range(N):
        
        # 'L_i' es el polinomio base de Lagrange. Lo iniciamos en 1.0
        L_i = 1.0
        
        # Bucle: Calcula el producto (Π) para el L_i(x) actual
        for j in range(N):
            
            # La fórmula dice que j debe ser diferente de i
            if i != j:
                termino = (x_eval - x_puntos[j]) / (x_puntos[i] - x_puntos[j])
                L_i = L_i * termino
        
        # Sumamos el término y_i * L_i(x) al total
        P_x = P_x + y_puntos[i] * L_i
        
    return P_x