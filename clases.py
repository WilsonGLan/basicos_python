#!/usr/bin/env python
# -*- coding: utf-8 -*-
# información encontrada en https://pythones.net/clases-y-metodos-python-oop/

# Ejemplo 1:

class Producto():   #clase producto el cual comienza con inicial en mayuscula
    def __init__(self, color) : #se define el constructor
        self.color = color #Atributo


#=========================================================================================
# Ejemplo 2

class Deporte(object):
    def __init__(self, nombre, numJugadores):
        self.nombre = nombre
        self.numJugadores = numJugadores
    
    def informacion (self):
        datos = ("El deporte que vamos a practicar hoy es {} y el equipo esta compuesto por {} jugadores")
        print(datos.format(self.nombre,self.numJugadores))

# la invocacion o instanciamiento de un objeto debe realizarse despues de definir los metodos
juego = Deporte('boleiball',6)
juego.informacion()

#=========================================================================================
# Ejemplo 3: 

# definimos dos clases en donde trabajamos con Herencia simple

class Television():
    def __init__(self, programa, categoria, genero):
        self.programa = programa
        self.categoria = categoria
        self.genero = genero

class Canal(Television):

#No es necesario crear constructor si la clase padre ya la tiene
    def mostrar(self):
        print("A continuación sigue el programa",self.programa, "en la franja de ", self.categoria, "genero ", self.genero)

tvninguna = Canal("\"El dolor de los inocentes\"", "Novela", "Terror")

tvninguna.mostrar()

#=========================================================================================
# Ejemplo 4: 

# definimos dos clases en donde trabajamos con Herencia multiple

class Television(object):
    def __init__(self, programa, categoria, genero):
        self.programa = programa
        self.categoria = categoria
        self.genero = genero

class Reseña(object):
    def comentario(self):
        print("Este programa relata la historia de colombianos sumidos la corrupción de su gobierno")

class Canal(Television,Reseña):

    def mostrar(self):
        print("A continuación sigue el programa",self.programa, "en la franja de ", self.categoria, "genero ", self.genero)

tvninguna = Canal("\"El dolor de los inocentes\"", "Novela", "Terror")

tvninguna.mostrar()
tvninguna.comentario()