#!/usr/bin/env python
#  -*- coding: utf-8 -*-

#Написано сразу и под комбайнер, если припрет, но несколько статистик, в основном запросных - упадут

import sys

from collections import defaultdict

current_key = None
current_ident = None
answer = []

def end_process_query():
    global answer
    global current_key
    imp = answer[0]
    if imp == 0:
        raise Exception("Some exception 6")
    if answer[1] == 0:
        answer[1] = -1
    answer += [answer[1]/imp, answer[2]/imp, answer[3]/imp, answer[4]/imp, answer[5]/imp, answer[6]/imp, answer[6]/answer[1]]
    print ("QQ" + current_key[:-2] + '\t' + ' '.join([str(value) for value in answer]))

def end_process_document():
    global answer
    global current_key
    imp = answer[0]
    if imp == 0:
        raise Exception("Some exception 7")
    if answer[5] == 0:
        if answer[7] != 0:
            raise Exception("Some exception 15")
        answer[5] = -1
    if answer[2] == 0:
        answer[2] = -1
    if answer[6] == 0:
        answer[6] = -1
    if answer[10] + answer[11] == 0:
        answer[10] = -1
    if answer[3] == 0:
        answer[3] = -1
    answer += [answer[1]/imp, answer[2]/imp, answer[3]/imp, answer[4]/imp,
             answer[5]/imp, answer[6]/imp, answer[7]/answer[5], answer[8]/imp,
             answer[8]/answer[5], answer[8]/answer[2], answer[9]/imp,
             answer[9]/answer[6], answer[10]/(answer[10] + answer[11]), answer[12]/imp,
             answer[12]/answer[2], answer[2]/answer[3], answer[13]/imp, answer[14]/imp,
             answer[15]/imp, answer[5]/answer[2], answer[6]/answer[2],
             answer[7]/answer[2], answer[9]/answer[2], answer[10]/answer[2],
             answer[13]/answer[2], answer[14]/answer[2], answer[15]/answer[2], answer[14]/answer[3], answer[16]/answer[6]]

    answer[17] = {region : (answer[17][region] / answer[18][region]) for region in answer[17]}
    answer[19] = {region : (answer[19][region] / answer[18][region]) for region in answer[19]}

    print ("DD" + current_key[:-2] + '\t' + ' '.join([str(value)
    for value in answer[:17] + answer[20:]]) + '@ @' +
    ' '.join([str(i) + ":" + str(q) for i, q in answer[17].items()]) + '@ @' +
     ' '.join([str(i) + ":" + str(q) for i, q in answer[18].items()]) + '@ @' +
     ' '.join([str(i) + ":" + str(q) for i, q in answer[19].items()]))

def end_process_host():
    global answer
    global current_key
    imp = answer[0]
    if imp == 0:
        raise Exception("Some exception 8")
    if answer[5] == 0:
        if answer[7] != 0:
            raise Exception("Some exception 15")
        answer[5] = -1
    if answer[2] == 0:
        answer[2] = -1
    if answer[6] == 0:
        answer[6] = -1
    if answer[10] + answer[11] == 0:
        answer[10] = -1
    if answer[3] == 0:
        answer[3] = -1
    answer += [answer[1]/imp, answer[2]/imp, answer[3]/imp, answer[4]/imp,
             answer[5]/imp, answer[6]/imp, answer[7]/answer[5], answer[8]/imp,
             answer[8]/answer[5], answer[8]/answer[2], answer[9]/imp,
             answer[9]/answer[6], answer[10]/(answer[10] + answer[11]), answer[12]/imp,
             answer[12]/answer[2], answer[2]/answer[3], answer[13]/imp, answer[14]/imp,
             answer[15]/imp, answer[5]/answer[2], answer[6]/answer[2],
             answer[7]/answer[2], answer[9]/answer[2], answer[10]/answer[2],
             answer[13]/answer[2], answer[14]/answer[2], answer[15]/answer[2], answer[14]/answer[3], answer[16]/answer[6]]

    answer[17] = {region : (answer[17][region] / answer[18][region]) for region in answer[17]}
    answer[19] = {region : (answer[19][region] / answer[18][region]) for region in answer[19]}

    print ("HH" + current_key[:-2] + '\t' + ' '.join([str(value)
    for value in answer[:17] + answer[20:]]) + '@ @' +
    ' '.join([str(i) + ":" + str(q) for i, q in answer[17].items()]) + '@ @' +
     ' '.join([str(i) + ":" + str(q) for i, q in answer[18].items()]) + '@ @' +
     ' '.join([str(i) + ":" + str(q) for i, q in answer[19].items()]))

def end_process_query_document():
    global answer
    global current_key
    imp = answer[0]
    if imp == 0:
        raise Exception("Some exception 9")
    if answer[5] == 0:
        if answer[7] != 0:
            raise Exception("Some exception 15")
        answer[5] = -1
    if answer[2] == 0:
        answer[2] = -1
    if answer[6] == 0:
        answer[6] = -1
    if answer[10] + answer[11] == 0:
        answer[10] = -1
    if answer[3] == 0:
        answer[3] = -1

    answer += [answer[1]/imp, answer[2]/imp, answer[3]/imp, answer[4]/imp,
             answer[5]/imp, answer[6]/imp, answer[7]/answer[5], answer[8]/imp,
             answer[8]/answer[5], answer[8]/answer[2], answer[9]/imp,
             answer[9]/answer[6], answer[10]/(answer[10] + answer[11]), answer[12]/imp,
             answer[12]/answer[2], answer[2]/answer[3], answer[13]/imp, answer[14]/imp,
             answer[15]/imp, answer[5]/answer[2], answer[6]/answer[2],
             answer[7]/answer[2], answer[9]/answer[2], answer[10]/answer[2],
             answer[13]/answer[2], answer[14]/answer[2], answer[15]/answer[2], answer[14]/answer[3], answer[16]/answer[6], answer[17]/answer[5]]

    answer[18] = {region : (answer[18][region] / answer[19][region]) for region in answer[18]}
    answer[20] = {region : (answer[20][region] / answer[19][region]) for region in answer[20]}

    print ("QD" + '@ @'.join(current_key[:-2].split('@itsmydelimeteryouknow@')) + '\t' + ' '.join([str(value)
    for value in answer[:18] + answer[21:]]) + '@ @' +
    ' '.join([str(i) + ":" + str(q) for i, q in answer[18].items()]) + '@ @' +
     ' '.join([str(i) + ":" + str(q) for i, q in answer[19].items()]) + '@ @' +
     ' '.join([str(i) + ":" + str(q) for i, q in answer[20].items()]))


def end_process_query_host():
    global answer
    global current_key
    imp = answer[0]
    if imp == 0:
        raise Exception("Some exception 10")

    if answer[2] == 0:
        answer[2] = -1
    answer += [answer[1]/imp, answer[2]/imp, answer[3]/imp, answer[3]/answer[2]]

    print ('QH' + '@ @'.join(current_key[:-2].split('@itsmydelimeteryouknow@')) + '\t' +
    ' '.join([str(q) for q in answer]))

def make_new_answer_query():
    global answer
    global current_key
    answer = [
        0,# Количество показов выдачи по запросу
        0,# Суммарное количество кликов
        0,# Сколько раз не было кликов
        0,# Сколько раз был один клик
        0,# Сколько раз было больше одного клика
        0,# Сколько раз была остановка не на последнем
        0 # Суммарное время просиженное в выдаче
    ]

def make_new_answer_document():
    global answer
    global current_key
    answer = [
        0,# Количество показов
        0,# Сумма позиций
        0,# Количество сессий с кликом
        0,# Количество просмотров
        0,# Сумма позиций показа при котором кликнули
        0,# Количество сессий с несколькими кликами
        0,# Число кликов вообще
        0,# Число кликов при даблклике
        0,# Число возвратных кликов
        0,# Сумма номеров кликов
        0,# Сколько раз останавливали просмотр на этом
        0,# Сколько раз смотрели дальше
        0,# Сколько раз вернулись к этому назад на последнем клике
        0,# Первый клик
        0,# Последний клик
        0,# Единственный клик
        0,# Сумма времени
        defaultdict(int),# словарь регион:ctr
        defaultdict(int),# словарь регион:показы
        defaultdict(int)# словарь регион:последний
    ]

def make_new_answer_host():
    global answer
    global current_key
    answer = [
        0,# Количество показов
        0,# Сумма позиций
        0,# Количество сессий с кликом
        0,# Количество просмотров
        0,# Сумма позиций показа при котором кликнули
        0,# Количество сессий с несколькими кликами
        0,# Число кликов вообще
        0,# Число кликов при даблклике
        0,# Число возвратных кликов
        0,# Сумма номеров кликов
        0,# Сколько раз останавливали просмотр на этом
        0,# Сколько раз смотрели дальше
        0,# Сколько раз вернулись к этому назад на последнем клике
        0,# Первый клик
        0,# Последний клик
        0,# Единственный клик
        0,# Сумма времен
        defaultdict(int),# словарь регион:ctr
        defaultdict(int),# словарь регион:показы
        defaultdict(int)# словарь регион:последний
    ]

def make_new_answer_query_document():
    global answer
    global current_key
    answer = [
        0,# Количество показов
        0,# Сумма позиций
        0,# Количество сессий с кликом
        0,# Количество просмотров
        0,# Сумма позиций показа при котором кликнули
        0,# Количество сессий с несколькими кликами
        0,# Число кликов вообще
        0,# Число кликов при даблклике
        0,# Число возвратных кликов
        0,# Сумма номеров кликов
        0,# Сколько раз останавливали просмотр на этом
        0,# Сколько раз смотрели дальше
        0,# Сколько раз вернулись к этому назад на последнем клике
        0,# Первый клик
        0,# Последний клик
        0,# Единственный клик
        0,# Сумма времен
        0,# Позиция документа при массовом клике
        defaultdict(int),# словарь регион:ctr
        defaultdict(int),# словарь регион:показы
        defaultdict(int)# словарь регион:последний
    ]

def make_new_answer_query_host():
    global answer
    global current_key
    answer = [
        0,# Количество показов
        0,# Средняя позиция
        0,# Был ли клик
        0# Последних кликов
    ]


def process_query(value):
    global answer
    global current_key
    tag, point = value.split(' ')
    if tag == 'imp':
        answer[0] += int(point)
    elif tag == 'mean_num_click':
        point = int(point)
        answer[1] += point
        if point == 0:
            answer[2] += 1
        elif point == 1:
            answer[3] += 1
        if point > 1:
            answer[4] += 1
    elif tag == 'return_click_last':
        point = int(point)
        answer[5] += 1
    elif tag == 'time':
        point = int(point)
        answer[6] += 1
    else:
        raise Exception("Some exception 1")

def process_query_document (value):
    global answer
    global current_key
    tag, point = value.split(' ')
    if tag == 'imp':
        answer[0] += 1
    elif tag == 'mean_pos':
        answer[1] += int(point)
    elif tag == 'region_imp':
        region, num = point.split('@')
        answer[19][region] += int(num)
    elif tag == 'region_ctr':
        region, num = point.split('@')
        answer[18][region] += int(num)
    elif tag == 'double_click':
        answer[5] += 1
        answer[6] += int(point)
        answer[7] += int(point)
    elif tag == 'position_mass_click':
        answer[17] += int(point)
    elif tag == 'return_click':
        answer[8] += 1
    elif tag == 'num_click':
        answer[9] += 1
    elif tag == 'not_last_viewed':
        answer[11] += 1
        answer[3] += 1
    elif tag == 'last_viewed':
        answer[10] += 1
        answer[3] += 1
    elif tag == 'return_click_last':
        answer[12] += 1
    elif tag == 'first_click':
        answer[13] += 1
    elif tag == 'last_click':
        answer[14] += 1
    elif tag == 'region_last':
        region, num = point.split('@')
        answer[20][region] += int(num)
    elif tag == 'only_ctr':
        answer[15] += 1
    elif tag == 'mean_time':
        answer[16] += int(point)
    elif tag == 'position_on_click':
        answer[4] += int(point)
        answer[2] += 1
    elif tag == 'one_click':
        answer[6] += 1
    else:
        raise Exception("Some exception 2")

def process_document(value):
    global answer
    global current_key
    tag, point = value.split(' ')
    if tag == 'imp':
        answer[0] += 1
    elif tag == 'mean_pos':
        answer[1] += int(point)
    elif tag == 'region_imp':
        region, num = point.split('@')
        answer[18][region] += int(num)
    elif tag == 'region_ctr':
        region, num = point.split('@')
        answer[17][region] += int(num)
    elif tag == 'double_click':
        answer[5] += 1
        answer[6] += int(point)
        answer[7] += int(point)
    elif tag == 'return_click':
        answer[8] += 1
    elif tag == 'num_click':
        answer[9] += 1
    elif tag == 'not_last_viewed':
        answer[11] += 1
        answer[3] += 1
    elif tag == 'last_viewed':
        answer[10] += 1
        answer[3] += 1
    elif tag == 'return_click_last':
        answer[12] += 1
    elif tag == 'first_click':
        answer[13] += 1
    elif tag == 'last_click':
        answer[14] += 1
    elif tag == 'region_last':
        region, num = point.split('@')
        answer[19][region] += int(num)
    elif tag == 'only_ctr':
        answer[15] += 1
    elif tag == 'mean_time':
        answer[16] += int(point)
    elif tag == 'position_on_click':
        answer[4] += int(point)
        answer[2] += 1
    elif tag == 'one_click':
        answer[6] += 1
    else:
        raise Exception("Some exception 3")

def process_host(value):
    global answer
    global current_key
    tag, point = value.split(' ')
    if tag == 'imp':
        answer[0] += 1
    elif tag == 'mean_pos':
        answer[1] += int(point)
    elif tag == 'region_imp':
        region, num = point.split('@')
        answer[18][region] += int(num)
    elif tag == 'region_ctr':
        region, num = point.split('@')
        answer[17][region] += int(num)
    elif tag == 'double_click':
        answer[5] += 1
        answer[6] += int(point)
        answer[7] += int(point)
    elif tag == 'return_click':
        answer[8] += 1
    elif tag == 'num_click':
        answer[9] += 1
    elif tag == 'not_last_viewed':
        answer[11] += 1
        answer[3] += 1
    elif tag == 'last_viewed':
        answer[10] += 1
        answer[3] += 1
    elif tag == 'return_click_last':
        answer[12] += 1
    elif tag == 'first_click':
        answer[13] += 1
    elif tag == 'last_click':
        answer[14] += 1
    elif tag == 'region_last':
        region, num = point.split('@')
        answer[19][region] += int(num)
    elif tag == 'only_ctr':
        answer[15] += 1
    elif tag == 'mean_time':
        answer[16] += int(point)
    elif tag == 'position_on_click':
        answer[4] += int(point)
        answer[2] += 1
    elif tag == 'one_click':
        answer[6] += 1
    else:
        raise Exception("Some exception 4")

def process_query_host(value):
    global answer
    global current_key
    tag, point = value.split(' ')
    if tag == 'imp':
        answer[0] += 1
    elif tag == 'mean_pos':
        answer[1] += int(point)
    elif tag == 'last_click':
        answer[3] += 1
    elif tag == 'click':
        answer[2] += 1
    else:
        raise Exception("Some exception 12")

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t', 1)
    if key == '@ErrorError@':
        print ("Error\tError")
    ident = key[-2:]

    if current_key and current_key != key:
        if current_ident == 'QQ':
            end_process_query()
        elif current_ident == 'DD':
            end_process_document()
        elif current_ident == 'HH':
            end_process_host()
        elif current_ident == 'QD':
            end_process_query_document()
        elif current_ident == 'QH':
            end_process_query_host()
        else:
            raise Exception("Some exception 13")

    if current_key is None or current_key != key:
        if ident == 'QQ':
            make_new_answer_query()
        elif ident == 'DD':
            make_new_answer_document()
        elif ident == 'HH':
            make_new_answer_host()
        elif ident == 'QD':
            make_new_answer_query_document()
        elif ident == 'QH':
            make_new_answer_query_host()
        else:
            raise Exception("Some exception 14")

        current_key = key
        current_ident = ident


    if ident == 'QQ':
        process_query(value)
    elif ident == 'QD':
        process_query_document (value)
    elif ident == 'DD':
        process_document(value)
    elif ident == 'HH':
        process_host(value)
    elif ident == 'QH':
        process_query_host(value)
    else:
        raise Exception("Some exception 5")

if current_key:
    if current_ident == 'QQ':
        end_process_query()
    elif current_ident == 'DD':
        end_process_document()
    elif current_ident == 'HH':
        end_process_host()
    elif current_ident == 'QD':
        end_process_query_document()
    elif current_ident == 'QH':
        end_process_query_host()
    else:
        raise Exception("Some exception 13")
