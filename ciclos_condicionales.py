#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ===============================================================================
# Ciclo while

x = 0
while (x < 5):
    x = x+1
    print(x)

#Uso de break en un while
while True:
    mensaje = input('escribe una palabra: ')
    if mensaje == 'chupacabra':
        print('Has adivinado')
        break

#Usando else con un ciclo while pero tambien sirve con un for
#modificar el valor de i con algo menor y observar los resultados

i = 5
while i < 5:
    print (i)
    i += 1
else:
    print("else:", i)

#Averiguar la altura de la piramide basado en el número de bloques
bloques = int(input("Ingrese el número de bloques:"))
puestos = 0
altura = 1
while bloques > 0:
    bloques = bloques - 1
    puestos = puestos + 1
    if puestos == altura:
        altura = altura + 1
        puestos = 0

altura = altura -1  
print("La altura de la pirámide:", altura)

# Otra manera de solucionar el problema anterior 
bloques = int(input("Ingrese el número de bloques:"))
acumulado = 0
altura = 0

while bloques >= acumulado:
    altura = altura + 1
    acumulado = altura + acumulado

altura = altura - 1
print("La altura de la pirámide:", altura)


# ===============================================================================
# Ciclo for

# Para este ejemplo se crea primero una lista llamada "numeros"
numeros = [10, 20, 30, 40, 50]
# se recorre la lista de numeros mediante numero y se imprime
for numero in numeros:
    print(numero)


puntos = [(0, 0), (3, 5), (-1, 4), (10, 2)]
for y, x in puntos:
    print("Px = {0}, Py = {1}".format(x, y))

''' Esto es un comentario multilinea:
    en el siguiente print el 
    0 corresponde al primer parametro en la posición 0 de format
    1 corresponde al segundo parametro en la posición 1 de format
    2 corresponde al tercer parametro en la posición 2 de format
'''
n = 2
for k in range(1, 12):
    print("ss {0} x {1} = {2}".format(n, k, n*k))

ord_asc = [1, 2, 3, 4]
print(ord_asc[::-1])

for num in reversed(ord_asc):
    print(num)

#Cuenta 5 Mississipi con el módulo time y el método sleep
import time
for i in range(1,6):
    print(i," Mississippi")
    time.sleep(1)

if i == 5:
    print('¡Listo o no, ahí voy!')

#break y continue

# break - ejemplo
# cuando i sea igual a 3 terminara por completo el ciclo
print("La instrucción de ruptura:")
for i in range(1,6):
    if i == 3:
        break
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

# continue - ejemplo
# cuando i sea igual a 3 saltara la impresión del mensaje y procederá a comenzar el próximo ciclo.
print("\nLa instrucción continue:")
for i in range(1,6):
    if i == 3:
        continue
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord.
# Quitar vocales
userWord = input('Por favor escriba una palabra con vocales: ')
userWord = userWord.upper()
for letra in userWord:
    # Completa el cuerpo del ciclo for.
    if letra == 'A':
        continue
    elif letra == 'E':
        continue
    elif letra == 'I':
        continue
    elif letra == 'O':
        continue
    elif letra == 'U':
        continue
    else:
        print(letra)

#variante del anterior:
palabraSinVocal = ""

# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord.
userWord = input('Por favor escriba una palabra con vocales: ')
userWord = userWord.upper()
for letra in userWord:
    # Completa el cuerpo del ciclo for.
    if letra == 'A':
        continue
    elif letra == 'E':
        continue
    elif letra == 'I':
        continue
    elif letra == 'O':
        continue
    elif letra == 'U':
        continue
    else:
        # Imprimir la palabra asignada a palabraSinVocal.
        palabraSinVocal = palabraSinVocal+letra

print(palabraSinVocal)




# ===============================================================================
# CONDICIONALES

# Algo super básico para las condicionales if y else:

n1 = 6
n2 = 14

if (n2/2) == n1:
    print(n2, " es divisible por", n1)
else:
    print(n2, " no es divisible por", n1)

a = "maria"
b = "diana"
c = "wilson"

print("¿De quien quiere saber: maria, diana o wilson?")
nombre = input()
print(nombre)

a = 'maria'
nombre = 'wilson'
if a == nombre:  # condicion si a es exactamente el nombre escrito, entonces(:)
    print("Maria es mi madre")  # Imprimir
elif a == nombre:
    print("Diana es mi hermana")
elif a == nombre:
    print("Wilson soy yo")
else:
    print("No lo conozco")

# ===========================================================
#
# Averiguar si un año es bisiesto
#
#año = int(input("Introduzca un año:"))
#!/usr/bin/env python
# -*- coding: utf-8 -*-

annio = 1980

if (annio % 4 > 0):
    print('es un año comun')
elif (annio % 100 > 0 and annio < 1582):
    print('No dentro de la epoca gregoriana')
elif (annio % 100 > 0 and annio >= 1582):
    print('Es un año bisiesto')
elif (annio % 400 > 0):
    print('Es un año común')
else:
    print('Es bisiesto')
