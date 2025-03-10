# 1. Promedio (Media)
def promedio(a, b):
    return (a + b) / 2

# 2. Varianza
def varianza(a, b):
    mu = promedio(a, b)  # media de los dos números
    return ((a - mu) ** 2 + (b - mu) ** 2) / 2  # fórmula de varianza

# 3. Desviación estándar
def desviacion_estandar(a, b):
    # Calculamos la raíz cuadrada de la varianza sin usar math.sqrt
    var = varianza(a, b)
    raiz = 0
    # Estimación de la raíz cuadrada usando el método de aproximación
    for i in range(1, int(var) + 1):
        if i * i == var:
            raiz = i
            break
        elif i * i > var:
            raiz = i - 1
            break
    return raiz

# 4. Rango
def rango(a, b):
    # Calculamos el rango sin usar abs
    if a > b:
        return a - b
    else:
        return b - a

# 5. Mediana
def mediana(a, b):
    return promedio(a, b)  # para dos números, la mediana es el promedio
