import csv

data_cerditos = [
    {"Nombre": "Patitas", "Edad": 3, "Pasaporte": "Sí", "Peso (kg)": 45, "Color": "Rosa", "Dueño": "Lucas"},
    {"Nombre": "Babe", "Edad": 2, "Pasaporte": "No", "Peso (kg)": 30, "Color": "Blanco", "Dueño": "Granjero Hoggett"},
    {"Nombre": "Pepita", "Edad": 4, "Pasaporte": "Sí", "Peso (kg)": 25, "Color": "Rosa", "Dueño": "Papá Pig"},
    {"Nombre": "Lola", "Edad": 1, "Pasaporte": "No", "Peso (kg)": 35, "Color": "Marrón", "Dueño": "Fern Arable"},
    {"Nombre": "Potaxiana", "Edad": 3, "Pasaporte": "Sí", "Peso (kg)": 20, "Color": "Rosa", "Dueño": "Winnie Pooh"},
    {"Nombre": "Jamoncito", "Edad": 5, "Pasaporte": "Sí", "Peso (kg)": 50, "Color": "Rosa", "Dueño": "Andy"},
    {"Nombre": "Bolitas", "Edad": 2, "Pasaporte": "No", "Peso (kg)": 28, "Color": "Blanco", "Dueño": "Rebelión Animal"},
    {"Nombre": "Jorge", "Edad": 4, "Pasaporte": "Sí", "Peso (kg)": 32, "Color": "Marrón", "Dueño": "Doctor Dolittle"}
]

with open("cerditos.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Nombre", "Edad", "Pasaporte", "Peso (kg)", "Color", "Dueño"] 
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data_cerditos)

data_aranas = [
    {"Nombre": "Tarantela", "Color": "Negro", "Especie": "Tarántula Goliat", "Edad": 5},
    {"Nombre": "Mosca", "Color": "Rojo y Azul", "Especie": "Araña Radiactiva", "Edad": 3},
    {"Nombre": "Chocolate", "Color": "Negro con Blanco", "Especie": "Viuda Negra", "Edad": 2},
    {"Nombre": "Argelina", "Color": "Marrón", "Especie": "Araña Lobo", "Edad": 4},
    {"Nombre": "Charlotte", "Color": "Gris", "Especie": "Araña de Jardín", "Edad": 6},
    {"Nombre": "Harry Pawter", "Color": "Blanco", "Especie": "Araña de Seda", "Edad": 1},
    {"Nombre": "Lobito", "Color": "Negro y Rojo", "Especie": "Araña Mutante", "Edad": 10},
    {"Nombre": "Rosa", "Color": "Negro", "Especie": "Araña Cazadora", "Edad": 3}
]

with open("aranas.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Nombre", "Color", "Especie", "Edad"]  
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data_aranas)
