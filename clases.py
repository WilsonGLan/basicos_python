#!/usr/bin/env python
# -*- coding: utf-8 -*-
# información encontrada en https://pythones.net/clases-y-metodos-python-oop/

# Ejemplo 1:

class Producto():   #clase producto el cual comienza con inicial en mayuscula
    def __init__(self, color) : #se define el constructor
        self.color = color #Atributo


#=========================================================================================
# Ejemplo 2

class Deporte():
    def __init__(self, nombre, numJugadores):
        self.nombre = nombre
        self.numJugadores = numJugadores

juego = Deporte('boleiball',6)

#=========================================================================================
# Ejemplo 3: (Continuación del 2)

# definimos un metodo de la clase Deporte

    def informacion (self):
        datos = ("El deporte que vamos a practicar hoy es {} y el equipo esta compuesto por {} jugadores")
        print(datos.format(self.nombre,self.numJugadores))
