import json
# Abrir el archivo ordenes.json
with open("ejemplo/cerditos.json") as archivo:
    # Cargar su contenido y crear un diccionario
    datos = json.load(archivo)

cerditos = datos["cerditos"]
# Acceder a él
print("--"*100)
print(cerditos)
print("--"*100)
print("--"*100)
print(cerditos[1])
print("--"*100)
print("--"*100)

# Recorrer Cerditos
for cerdito in cerditos:
    print(cerdito)
    
# Cerditos Felices
print("--"*100)
print("--"*100)
felices = [c for c in cerditos if c ["feliz"]]
print(f"Los Cerditos Felices son: {felices}")
tristes = [c for c in cerditos if c ["feliz"] == False]
print(f"Los Cerditos no Felices son: {tristes}")
print("--"*100)
print("--"*100)