texto = input("Please, enter palindrome: ")
lista_palabra = []

for letra in range(len(texto)):
    if texto[letra] != " ":
        lista_palabra.append(texto[letra].lower())

for indice in range(len(lista_palabra)):
    if lista_palabra[indice] != lista_palabra[(indice+1)*-1]:
        print("It's not a palindrome")
        break
else:
    print("It's a palindrome")
