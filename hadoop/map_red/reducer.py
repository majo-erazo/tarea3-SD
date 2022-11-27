#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys

current_word = None
current_count = 0
word = None
count_doc = 0

mapa = {}

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t',1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print('{}\t{}'.format(current_word,current_count))
        current_word = word
        current_count = count


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

