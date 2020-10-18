#!/usr/bin/env python
# -*- coding: utf-8 -*-


#====================================================================
#Ejercicios básicos de Phyton


#Calcular el area de un triangulo
base = 7    #le asigno a una variable llamada base el valor de 7
altura=6    #le asigno a una variable llamada altura el valor de 6
area=base*altura/2  #uso las variables para calcular el area y lo asigno a una variable
print("El area es: ",area) #imprimo en pantalla el valor del resultado


#Condicional if

#Solicita mediante imput un valor correspondiente a la edad
edad = int(input("Escriba su edad: ")) 


# Todo lo que se va a calcular dentro de una condicional va después de los dos puntos 
# y en la próxima línea con tabulación
if edad < 18:
    print("Es usted menor de edad")
else:
    print("Es usted mayor de edad")
print("¡Hasta la próxima!")



#Para capturar solo texto:
mensaje = input("escriba texto: ")
print ("Imprimiendo texto: ", mensaje)

#para capturar entero:
mensaje2 = int(input("escriba un número: "))
print("Imprimiendo numero:",mensaje2)

#El segundo mensaje debe imprimirse continuamente en la misma linea
print("Mi nombre es ", end="")
print("Monty Python.")

#Se indica que separador debe aparecer
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")
print("Mi", "nombre", "es", "Monty", "Python.", sep="")

#Utilizar el caracter de escape para poder imprimir comillas dobles
print("\"hola\"")

a = "trabajo suelto"
b = "joder"
print(a+b) #el operador plus (+) concatena sin espacio al final
print(a,b) #el caracter coma (,) concatena dejando un espacio al final

print(1//2*3)

x = int(input())
y = int(input())
x = x % y
x = x % y
y = 1/2+3//3+4**2
print (y)