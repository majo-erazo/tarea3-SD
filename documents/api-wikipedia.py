import wikipedia
import os

os.makedirs('documents/doc1-5', exist_ok=True)
os.makedirs('documents/doc6-10', exist_ok=True)

# Se generan 10 titulos random
result = wikipedia.random(10)
#print(result)

n = 1
for i in result:
    if n <= 5:
        # Se verifica si el archivo ya existe para no sobreescribir
        if os.path.isfile("documents/doc1-5/Archivo" + str(n) + ".txt") == False:
            archivo = open("documents/doc1-5/Archivo" + str(n) + ".txt", "w")
            # Se extrae el contenido de la pagina i
            texto_page = wikipedia.page(i).content
            # Se escribe en el archivo correspondiente
            archivo.write(texto_page)
            archivo.close
    elif n > 5 and n <= 10:
        if os.path.isfile("documents/doc1-5/Archivo" + str(n) + ".txt") == False:
            archivo = open("documents/doc6-10/Archivo" + str(n) + ".txt", "w")
            texto_page = wikipedia.page(i).content
            archivo.write(texto_page)
            archivo.close
    n += 1 
