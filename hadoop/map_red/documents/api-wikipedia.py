import wikipedia
import os

os.makedirs('hadoop/map_red/documents/doc1-5', exist_ok=True)
os.makedirs('hadoop/map_red/documents/doc6-10', exist_ok=True)

# Se generan 10 titulos random
result = ["Intelligence assessment","Jujutsu Kaisen","One Piece (TV series)","Monkey D. Luffy","Diane Shaw","Artificial intelligence","Greek mythology","Book burning","Cryptography","Information theory"]
#print(result)

URL = open("hadoop/map_red/documents/URLs.txt", "w")
n = 1
for i in result:
    if n <= 5:
        # Se verifica si el archivo ya existe para no sobreescribir
        if os.path.isfile("hadoop/map_red/documents/doc1-5/Archivo" + str(n) + ".txt") == False:
            archivo = open("hadoop/map_red/documents/doc1-5/Archivo" + str(n) + ".txt", "w")
            # Se extrae el contenido de la pagina i
            texto_page = wikipedia.page(i).content

            url = wikipedia.page(i).url
            URL.write("Archivo" + str(n) + ".txt" + "\t" + url + "\n")

            # Se escribe en el archivo correspondiente
            archivo.write(texto_page)
            archivo.close
    elif n > 5 and n <= 10:
        if os.path.isfile("hadoop/map_red/documents/doc1-5/Archivo" + str(n) + ".txt") == False:
            archivo = open("hadoop/map_red/documents/doc6-10/Archivo" + str(n) + ".txt", "w")
            texto_page = wikipedia.page(i).content

            url = wikipedia.page(i).url
            URL.write("Archivo" + str(n) + ".txt" + "\t" + url + "\n")

            archivo.write(texto_page)
            archivo.close
    n += 1 
URL.close