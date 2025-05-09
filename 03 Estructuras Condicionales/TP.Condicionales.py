#Ejercicio1
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")


#Ejercicio2
nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


#Ejercicio3
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


#Ejercicio4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


#Ejercicio5
contraseña = input("Ingrese una contraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#Ejercicio6
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media < mediana < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
else:
    sesgo = "Sin sesgo"

print(f"Números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")
print(f"Resultado: {sesgo}")


#Ejercicio7
frase = input("Ingrese una frase o palabra: ")

ultima_letra = frase[-1]
if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    frase = frase + "!"

print(frase)


#Ejercicio8
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 para mayúsculas, 2 para minúsculas o 3 para primera letra mayúscula: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")


#Ejercicio9

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")


#Ejercicio10
hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

print(f"La estación correspondiente es: {estacion}")