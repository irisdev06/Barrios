import json

with open("Empleados\employees.json", "r") as archivo:
    datos = json.load(archivo)
    

salarios = [int(sa["SALARY"]) for sa in datos]
print(salarios)

# Determinar el promedio salarial del archivo.
def promedio():
    return sum(salarios) / len(salarios)

promediando = promedio()
print(f"El promedio de los salarios es: {promediando}")



id = [x ["DEPARTMENT_ID"]for x in datos if x == 50]
print(id)