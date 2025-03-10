import random

def llenar_arreglo(n):
    return [random.randint(1, 100) for _ in range(n)]

def imprimir_arreglo(arreglo):
    print("Arreglo original:", arreglo)

def suma(arreglo):
    return sum(arreglo)

def promedio(arreglo):
    return sum(arreglo) / len(arreglo)

def mayor(arreglo):
    return max(arreglo)

def menor(arreglo):
    return min(arreglo)

def ordenar_ascendente(arreglo):
    return sorted(arreglo)

def ordenar_descendente(arreglo):
    return sorted(arreglo, reverse=True)

def moda(arreglo):
    from collections import Counter
    contador = Counter(arreglo)
    max_freq = max(contador.values())
    return [key for key, value in contador.items() if value == max_freq]

def mediana(arreglo):
    arreglo_ordenado = sorted(arreglo)
    n = len(arreglo_ordenado)
    if n % 2 == 1:
        return arreglo_ordenado[n // 2]
    else:
        return (arreglo_ordenado[n // 2 - 1] + arreglo_ordenado[n // 2]) / 2

def buscar(arreglo, numero):
    posiciones = [i for i, x in enumerate(arreglo) if x == numero]
    if posiciones:
        return f"Encontrado en posiciones: {posiciones}, se repite {len(posiciones)} veces."
    return "No encontrado."
