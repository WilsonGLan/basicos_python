#Crear una función básica:

#Ejemplo de la tabla de multiplicar:
def tablasMultiplicar(x):
    for i in range(1,11):
        print(i," * ",x," = ", i*x)

a    = int(input("Cual tabla de multiplicar desea ver:"))
tablasMultiplicar(a)

#Ejercicio propuesto por curso Cisco edube.org

'''
Escenario
Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve True si el año es un año bisiesto, o False sí no lo es.
Parte del esqueleto de la función ya está en el editor.
Nota: también hemos preparado un breve código de prueba, que puedes utilizar para probar tu función.
El código utiliza dos listas: una con los datos de prueba y la otra con los resultados esperados. El código te dirá si alguno de tus resultados no es válido.
'''

def isYearLeap(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print(result,"OK")
	else:
		print(result,"Error")


#Ejercicio propuesto por curso Cisco edube.org
'''
Escenario

Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días del mes/año dado (mientras que solo febrero es sensible al valor year, tu función debería ser universal).

La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos no tienen sentido.

Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (LAB 4.1.3.6). Puede ser muy útil. Te recomendamos que utilices una lista con los meses. Puedea crearla dentro de la función; este truco acortará significativamente el código.

Hemos preparado un código de prueba. Amplíalo para incluir más casos de prueba.
'''

def isYearLeap(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def daysInMonth(year, month):
    mesPar = [4,6,9,11]
    mesImpar = [1,3,5,7,8,10,12]
    flag = isYearLeap(year)
    
    if month in mesPar:
        return 30
    elif month in mesImpar:
        return 31
    elif flag == False:
        return 28
    else:
        return 29


testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")

#Ejercicio propuesto por curso Cisco edube.org
'''
Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.

Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código. Esta prueba es solo el comienzo.
'''

def isYearLeap(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def daysInMonth(year, month):
    mesPar = [4,6,9,11]
    mesImpar = [1,3,5,7,8,10,12]
    flag = isYearLeap(year)
    
    if month in mesPar:
        return 30
    elif month in mesImpar:
        return 31
    elif flag == False:
        return 28
    else:
        return 29

def dayOfYear(year, month, day):
    dias=0
    if year>0 and month <= 12 and day <= daysInMonth(year, month):
        for i in range(1,month+1):
            if i < month:       
                dias+=daysInMonth(year, i)
            else:
                dias+=day
        return dias
    else:
        return None

print(dayOfYear(1980, 12, 31))


#Imprimir los números del 1 al 20 que sean primos
def isPrime(num):
    count=0
    for i in range(1,num):
        if num%(i+1)==0 and (i+1)!=num:
            count+=1
    if count > 0:
        return False
    else:
        return True

for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
