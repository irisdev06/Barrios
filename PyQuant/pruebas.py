from ciclos.ciclos import invertir_numero 
from condicionales.condicionales import valor_del_medio 
from estadísticas.estadisticas import promedio 
from listas.listas import mediana 
"""
print(valor_del_medio(1, 2, 3))
invertir = invertir_numero()
print(invertir)
print(promedio(1, 2))
med = mediana([1, 3, 5, 7, 9])
print(med)
"""
# Menú Divalopers
sel = 0
while sel != 5:
    print("\nMenú Divalopers. Escoja su Receta del Día de Hoy: ")
    print("1 - Valor del Medio")
    print("2 - Invertir Número")
    print("3 - Promedio de dos números")
    print("4 - Mediana de una lista de números")
    print("5 - Salir")

    # Opciones
    sel = int(input("Seleccione opción: "))

    if sel == 1:
        # Valor del medio
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        num3 = int(input("Ingrese el tercer número: "))
        print("--"*20)
        print(f"El valor del medio es: {valor_del_medio(num1, num2, num3)}")

    elif sel == 2:
        # Invertir número
        print("--"*20)
        print(invertir_numero())

    elif sel == 3:
        # Promedio
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print("--"*20)
        print(f"Promedio: {promedio(num1, num2)}")

    elif sel == 4:
        # Mediana
        lista = list(map(int, input("Ingrese una lista de números separados por espacio: ").split()))
        print("--"*20)
        print(f"Mediana: {mediana(lista)}")

    elif sel == 5:
        print("¡Hasta luego!")
    else:
        print("Opción inválida. Por favor, intente nuevamente.")
