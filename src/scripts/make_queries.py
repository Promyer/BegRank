#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import requests
from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation

mystem = Mystem()
russian_stopwords = stopwords.words("russian")

queries = open("queries.tsv")

query_file = open('queries.dat', 'w')
query_spell_file = open('queries_spell.dat', 'w')
query_normalise_file = open('queries_norm.dat', 'w')

for line in queries:
    query = line.rstrip().split('\t')[1]
    query_file.write(query + '\n')

    spellchecked = query
    answer = requests.get('https://speller.yandex.net/services/spellservice.json/checkText?text='
                            + '+'.join(query.split(' ')) + '&options=516').json()
    for error in answer:
        if error['code'] != 1:
            print (answer)
            print (query)
        spellchecked = spellchecked[:error['pos']] + error['s'][0] + spellchecked[error['pos'] + error['len']:]

    if spellchecked != query and spellchecked != '':
        print (spellchecked)
        print(query)
        query_spell_file.write(spellchecked + '\t' + query + '\n')

    tokens = mystem.lemmatize(spellchecked.lower())
    tokens = [token for token in tokens if token not in russian_stopwords and token != " " and token.strip() not in punctuation]
    normalised = " ".join(tokens)

    if normalised != spellchecked and normalised != '':
        query_normalise_file.write(normalised + '\t' + query + '\n')