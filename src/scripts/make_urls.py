#!/usr/bin/env python
#  -*- coding: utf-8 -*-

from urllib.parse import urlparse

urls = open("url.data")

host_file = open('hosts.dat', 'w')
url_file = open('urls.dat', 'w')

for line in urls:
    url = line.rstrip().split('\t')[1]
    host = urlparse('//' + url).hostname
    url_file.write(url + '\n')
    if not (host is None):
        host_file.write(host + '\n')