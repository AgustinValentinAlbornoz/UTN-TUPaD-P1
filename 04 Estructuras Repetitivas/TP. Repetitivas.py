#Ejercicio1
for i in range(101):
    print(i)

print("//////////////////")


#Ejercicio2
while True:
    numero = input("Ingresa un número entero: ")
    if numero.isdigit():
        print(f"El número ingresado tiene {len(numero)} dígito(s).")
        break
    else:
        print("Por favor, ingresa un número entero válido.")

print("//////////////////////")


#Ejercicio3
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

suma = 0
for i in range(min(a, b) + 1, max(a, b)):
    suma += i

print(f"La suma de los números entre {a} y {b}, excluyendo esos valores, es: {suma}")

print("///////////////////////")


#Ejercicio4
suma = 0

while True:
    numero = int(input("Ingresa un número entero (0 para finalizar): "))
    if numero == 0:
        break
    suma += numero

print(f"La suma total es: {suma}")

print("////////////////////////")


#Ejercicio5
import random

numero_secreto = random.randint(0, 9)
intentos = 0
numero = -1

while numero != numero_secreto:
    numero = int(input("Adivina un número entre 0 y 9: "))
    intentos += 1

print(f"¡Ganaste! Intentos: {intentos}")

print("///////////////////////////")


#Ejercicio6
i = 100

while i >= 0:
    print(i)
    i -= 2

print("//////////////////////////////")


#Ejercicio7
n = int(input("Ingresa un número entero positivo: "))

suma = 0
i = 0

while i <= n:
    suma += i
    i += 1

print(f"La suma de los números entre 0 y {n} es: {suma}")

print("///////////////////////////////")


#Ejercicio8
cantidad = 100
pares = 0
impares = 0
positivos = 0
negativos = 0

for _ in range(cantidad):
    numero = int(input("Ingresa un número entero: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Pares: {pares}, Impares: {impares}")
print(f"Positivos: {positivos}, Negativos: {negativos}")

print("/////////////////////////////////////")


#Ejercicio9
cantidad = 100
suma = 0
contador = 0

while contador < cantidad:
    numero = int(input("Ingresa un número entero: "))
    suma += numero
    contador += 1

media = suma / cantidad

print(f"La media de los números ingresados es: {media}")

print("//////////////////////////////////////")


#Ejercicio10
numero = int(input("Ingresa un número entero: "))
invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero //= 10

print(f"El número invertido es: {invertido}")