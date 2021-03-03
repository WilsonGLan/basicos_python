from googlesearch import search

artista = input("Ingrese el nombre del artista: ")
cancion = input("Ingrese el nombre de la canción: ")

titulo_cancion = f"{artista} - {cancion} lyrics"


lang = "en"
num = 10
stop = 10

urls = search(titulo_cancion, lang, num, stop)
#print(type(urls)," - ", urls)