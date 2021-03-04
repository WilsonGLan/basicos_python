from googlesearch import search

artista = input("Ingrese el nombre del artista: ")
# cancion = input("Ingrese el nombre de la canción: ")

# titulo_cancion = f"{artista} - {cancion} lyrics"

# urls = search(titulo_cancion, lang, num, stop)
# print(type(urls)," - ", urls)

for j in search(artista, tld="com.co", start=1, stop=10):
    print(j)
