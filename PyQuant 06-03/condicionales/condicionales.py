# 1. Pedir 3 números e indicar cual de ellos es el valor del medio.
def valor_del_medio(num1, num2, num3):
    if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
        return num1
    elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
        return num2
    else:
        return num3


# 2. Pedir tres números y escribir si son los tres iguales, dos iguales o tres distintos.
def comparar_numeros(num1, num2, num3):
    if num1 == num2 == num3:
        return "Todos son iguales"
    elif num1 == num2 or num1 == num3 or num2 == num3:
        return "Hay dos iguales"
    else:
        return "Son tres distintos"


# 3. Pedir un número entre 0 y 9.999 y decir cuántas cifras tiene.
def contar_cifras(numero):
    if numero < 0 or numero > 9999:
        return "Número fuera de los límites"
    
    cifras = 0
    while numero > 0:
        numero = numero // 10
        cifras += 1
    
    return cifras


# 4. Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien, etc.
def calificar_nota(nota):
    if nota < 5:
        return "Insuficiente"
    elif 5 <= nota < 6:
        return "Suficiente"
    elif 6 <= nota < 7:
        return "Bien"
    elif 7 <= nota < 9:
        return "Notable"
    else:
        return "Sobresaliente"


# 5. Juego de preguntas con respuestas "Si" o "No".
def juego_de_preguntas():
    preguntas = [
        ("¿Colón descubrió América?", "Si"),
        ("¿La independencia de Colombia fue en el año 1810?", "Si"),
        ("¿The Doors fue un grupo de rock Americano?", "Si")
    ]
    
    for pregunta, respuesta_correcta in preguntas:
        respuesta_usuario = input(pregunta + " (Si/No): ").strip()
        if respuesta_usuario != respuesta_correcta:
            return "Perdiste, respuesta incorrecta"
    
    return "Ganaste, todas las respuestas son correctas"


# 6. Número de días del año y el mes correspondiente.
def obtener_mes_por_dia(dia_del_anio):
    if dia_del_anio <= 31:
        return "Enero"
    elif dia_del_anio <= 59:
        return "Febrero"
    elif dia_del_anio <= 90:
        return "Marzo"
    elif dia_del_anio <= 120:
        return "Abril"
    elif dia_del_anio <= 151:
        return "Mayo"
    elif dia_del_anio <= 181:
        return "Junio"
    elif dia_del_anio <= 212:
        return "Julio"
    elif dia_del_anio <= 243:
        return "Agosto"
    elif dia_del_anio <= 273:
        return "Septiembre"
    elif dia_del_anio <= 304:
        return "Octubre"
    elif dia_del_anio <= 334:
        return "Noviembre"
    elif dia_del_anio <= 365:
        return "Diciembre"
    else:
        return "Número de días fuera del rango"

# 7. Cálculo del salario semanal de un obrero.
def calcular_salario_semanal(horas_trabajadas):
    if horas_trabajadas <= 40:
        return horas_trabajadas * 2600
    else:
        horas_extra = horas_trabajadas - 40
        return (40 * 2600) + (horas_extra * 5000)


# 8. Calcular el costo de una llamada telefónica.
def costo_llamada(minutos):
    if minutos <= 3:
        return 200
    else:
        return 200 + (minutos - 3) * 50


# 9. Solicitar una fecha al usuario y calcular el tiempo transcurrido o el tiempo faltante.
def calcular_tiempo_fecha(dia, mes, anio):
    from datetime import datetime
    fecha_usuario = datetime(anio, mes, dia)
    fecha_actual = datetime.now()
    
    if fecha_usuario < fecha_actual:
        return f"Han pasado {fecha_actual - fecha_usuario}"
    else:
        return f"Faltan {fecha_usuario - fecha_actual} para llegar a esa fecha."


# 10. Incrementar la hora en un segundo.
def siguiente_segundo(hora, minuto, segundo):
    segundo += 1
    if segundo == 60:
        segundo = 0
        minuto += 1
        if minuto == 60:
            minuto = 0
            hora += 1
            if hora == 24:
                hora = 0
    return f"{hora:02d}:{minuto:02d}:{segundo:02d}"


# 11. Calcular la cantidad de billetes de cada denominación.
def calcular_billetes(cantidad):
    denominaciones = [50000, 20000, 10000, 5000, 2000, 1000]
    resultado = []
    
    for denom in denominaciones:
        cantidad_billetes = cantidad // denom
        if cantidad_billetes > 0:
            resultado.append(f"{cantidad_billetes} billetes de {denom}")
            cantidad -= cantidad_billetes * denom
            
    return ', '.join(resultado)


# 12. Hora que será dentro de 1 segundo.
def hora_siguiente(hora, minutos, segundos):
    segundos += 1
    if segundos == 60:
        segundos = 0
        minutos += 1
        if minutos == 60:
            minutos = 0
            hora += 1
            if hora == 24:
                hora = 0
    return f"{hora:02d}:{minutos:02d}:{segundos:02d}"


# 13. Convertir segundos en horas, minutos y segundos.
def convertir_segundos(segundos):
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60
    return f"{horas} horas, {minutos} minutos, {segundos} segundos"


# 14. Determinar en qué cuadrante está un ángulo.
import math
def cuadrante_angulo(angulo):
    angulo = angulo % 360  # Normalizar el ángulo a un rango de 0 a 360 grados
    if 0 < angulo < 90:
        cuadrante = 1
    elif 90 < angulo < 180:
        cuadrante = 2
    elif 180 < angulo < 270:
        cuadrante = 3
    elif 270 < angulo < 360:
        cuadrante = 4
    else:
        cuadrante = "Sobre el eje"
    
    radianes = angulo * (math.pi / 180)
    
    vuelta = angulo // 360
    return f"Cuadrante: {cuadrante}, Vuelta: {vuelta}, Radianes: {radianes:.2f}"


# 15. Calcular la fecha de Pascua para un año dado.
def fecha_de_pascua(anio):
    A = anio % 19
    B = anio % 4
    C = anio % 7
    D = (19 * A + 24) % 30
    E = (2 * B + 4 * C + 6 * D + 5) % 7
    N = 22 + D + E
    
    if N > 31:
        mes = "Abril"
        N -= 31
    else:
        mes = "Marzo"
    
    return f"La fecha de Pascua en {anio} es el {N} de {mes}"

# Puedes probar cada función llamándola con diferentes valores de entrada.
