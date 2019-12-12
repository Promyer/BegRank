#!/usr/bin/env python
import sys

current_key = None
answer = []

def print_last_value(key, values):
    print (current_key + '\t' + ' '.join([str(value) for value in values]))

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t', 1)
    ident = key[-2:]
    value = [2:]
    mark, down = value[3:].split(' ')

    if ident == 'QQ':
        process_query()

    elif ident == 'QD':
        process_query_document (key[:-2], )

    elif ident == 'DD':
        process_document(key[:-2], )

    elif ident == :
        process_(key[:-2],)

    elif ident == :
        process_(key[:-2],)


    if current_key is None or key != current_key:

        if current_key:
            print_last_value(current_key, answer)

            answer = [0,#Количество показов выдачи по запросу
                  0,#Суммарное количество кликов
                  0,#Сколько раз не было кликовую
                  0,#Сколько раз был один клик
                  0,#Сколько раз было больше одного клика
                  0 #Суммарное время просиженное в выдаче
                  ]
    process (ident, , value, answer)


    elif ident == 'QD':
        ctr = 0
        imp = 0

    elif ident == 'DD':
        ctr = 0
        imp = 0

    elif ident == 'QH':

    elif ident == 'HH':
    print (1)

if current_key:
    #Вывод ответа