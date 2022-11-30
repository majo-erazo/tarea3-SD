import json

f1 = open('info.json')
database = json.load(f1)

urls = []
urls.append(0)

f2 = open("documents/URLs.txt", "r")
for line in f2:
    urls.append(line)

#entrada por consola
search = input("Ingrese la palabra a buscar: ")

if(search not in database):
    print ("La palabra no está en la base de datos")
else:
    docs = []
    num = 0
    doc = 0
    for value in database[search]:
        docs.append(value)
        if(num < int(database[search][value])):
            num = database[search][value]
            doc = value
    print("El archivo con más coincidencias es:\n")
    print(urls[int(doc)])
    print("Otros archivos que contienen la palabra:\n")
    for documento in docs:
        if documento != doc:
            print(urls[int(documento)])