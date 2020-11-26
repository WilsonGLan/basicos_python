
#=================================================================================
# Las listas en Python son tratadas con [] osea Listas=[ ]
Lista1 = [1, 2, 3]
Lista2 = [4, 5, 6]
#Imprimir un numero de la lista de acuerdo a la posición:
print(Lista2[1])

print (Lista1)

# Método Append

# Inserta un elemento al final de la lista
Lista2.append(0)
print(Lista2)

# Metodo extend
# Inserta varios elementos al final de la lista

Lista2.extend(98) # presenta un error cuando se ingresan numeros
Lista2.extend(Lista1) # Se agregan numeros de otra lista
print(Lista2)

# Método insert
# Agrega un elemento a una posición especifica de la lista

Lista2.insert(2,33)
print(Lista2)

# Método pop
# Elimina elementos de una lista indicando el indice

ocupaciones = ['Secretaria','Mecanico','Obrero','Conductor']
print(ocupaciones)
ocupaciones.pop(2)
print(ocupaciones)

# Método remove
# Elimina elementos de una lista indicando el valor

ocupaciones.remove('Obrero')
print(ocupaciones)

# Método count
# Cuenta cuantas veces aparece un elemento indicandole el valor en la lista.
num_ocup = ocupaciones.count('Secretaria')
print(num_ocup)

# Método reverse
# Me imprime la lista desde el último elemento al primero
ocupaciones.reverse()
print(ocupaciones)

#invertir el orden de impresión
ord_asc = [1, 2, 3, 4]
print(ord_asc[::-1])

for num in reversed(ord_asc):
    print(num)

#=================================================================================
#Las tuplas en Python se trabajan con parentesis () osea tuplas=() y no se pueden modificar

nombres=("Ana", "Daniela", "Jose", "David","Wilson")
print(nombres)
#Imprimir un nombre de la tupla de acuerdo a la posición:
print(nombres[3])
#Imprimir la lista de la tupla de acuerdo a un rango pero restando 1 a la posición final:
print(nombres[1:4])


#=================================================================================
#RANGE -->crea un rango de valores
# La función list() convierte a range() en una lista
x = list(range(5))
print(x)

#De la lista de numeros generado solo imprime cada tercer número despues del primero
x = list(range(1,10,3))
print(x)
#=================================================================================
#DICCIONARIO

MiMarga = {
'Nombre' : 'Margarita',
'Apellido' : 'Filosa',
'Alias' : 'Cuchillos',
'Padres' : ["Maria Chaira", "Carlos Cortez"], # Se incluye una lista en el ejemplo
'Edad' : 55,
'Genero' : 'Femenino',
'Estado Civil' : 'Soltera',
'Hijos' : 'Ninguno/a',
'Mascotas' : 'Gatos',
'Nombres de mascotas' : ["Mango", "Doble Filo"] #Segunda lista
}

print (MiMarga ['Apellido'])
print (MiMarga ['Padres'][0:2])
print (MiMarga ['Padres'][1])

#ingresando un nuevo dato al diccionario:
MiMarga['Ingresos'] = '16000'
print (MiMarga ['Ingresos'])

#Modificando valores
MiMarga['Ingresos'] = '25000'
print (MiMarga ['Ingresos'])

#Cambiar la clave conservando su valor
MiMarga['Salario'] = MiMarga.pop('Ingresos')
print (MiMarga ['Salario'])

#Eliminando clave y valor
del(MiMarga['Nombre'])
print(MiMarga['Nombre']) #marca error por que ya no existe

MiMarga['Nombre'] = 'Margarita' #vuelvo a agregar la clave Nombre
print(MiMarga.get('Nombre', "No tienen nombre")) #imprimir el valor de Nombre

#imprimir todas las claves
claves = MiMarga.keys()
print(claves)

#imprimir todos los valores
valores = MiMarga.values()
print(valores)

lista_invitados = ['Marcos','Angelica', 'Matias', 'Jose', 'Gaston', 'Nahuel', 'Ricardo', 'Roberto', 'Mariano', 'Mauricio',
'Leonel', 'Leonardo', 'Aldo', 'Raquel', 'Hernan', 'Sofia', 'Juan', 'Antonio', 'Marcelo', 'Juan cruz', 'Pedro', 'Pepe', 'Luisina',
'Celeste', 'Zulma', 'Irma', 'Diana', 'Daiana', 'Wally', 'Ruben', 'Rosendo', 'Joaquin']

x = 'Wilson'

if x in lista_invitados:
    print ("Si está en la lista")
else:
    print ("No se encuentra")

print(x)

#=================================================================================================
#Ordenar listas con el método de la burbuja
#Ejemplo obtenido del curso edube.org con Cisco 

miLista = []  #Definimos la variable de tipo lista
swapped = True  #Definimos una variable booleana
num = int (input("¿Cuántos elementos deseas ordenar?:"))

#El usuario ingresa una lista de elementos en desorden cuya cantidad sea la especificada anteriormente
for i in range(num):
    val = float(input("Introduce un elemento de la lista:"))
    miLista.append(val)


#Se procede a ordenar los elementos ingresados en la lista.
while swapped:
    swapped = False
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped = True
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print("\nOrdenado:")
print(miLista)

#=================================================================================================
#Ordenar listas con dos ciclos for 
#Se acopla el ejercicio anterior

nuevaLista = []

tam = int(input("Cuantos números se deben ordenar "))
print("De acuerdo")

for i in range(tam):
    num = int(input("De acuerdo, Por favor ingrese el elemento de la lista ==> "))
    nuevaLista.append(num)

for j in range(len(nuevaLista) - 1):
    for i in range(len(nuevaLista) - 1):
        if nuevaLista[i] > nuevaLista[i + 1]:
            nuevaLista[i], nuevaLista[i + 1] = nuevaLista[i + 1], nuevaLista[i]

print("Asi queda ordenada la lista:")
print(nuevaLista)

#=================================================================================================
#Ordenar listas con el método sort de python para ordenar de menor a mayor
#Se acopla el ejercicio anterior

nuevaLista = []

tam = int(input("Cuantos números se deben ordenar "))
print("De acuerdo")

for i in range(tam):
    num = int(input("De acuerdo, Por favor ingrese el elemento de la lista ==> "))
    nuevaLista.append(num)

print("Asi queda ordenada la lista:")
nuevaLista.sort()
print(nuevaLista)

#=================================================================================================
#Ordenar listas con el método reverse de python para ordenar de mayor a menor
#Se acopla el ejercicio anterior

nuevaLista = []

tam = int(input("Cuantos números se deben ordenar "))
print("De acuerdo")

for i in range(tam):
    num = int(input("De acuerdo, Por favor ingrese el elemento de la lista ==> "))
    nuevaLista.append(num)

print("Asi queda ordenada la lista:")
nuevaLista.reverse()
print(nuevaLista)

#=================================================================================================
# Copiando parte de la lista
#Ejemplo obtenido del curso edube.org con Cisco 

miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[0:5]
print(nuevaLista)

#Con indices negativos
nuevaLista = miLista [1:-1]
print(nuevaLista)