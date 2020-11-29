#Crear una función básica:

#Ejemplo de la tabla de multiplicar:
def tablasMultiplicar(x):
    for i in range(1,11):
        print(i," * ",x," = ", i*x)

a    = int(input("Cual tabla de multiplicar desea ver:"))
tablasMultiplicar(a)