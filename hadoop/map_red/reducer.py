#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys

current_word = None
current_doc = None
current_count = 0
word = None
<<<<<<< Updated upstream
count_doc = 0

mapa = {}
=======
doc = None
>>>>>>> Stashed changes

for line in sys.stdin:
    line = line.strip()
    word, count, doc = line.split('\t',2)


    dic_aux = {
        doc:count
    }

    dic = {
        word:dic_aux
    }

    
    try:
        count = int(count)
    except ValueError:
        continue
    
    

    if current_word == word:
        current_count += count
        current_doc = doc
        if current_word in dic:
            if current_doc in dic[current_word]:
                dic[current_word][current_doc] = current_count
            else:
                dic[current_doc] = current_count
    else:
        if current_word:
            print('{}\t{}\t{}'.format(current_word,current_count,current_doc))
        current_word = word
        current_count = count
        current_doc = doc

    if word in mapa:
        if count_doc not in mapa[word]:
            mapa[word] = {count_doc:current_count}
        else:
            mapa[word][count_doc] = current_count

    else:
        mapa = {word:{count_doc:current_count}}

    print(mapa)



if current_word == word:
    print('{}\t{}'.format(current_word,current_count))

