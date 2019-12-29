#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import sys
from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation

stemmer = Mystem()
russian_stopwords = stopwords.words("russian")

#Preprocess function
def preprocess_text(text):
    tokens = stemmer.lemmatize(text.lower())
    tokens = [token for token in tokens if token not in russian_stopwords\
              and token != " " \
              and token.strip() not in punctuation]

    text = " ".join(tokens)

    return text
file = open(sys.argv[1], "r")
titles = open("title_normalized_" + sys.argv[1], "w")
bodies = open("bodies_normalized_" + sys.argv[1], "w")
for line in file:
    try:
        num, title, body = line.strip().split("\t")
        titles.write(num + "\t" + preprocess_text(title))
        bodies.write(num + "\t" + preprocess_text(body))
    except:
        continue