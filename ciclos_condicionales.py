#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ciclo while

x=0
while (x<5) :
    x=x+1
    print(x)

# Ciclo for

# Para este ejemplo se crea primero una lista llamada "numeros"
numeros = [10, 20, 30, 40, 50]
# se recorre la lista de numeros mediante numero y se imprime
for numero in numeros:
    print(numero)


puntos = [(0,0), (3,5), (-1,4), (10,2)]
for y,x in puntos:
    print ("Px = {0}, Py = {1}".format(x,y))

''' Esto es un comentario multilinea:
    en el siguiente print el 
    0 corresponde al primer parametro en la posición 0 de format
    1 corresponde al segundo parametro en la posición 1 de format
    2 corresponde al tercer parametro en la posición 2 de format
'''
n = 2
for k in range(1,12):    
    print ("ss {0} x {1} = {2}".format(n,k,n*k))

ord_asc = [1, 2, 3, 4]
print(ord_asc[::-1])

for num in reversed(ord_asc):
    print(num)


#===============================================================================
# CONDICIONALES

# Algo super básico para las condicionales if y else:

n1 = 6
n2 = 14

if (n2/2) == n1:
    print(n2," es divisible por", n1)
else:
    print(n2," no es divisible por", n1)

a = "maria"
b = "diana"
c = "wilson"

print("¿De quien quiere saber: maria, diana o wilson?")
nombre = input()
print(nombre)

if a == nombre:#condicion si a es exactamente el nombre escrito, entonces(:)
    print ("Maria es mi madre") # Imprimir
elif a == nombre:
    print ("Diana es mi hermana")
elif a == nombre:
    print ("Wilson soy yo")
else:
    print ("No lo conozco")

