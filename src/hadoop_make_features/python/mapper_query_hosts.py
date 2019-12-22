#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from urlparse import urlparse


for ln in sys.stdin:
    line = ln.strip('\n')
    if len(line) < 6:
        print("$$$fdad!@##$$$ERROR+\t" + '2##@'.join(buf))
        continue
    if line[:2] == 'QQ':
        print (line)
    elif line[:2] == 'QD':
        line = line[2:]
        buf = line.split('\t')
        if len(buf != 2):
            print("$$$fdad!@##$$$ERROR+\t" + '1##@'.join(buf))
            continue
        key, value = buf
        buf = key.split('@ @')
        if len(buf != 2):
            print("$$$fdad!@##$$$ERROR+\t" + '2##@'.join(buf))
            continue
        query, site = buf
        host =

        host =
    elif line[:2] == 'DD':

    elif line[:2] == 'QH':

    elif line[:2] == 'HH':

    else:
    print("Error: " + line)
    count[5] += 1
