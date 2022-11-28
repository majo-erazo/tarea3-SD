import json

archivo = open("output.txt","r")
data = {}

next(archivo)
for line in archivo:
    linea = line.strip()
    word, info = linea.split("\t",1)

    Info = info.split(" ")
    for i in Data:
        # Se reemplazan los parentesis y se separan los elementos
        arch, count = (i.replace("(", "").replace(")", "")).split(",")
        if word in data:
            data[word][arch] = int(count)
        else:
            data[word] = {arch : int(count)}
with open("../info.json", "w") as output:
    json.dump(data, output, indent = 4)