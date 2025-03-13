import csv

data = [
    ["Nombre", "Edad", "Sabor Helado Fav", "Deporte Fav"],
    ["Iris", 23, "Maracuyá", "Patinaje"],
    ["Margarita", 26, "Fresa", "Fútbol"],
    ["Camilo", 20, "Mora", "Ninguno"],
    ["Juan", 30, "Chocolate", "Baloncesto"],
    ["Sofía", 19, "Vainilla", "Natación"],
    ["Diego", 25, "Coco", "Ciclismo"],
    ["Valeria", 22, "Arequipe", "Tenis"],
    ["Andrés", 27, "Limón", "Atletismo"],
    ["Laura", 24, "Cereza", "Voleibol"],
    ["Esteban", 21, "Tamarindo", "Rugby"],
    ["Natalia", 29, "Dulce de leche", "Surf"],
    ["Samuel", 18, "Nuez", "Béisbol"],
    ["Carolina", 31, "Mandarina", "Senderismo"],
    ["Manuel", 28, "Piña", "Escalada"],
    ["Luisa", 20, "Melón", "Esgrima"],
    ["Ricardo", 23, "Algodón de azúcar", "Ajedrez"],
    ["Fernanda", 25, "Matcha", "Yoga"],
    ["Julián", 32, "Tutti Frutti", "Boxeo"],
    ["Paula", 19, "Café", "Gimnasia"],
    ["Sebastián", 26, "Frutos Rojos", "Snowboard"]
]



with open("Crear Csv/personas_lista_1.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for x in data:
        writer.writerow(x)

data2 = [
    ["Animal", "Peso (kg)", "Le gustan los besitos", "Nivel de Cariño", "Comida Favorita"],
    ["Perro", 25, "Sí", "Alto", "Huesos y croquetas"],
    ["Gato", 4, "Depende del humor", "Medio", "Atún y pollo"],
    ["Conejo", 2, "Sí", "Alto", "Zanahorias y hojas verdes"],
    ["Tortuga", 10, "No", "Bajo", "Lechuga y frutas"],
    ["Loro", 1.2, "Sí, pero solo de su humano favorito", "Alto", "Semillas y frutas"],
    ["Hamster", 0.3, "Sí, pero con cuidado", "Medio", "Semillas y nueces"],
    ["Caballo", 500, "Sí, en la nariz", "Alto", "Manzanas y zanahorias"],
    ["Cerdo", 120, "Sí, pero solo si hay comida", "Alto", "Cualquier cosa comestible"],
    ["Erizo", 0.6, "No, soy puntiagudo", "Bajo", "Insectos y frutas"],
    ["Pato", 3, "Sí, pero con respeto", "Medio", "Maíz y hierbas"],
    ["León", 190, "Solo si no quieres salir vivo", "Bajo", "Carne fresca"],
    ["Tiburón", 680, "Mejor no intentarlo", "Nulo", "Peces y focas"],
    ["Koala", 8, "Sí, pero con eucalipto en la boca", "Alto", "Hojas de eucalipto"],
    ["Oso Panda", 100, "Sí, pero con bambú en la mano", "Alto", "Bambú"],
    ["Zorro", 6, "Depende del día", "Medio", "Pequeños roedores y frutas"],
    ["Mapache", 9, "Sí, pero revisa tus bolsillos después", "Medio", "Frutas y basura"],
    ["Lobo", 45, "Solo de la manada", "Medio", "Carne de caza"],
    ["Elefante", 5400, "Sí, con la trompa", "Alto", "Hojas, frutas y corteza"],
    ["Delfín", 150, "Sí, pero en el agua", "Alto", "Peces y calamares"],
    ["Gallo", 3.5, "No, mejor corre", "Bajo", "Granos y lombrices"],
    ["Ardilla", 0.5, "Sí, pero solo si confía en ti", "Medio", "Nueces y semillas"],
    ["Búho", 2, "No, respeto mi espacio", "Bajo", "Pequeños roedores"],
    ["Hipopótamo", 1500, "No, mejor no te acerques", "Bajo", "Plantas acuáticas"],
    ["Pingüino", 30, "Sí, pero solo si eres su pareja", "Medio", "Peces y calamares"],
    ["Canguro", 85, "Sí, pero no te pongas en su camino", "Medio", "Hierbas y hojas"],
    ["Camaleón", 0.2, "No, soy tímido", "Bajo", "Insectos"],
    ["Suricata", 1, "Sí, en grupo", "Alto", "Insectos y huevos"],
    ["Ornitorrinco", 1.5, "¿Qué es un besito?", "Desconocido", "Gusanos y crustáceos"],
    ["Hormiga", 0.00003, "No, tengo trabajo que hacer", "Nulo", "Azúcar y hojas"]
]


with open("Crear Csv/productos_lista_2.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data2)
