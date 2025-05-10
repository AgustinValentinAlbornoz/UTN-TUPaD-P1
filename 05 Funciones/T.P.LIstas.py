#Ejercicio1
lista_multiplos_4 = list(range(4, 101, 4))
print(lista_multiplos_4)

print("//////////////////////////////////")


#Ejercicio2
mi_lista = ["pizza", "guitarra", "viajes", "cine", "programación"]
penultimo_elemento = mi_lista[-2]
print(penultimo_elemento)

print("///////////////////////////////////")


#Ejercicio3
lista_vacia = []

lista_vacia.append("Guitarra")
lista_vacia.append("Pizza")
lista_vacia.append("Fútbol")

print(lista_vacia)

print("////////////////////////////////////")


#Ejercicio4
animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"

print(animales)

print("/////////////////////////////////////")


#Ejercicio5
#Este programa elimina el numero mas alto de la lista y luego imprime la lista modificada.

print("//////////////////////////////////////")


#Ejercicio6
lista_numeros = list(range(10, 31, 5))
print(lista_numeros[:2])

print("///////////////////////////////////////")


#Ejercicio7
autos = ["sedan", "polo", "suran", "gol"]

autos[1:3] = ["camioneta", "deportivo"]

print(autos)

print("///////////////////////////////////////")


#Ejercicio8
dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

print("///////////////////////////////////////")


#Ejercicio9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

print("///////////////////////////////////////")


#Ejercicio10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)