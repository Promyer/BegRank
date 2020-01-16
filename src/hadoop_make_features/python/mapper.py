#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from urlparse import urlparse, ParseResult


with open('urls.dat', 'r') as urls_file, open('hosts.dat', 'r') as hosts_file, open('queries.dat', 'r') as queries_file, \
     open('queries_spell.dat', 'r') as query_spell_file, open('queries_norm.dat', 'r') as queries_norm_file:

    urls = set()
    for url in urls_file:
        urls.add(url.rstrip())

    hosts = set()
    for host in hosts_file:
        hosts.add(host.rstrip())

    queries = set()
    for query in queries_file:
        queries.add(query.rstrip())

    queries_spell = dict()
    for line in queries_spell_file:
        good_query, real_query = line.split('\t')
        queries_spell[good_query] = real_query

    queries_norm = dict()
    for line in queries_norm_file:
        good_query, real_query = line.split('\t')
        queries_norm[good_query] = real_query


    for ln in sys.stdin:
        line = ln.strip('\n')
        itent = line[:2]
        line = line[2:]
        key, value = line.split('\t')

        if itent == 'QQ':

            if key in queries:
                print ("QQ@ @" + line)

            key_spell = queries_spell[key]

        elif itent == 'QD':

            query, url = key.split("@ @")
            parsed_url = urlparse(url)
            url = ParseResult('', *parsed_url[1:]).geturl()[2:]

            if query in queries and url in urls:
                print ('QD@ @' + query + '@ @' + url + '\t' + value.split('@ @')[0])

        elif itent == 'DD':

            parsed_url = urlparse(key)
            url = ParseResult('', *parsed_url[1:]).geturl()[2:]

            if url in urls:
                print ('DD@ @' + url + '\t' + value.split('@ @')[0])

        elif itent == 'QH':

            query, host = key.split("@ @")

            if query in queries and host in hosts:
                print ('QH@ @' + line)

        elif itent == 'HH':

            if key in hosts:
                print ('HH@ @' + key + '\t' + value.split('@ @')[0])

        else:
            print("Error: " + line)
