with open('Ejercicios\employees.csv', 'r') as file:
    empleados = [line.strip().split(',') for line in file.readlines()]

print("--" * 40)
#print(f"Los datos son: {empleados}")

# Salarios
def obtener_salarios(empleados):
    salarios = [
        float(empleado[7]) for empleado in empleados[1:]
        if empleado[7].replace('.', '', 1).isdigit()
    ]
    return salarios
salarios = obtener_salarios(empleados)
print(salarios)
print("--" * 40)
print(f"El salario más alto es: {max(salarios)}")
print(f"El salario más bajo es: {min(salarios)}")


""""
# Departamentos 
departamentos = [
    int(empleado[10]) for empleado in empleados[1:] if empleado[10].isdigit() 
    ]
print("--" * 40)
print(f"Los departamentos son: {departamentos}")

#def obtener_deptos(empleados):"""