#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


with open('urls.dat', 'r') as urls_file, open('hosts.dat', 'r') as hosts_file, open('queries.dat', 'r') as queries_file:

    urls = set()
    for url in urls_file:
        urls.add(url.rstrip())

    queries = set()
    for query in queries_file:
        queries.add(query.rstrip())

    hosts = set()
    for host in hosts_file:
        hosts.add(host.rstrip())

    for ln in sys.stdin:
        line = ln.strip('\n')
        itent = line[:2]
        line = line[2:]
        key, value = line.split('\t')

        if itent == 'QQ':

            if key in queries:
                print ("QQ@ @" + line)

        elif itent == 'QD':

            query, url = key.split("@ @")

            if query in queries and url in urls:
                print ('QD@ @' + key + '\t' + value.split('@ @')[0])

        elif itent == 'DD':

            if key in urls:
                print ('DD@ @' + key + '\t' + value.split('@ @')[0])

        elif itent == 'QH':

            query, host = key.split("@ @")

            if query in queries and host in hosts:
                print ('QH@ @' + line)

        elif itent == 'HH':

            if key in hosts:
                print ('HH@ @' + key + '\t' + value.split('@ @')[0])

        else:
            print("Error: " + line)
