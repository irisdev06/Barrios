with open('himno (1).txt','r') as file:
    contenido = file.read()
    palabra = 'gloria '
    
contenido=contenido.split()
print(contenido)
repeticiones = [palabra for x in contenido if x == palabra.lower()]

print(repeticiones)

if repeticiones: 

    print(f'la palabra"{palabra}" se repite {len(repeticiones)} veces')
else:
    print(f'la palabra "{palabra}" no se encuentra en el archivo')