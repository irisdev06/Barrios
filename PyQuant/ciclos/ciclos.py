# 1. Determinar los divisores de un número introducido por teclado
def divisores(numero):
    divisores_lista = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores_lista.append(i)
    return divisores_lista


# 2. Determinar si un número es o no es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


# 3. Determinar si un número es perfecto
def es_perfecto(numero):
    divisores_lista = divisores(numero)
    divisores_lista.remove(numero)  # No se incluye el número en sí mismo
    return sum(divisores_lista) == numero


# 4. Determinar cuáles y cuántos números perfectos hay entre 1 y 1000
def numeros_perfectos():
    perfectos = []
    for num in range(1, 1001):
        if es_perfecto(num):
            perfectos.append(num)
    return perfectos, len(perfectos)


# 5. ¿Cuáles y cuántos son los números primos comprendidos entre 1 y 1000?
def numeros_primos():
    primos = []
    for num in range(2, 1001):
        if es_primo(num):
            primos.append(num)
    return primos, len(primos)


# 6. Calcular el máximo de números positivos introducidos por teclado hasta introducir uno negativo
def maximo_positivo():
    max_num = None
    while True:
        num = int(input("Introduce un número positivo (o negativo para terminar): "))
        if num < 0:
            break
        if max_num is None or num > max_num:
            max_num = num
    return max_num


# 7. Encontrar un número natural n más pequeño tal que la suma de los n primeros números naturales
def suma_excede_maximo(maximo):
    suma = 0
    n = 0
    while suma <= maximo:
        n += 1
        suma += n
    return n


# 8. Determinar cuáles son los múltiplos de 5 comprendidos entre 1 y N
def multiplos_de_5(N):
    multiplos = []
    for i in range(1, N + 1):
        if i % 5 == 0:
            multiplos.append(i)
    return multiplos


# 9. Calcular la operación x^n sin utilizar la función pow
def potencia(x, n):
    resultado = 1
    for _ in range(n):
        resultado *= x
    return resultado


# 10. Algoritmo para hallar el m.c.d de dos números m y n por el algoritmo de Euclides
def mcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m


# 11. Solicitar 2 números al usuario e imprimir el cociente y el residuo del mayor en el menor sin utilizar la división ni el mod
def cociente_residuo():
    m = int(input("Introduce el primer número: "))
    n = int(input("Introduce el segundo número: "))
    
    if m < n:
        m, n = n, m  # Asegurarse de que m sea el mayor
    
    cociente = 0
    while m >= n:
        m -= n
        cociente += 1
    
    residuo = m
    return cociente, residuo


# 12. Escribir un programa que visualice la siguiente figura utilizando ciclos
def visualiza_figura():
    lineas = int(input("Introduce cuántas líneas quieres imprimir: "))
    for i in range(1, lineas + 1):
        print('* ' * i)


# 13. Solicitar al usuario un número de hasta 9 dígitos e imprimirlo en orden contrario
def invertir_numero():
    numero = input("Introduce un número de hasta 9 dígitos: ")
    if len(numero) > 9:
        return "Número fuera de los límites"
    return numero[::-1]


# 14. Calcular todos los números de 3 cifras tales que la suma de los cubos de las cifras es igual al valor del número
def numeros_armstrong():
    armstrong = []
    for num in range(100, 1000):
        centenas = num // 100
        decenas = (num // 10) % 10
        unidades = num % 10
        if num == (centenas**3 + decenas**3 + unidades**3):
            armstrong.append(num)
    return armstrong


# 15. Diseñar e implementar un programa que visualice una salida específica
def visualizar_salida(n):
    for i in range(n, 0, -1):
        print(' '.join(str(x) for x in range(1, i + 1)))

