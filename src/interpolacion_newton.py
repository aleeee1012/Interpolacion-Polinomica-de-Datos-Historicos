import numpy as np

def calcular_coeficientes_newton(x_puntos, y_puntos):
    """
    Calcula los coeficientes (b0, b1, b2, ...) para el polinomio
    de Newton usando la tabla de diferencias divididas.
    """
    n = len(x_puntos)
    
    # Creamos 'copia' de los y_puntos para no modificar el original. Se irá actualizando para contener las diferencias divididas
    coef = np.copy(y_puntos)

    # El bucle externo 'j' representa la columna de la tabla (Diferencia 1, Dif 2, ...)
    for j in range(1, n):
        # El bucle interno 'i' calcula cada valor en esa columna. Va de atrás hacia adelante para no sobrescribir valores necesarios
        for i in range(n - 1, j - 1, -1):
            # Fórmula de la diferencia dividida:
            coef[i] = (coef[i] - coef[i - 1]) / (x_puntos[i] - x_puntos[i - j])
            
    # Los coeficientes finales son la diagonal de la tabla, que después quedan almacenados en 'coef'
    return coef

def polinomio_newton(x_puntos, y_puntos, x_eval):
    """
    Calcula el valor del polinomio de interpolación de Newton
    en un punto específico 'x_eval'.
    """
    
    # 1. Obtener los coeficientes (b0, b1, b2, ...)
    coeficientes = calcular_coeficientes_newton(x_puntos, y_puntos)
    
    n = len(x_puntos)
    resultado = 0.0

    # 2. Evaluar el polinomio usando la forma anidada (Método de Horner)
    for i in range(n - 1, -1, -1): # Bucle de n-1 hasta 0
        resultado = resultado * (x_eval - x_puntos[i]) + coeficientes[i]
        
    return resultado