#Crear una función básica:

#Ejemplo de la tabla de multiplicar:
def tablasMultiplicar(x):
    for i in range(1,11):
        print(i," * ",x," = ", i*x)

a    = int(input("Cual tabla de multiplicar desea ver:"))
tablasMultiplicar(a)


ListasAlumnos = [['Juan', 'Carmelo', 5, 7, 9, 7], 
                 ['Laura', 'Jazmine', 7, 8, 5, 6.66],
                 ['Dario', 'Villalobos', 5, 6, 3, 4.66], 
                 ['Marito', 'Tasolo', 4, 7, 9, 6.666],
                 ['Esteban', 'Quito', 9, 9, 8, 8.66]]
Tabla = """\
+---------------------------------------------------------------------+
| Nombre    Apellido        Primero Segundo Tercero     Promedio anual|
|---------------------------------------------------------------------|
{}
+---------------------------------------------------------------------+\
"""
Tabla = (Tabla.format('\n'.join("| {:<8} {:<10} {:>8} {:>6} {:>7} {:>23} |".format(*fila)
 for fila in ListasAlumnos)))
print (Tabla)

