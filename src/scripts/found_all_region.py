#!/usr/bin/env python
#  -*- coding: utf-8 -*-


import sys

file_name = sys.argv[1]

known_regions = set()

for line in open(file_name, 'r'):
    items = line.strip("\n").split("\t")[1].split("@ @")
    if len(items) < 2:
        continue
    asking_regions = items[1:]
    for item in asking_regions:
        dic_points = item.split(" ")
        for point in dic:
            if point != "":
                region, ctr = point.split(":")
                if region in known_regions:
                    continue
                print (region)
