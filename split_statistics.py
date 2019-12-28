#!/usr/bin/env python
#  -*- coding: utf-8 -*-


import sys


file_name = sys.argv[1] + num
num = sys.argv[2]

host = open("host_stats.dat" + num, 'w')
query_doc = open("duery_document_stats.dat" + num, 'w')
document = open("document_stats.dat" + num, 'w')
query_host = open("query_host_stats.dat" + num, 'w')
query = open("query_stats.dat" + num, 'w')

count = [0] * 6

for line in open(file_name, 'r'):
    if line[:2] == 'QQ':
        query.write(line.strip() + '\n')
        count[0] += 1
    elif line[:2] == 'QD':
        query_doc.write(line.strip() + '\n')
        count[1] += 1
    elif line[:2] == 'DD':
        document.write(line.strip() + '\n')
        count[2] += 1
    elif line[:2] == 'QH':
        query_host.write(line.strip() + '\n')
        count[3] += 1
    elif line[:2] == 'HH':
        host.write(line.strip() + '\n')
        count[4] += 1
    else:
        print ("Error: " + line)
        count[5] += 1

    print ("Found: %d queries, %d query_documents, %d documents, %d query_hosts, %d hosts, %d errors")