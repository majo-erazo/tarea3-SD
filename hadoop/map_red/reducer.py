#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys

current_word = None
current_doc = None
current_count = 0
word = None
doc = None
dict = {}

for line in sys.stdin:
    line = line.strip()
    word, count, doc = line.split('\t', 3)

    try:
        count = int(count)
    except ValueError:
        continue

    if word not in dict:
        dict[word] = {doc:count}
    else:
        if doc not in dict[word]:
            dict[word][doc] = count
        else:
            dict[word][doc] += 1

print('Word [Doc1, Count1], [Doc2, Count2], ...') 

for palabra, conteo in dict.items():
    print(palabra + "\t")
    for key in conteo:
        #print in one line 
        print('[',key,',',conteo[key],']', end = ' ')
    print("\n")
