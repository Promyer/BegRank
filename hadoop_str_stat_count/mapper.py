#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from urlparse import urlparse


for ln in sys.stdin:
    line = ln.strip('\n').split('\t')

    query, region = line[0].split("@")

    shown_urls = line[1].split(r',')

    clicked_list = line[2].split(r',')
    if clicked_list == ['']:
        clicked_list = []

    clicked_ts = line[3].split(r',')
    if clicked_ts == ['']:
        clicked_ts = []

    hosts = [urlparse(known_url).hostname for known_url in shown_urls]

    session = [[x, [], False] for x in shown_urls] # url, [num clciks], is return click

    last_viewed = -1
    for i, site in enumerate(clicked_list):
        url_pos = shown_urls.index(site)
        session[url_pos][1].append(i)
        if url_pos < last_viewed:
            session[url_pos][2] = True
        last_viewed = max(last_viewed, url_pos)

    session = session[:last_viewed + 1]
    if last_viewed == -1:
        session = []

    for i, (url, host) in enumerate(zip(shown_urls, hosts)):
        print (query + '@itsmydelimeteryouknow@' + url + 'QD' + '\t' + 'imp 1')
        print (query + '@itsmydelimeteryouknow@' + url + 'QD' + '\t' + 'mean_pos ' + str(i + 1))

        print (query + '@itsmydelimeteryouknow@' + url + 'QD' + '\t' + 'region_imp ' + region + '@1')
        print (url + 'DD' + '\t' + 'region_imp ' + region + '@1')
        print (host + 'HH' + '\t' + 'region_imp ' + region + '@1')


        if i <= last_viewed:

            if (len(session[i][1]) > 0):
                print (query + '@itsmydelimeteryouknow@' + url + 'QD' + '\t' + 'position_on_click ' + str(i + 1))
                print (url + 'DD' + '\t' + 'position_on_click ' + str(i + 1))
                print (host + 'HH' + '\t' + 'position_on_click ' + str(i + 1))

                if (len(session[i][1]) == 1):
                    print (query + '@itsmydelimeteryouknow@' + url + 'QD' + '\t' + 'one_click 1')
                    print (url + 'DD' + '\t' + 'one_click 1')
                    print (host + 'HH' + '\t' + 'one_click 1')

            print (query + '@itsmydelimeteryouknow@' + session[i][0] + 'QD' + '\t' + 'region_ctr ' + region + '@' + str(len(session[i][1])))
            print (url + 'DD' + '\t' + 'region_ctr ' + region + '@' + str(len(session[i][1])))
            print (host + 'HH' + '\t' + 'region_ctr ' + region + '@' + str(len(session[i][1])))
            if len(session[i][1]) > 1:
                print (query + '@itsmydelimeteryouknow@' + url + 'QD' + '\t' + 'double_click ' + str(len(session[i][1])))
                print (query + '@itsmydelimeteryouknow@' + url + 'QD' + '\t' + 'position_mass_click ' + str(len(session[i][1])))
                print (url + 'DD' + '\t' + 'double_click ' + str(len(session[i][1])))
                print (host + 'HH' + '\t' + 'double_click ' + str(len(session[i][1])))

            if session[i][2]:
                print (query + '@itsmydelimeteryouknow@' + url + 'QD' + '\t' + 'return_click 1')
                print (url + 'DD' + '\t' + 'return_click 1')
                print (host + 'HH' + '\t' + 'return_click 1')

            for clicker in session[i][1]:
                print (query + '@itsmydelimeteryouknow@' + url + 'QD' + '\t' + 'num_click ' + str(clicker + 1))
                print (url + 'DD' + '\t' + 'num_click ' + str(clicker + 1))
                print (host + 'HH' + '\t' + 'num_click ' + str(clicker + 1))

        if i < last_viewed:
            print (query + '@itsmydelimeteryouknow@' + url + 'QD' + '\t' + 'not_last_viewed 1')
            print (url + 'DD' + '\t' + 'not_last_viewed 1')
            print (host + 'HH' + '\t' + 'not_last_viewed 1')

        if i == last_viewed and i > 0:
            print (query + '@itsmydelimeteryouknow@' + url + 'QD' + '\t' + 'last_viewed 1')
            print (url + 'DD' + '\t' + 'last_viewed 1')
            print (host + 'HH' + '\t' + 'last_viewed 1')

        print (query + '@itsmydelimeteryouknow@' + host + 'QH' + '\t' + 'imp 1')
        print (query + '@itsmydelimeteryouknow@' + host + 'QH' + '\t' + 'mean_pos ' + str(i + 1))

        print (url + 'DD' + '\t' + 'imp 1')
        print (url + 'DD' + '\t' + 'mean_pos ' + str(i + 1))

        print (host + 'HH' + '\t' + 'imp 1')
        print (host + 'HH' + '\t' + 'mean_pos ' + str(i + 1))


    print (query + 'QQ' + '\t' + 'imp 1')
    print (query + 'QQ' + '\t' + 'mean_num_click ' + str(len(clicked_list)))

    if len(clicked_list) > 0:
        if shown_urls[last_viewed] != clicked_list[-1]:
            print (query + '@itsmydelimeteryouknow@' + clicked_list[-1] + 'QD' + '\t' + 'return_click_last 1')
            print (clicked_list[-1] + 'DD' + '\t' + 'return_click_last 1')
            print (urlparse(clicked_list[-1]).hostname + 'HH' + '\t' + 'return_click_last 1')
            print (query + 'QQ' + '\t' + 'return_click_last 1')

        if len(clicked_list) > 1:
            print (query + '@itsmydelimeteryouknow@' + clicked_list[0] + 'QD' + '\t' + 'first_click 1')
            print (clicked_list[0] + 'DD' + '\t' + 'first_click 1')
            print (urlparse(clicked_list[0]).hostname + 'HH' + '\t' + 'first_click 1')

            print (query + '@itsmydelimeteryouknow@' + clicked_list[-1] + 'QD' + '\t' + 'last_click 1')
            print (query + '@itsmydelimeteryouknow@' + urlparse(clicked_list[-1]).hostname + 'QH' + '\t' + 'last_click 1')
            print (clicked_list[-1] + 'DD' + '\t' + 'last_click 1')
            print (urlparse(clicked_list[-1]).hostname + 'HH' + '\t' + 'last_click 1')

            print (query + '@itsmydelimeteryouknow@' + clicked_list[-1] + 'QD' + '\t' + 'region_last ' + region + '@1')
            print (clicked_list[-1] + 'DD' + '\t' + 'region_last ' + region + '@1')
            print (urlparse(clicked_list[-1]).hostname + 'HH' + '\t' + 'region_last ' + region + '@1')

            print (query + 'QQ' + '\t' + 'time ' + str(int(clicked_ts[-1]) - int(clicked_ts[0])))

            for hoster in clicked_list:
                print (query + '@itsmydelimeteryouknow@' + host + 'QH' + '\t' + 'click 1')

    if len(clicked_list) == 1:
        print (query + '@itsmydelimeteryouknow@' + clicked_list[0] + 'QD' + '\t' + 'only_ctr 1')
        print (clicked_list[0] + 'DD' + '\t' + 'only_ctr 1')
        print (urlparse(clicked_list[-1]).hostname + 'HH' + '\t' + 'only_ctr 1')

    for t, s in zip([int(clicked_ts[i + 1]) - int(clicked_ts[i]) for i in range(len(clicked_ts) - 1)], clicked_list):
        print (query + '@itsmydelimeteryouknow@' + s + 'QD' + '\t' + 'mean_time ' + str(t))
        print (s + 'DD' + '\t' + 'mean_time ' + str(t))
        print (urlparse(clicked_list[-1]).hostname + 'HH' + '\t' + 'mean_time ' + str(t))
