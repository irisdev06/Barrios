def palabra_himno(palabra):
    try:
        with open('himno_colombia.txt', 'r', encoding='utf-8') as archivo:
            contenido = archivo.read().lower()  
            ocurrencias = contenido.count(palabra.lower())  
            if ocurrencias > 0:
                print(f"Tu palabra elegida '{palabra}' aparece {ocurrencias} veces en el himno de Colombia.")
            else:
                print(f"Tu palabra '{palabra}' no está en el himno de Colombia.")
    except FileNotFoundError:
        print("El archivo 'himno_colombia.txt' no se encuentra en el directorio.")

palabra = input("Introduce la palabra que deseas buscar en el himno de Colombia: ")
palabra_himno(palabra)
