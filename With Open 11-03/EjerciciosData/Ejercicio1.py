with open('EjerciciosData\\employees.csv', 'r') as file:
    empleados = [line.strip().split(',') for line in file.readlines()]

print("--" * 40)
print(f"Los empleados son: {empleados}")

# Salarios
salarios = [
    float(empleado[7]) for empleado in empleados[1:] if empleado[7].replace('.', '', 1).isdigit()  
]

print(salarios)
print("--" * 40)
print(f"El salario más alto es: {max(salarios)}")
print(f"El salario más bajo es: {min(salarios)}")

# Departamentos 
departamentos = [
    int(empleado[10]) for empleado in empleados[1:] if empleado[10].isdigit() 
]
print("--" * 40)
print(f"Los departamentos son: {departamentos}")
