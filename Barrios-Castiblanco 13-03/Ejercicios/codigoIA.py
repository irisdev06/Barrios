# Leer las primeras líneas del archivo CSV para entender su estructura
file_path = "Ejercicios\employees.csv"

with open(file_path, "r", encoding="utf-8") as file:
    header = file.readline().strip()  # Leer la primera línea como encabezado
    first_lines = [file.readline().strip() for _ in range(5)]  # Leer algunas líneas para ver la estructura

header, first_lines
# Leer el archivo y almacenar los datos en una lista de diccionarios
employees = []

with open(file_path, "r", encoding="utf-8") as file:
    headers = file.readline().strip().split(",")  # Leer encabezados
    for line in file:
        values = line.strip().split(",")
        employee = dict(zip(headers, values))
        employees.append(employee)

# Convertir SALARY a número y manejar valores vacíos
for emp in employees:
    emp["SALARY"] = int(emp["SALARY"]) if emp["SALARY"].strip().isdigit() else 0

# 1. Salario más alto y más bajo
def salario_extremos(employees):
    max_salary = max(employees, key=lambda x: x["SALARY"])
    min_salary = min(employees, key=lambda x: x["SALARY"])
    return max_salary, min_salary

# 2. Agrupar por departamento
def agrupar_por_departamento(employees):
    departamentos = {}
    for emp in employees:
        dept = emp["DEPARTMENT_ID"]
        if dept not in departamentos:
            departamentos[dept] = []
        departamentos[dept].append(emp)
    return departamentos

# 3. Agrupar por manager
def agrupar_por_manager(employees):
    managers = {}
    for emp in employees:
        manager = emp["MANAGER_ID"]
        if manager not in managers:
            managers[manager] = []
        managers[manager].append(emp)
    return managers

# 4. Ordenar por apellido
def ordenar_por_apellido(employees):
    return sorted(employees, key=lambda x: x["LAST_NAME"])

# 5. Ordenar por código (EMPLOYEE_ID)
def ordenar_por_codigo(employees):
    return sorted(employees, key=lambda x: int(x["EMPLOYEE_ID"]))

# Ejecutar las funciones y mostrar resultados
salario_max, salario_min = salario_extremos(employees)
deptos = agrupar_por_departamento(employees)
managers = agrupar_por_manager(employees)
orden_apellido = ordenar_por_apellido(employees)
orden_codigo = ordenar_por_codigo(employees)

# Mostrar algunos resultados
salario_max, salario_min, list(deptos.keys())[:5], list(managers.keys())[:5], orden_apellido[:3], orden_codigo[:3]
print("Salarios")
print(salario_max, salario_min)
print("--"*60)