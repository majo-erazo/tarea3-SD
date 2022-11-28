import json

archivo = open("output.txt","r")
data = {}

next(archivo)
for line in archivo:
    linea = line.strip()
    if linea == '':
        continue
    else:
        word, info = linea.split(' ',1)

        Info = info.split("]")
        for i in Info:
            # Se reemplazan los parentesis y se separan los elementos
            conjunto = (i.replace("[","")).split("]")

            if conjunto[0] == '':
                continue;
            else:
                arch, count = conjunto[0].split(",")
                arch = arch.replace(",","")
                count = count.replace(",","")

            if word not in data:
                data[word] ={ arch:int(count)}
            else:
                data[word][arch] = int(count)
print(data)



with open("../info.json", "w") as output:
    json.dump(data, output, indent = 4)
                                          