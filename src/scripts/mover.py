#!/usr/bin/env python
#  -*- coding: utf-8 -*-

from urlparse import urlparse

urls = open("/home/miroslavmorozov/Загрузки/url.data")
queries = open("/home/miroslavmorozov/Загрузки/queries.tsv")

urls = open("/home/miroslavmorozov/Загрузки/url.data")
queries = open("/home/miroslavmorozov/Загрузки/queries.tsv")

host_file = open('hosts.dat', 'w')
url_file = open('urls.dat', 'w')
query_file = open('queries.dat', 'w')

for line in urls:
    url = line.split('\t')[1]
    host = urlparse('//' + url).hostname
    url_file.write(url + '\n')
    if not (host is None):
        host_file.write(host + '\n')

for line in queries:
    query = line.split('\t')[1]
    query_file.write(query + '\n')
