#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys
import re
import os


for line in sys.stdin:
    line = re.sub(r'\W+',' ',line.strip())
    words = line.split()

    ruta = os.environ['map_input_file']
    lista_ruta = ruta.split("/", 6)
    doc = lista_ruta[6].split('.', 1)[0]
    doc = doc.split('o', 1)[1]

    for word in words:
        print('{}\t{}\t{}'.format(word,1,int(doc)))


