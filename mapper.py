#!/usr/bin/env python

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
    clicked_hosts = [urlparse(known_url).hostname for known_url in clicked_list] #Bad. TODO

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
        print (query + '@itsmydelimeteryouknow@' + url + 'QD' + '\t' + 'mean_pos ' + str(i))
        if i < last_viewed:
            print (query + '@itsmydelimeteryouknow@' + url + 'QD' + '\t' + 'click_bot 1')
            print (url + 'DD' + '\t' + 'click_bot 1')
            print (host + 'HH' + '\t' + 'click_bot 1')

        if i == last_viewed and i > 0:
            print (query + '@itsmydelimeteryouknow@' + url + 'QD' + '\t' + 's_last_viewed 1')
            print (url + 'DD' + '\t' + 'last_viewed_u 1')
            print (host + 'HH' + '\t' + 'last_viewed_u 1')

            if len(session[i][1]) > 1:
                print (query + '@itsmydelimeteryouknow@' + url + 'QD' + '\t' + 'last_click_after_move 1')
                print (url + 'DD' + '\t' + 'last_click_after_move 1')
                print (host + 'HH' + '\t' + 'last_click_after_move 1')

        print (query + '@itsmydelimeteryouknow@' + host + 'QH' + '\t' + 'imp 1')
        print (query + '@itsmydelimeteryouknow@' + host + 'QH' + '\t' + 'mean_pos ' + str(i))


        print (url + 'DD' + '\t' + 'imp 1')
        print (url + 'DD' + '\t' + 'mean_pos ' + str(i))

        print (host + 'HH' + '\t' + 'imp 1')
        print (host + 'HH' + '\t' + 'mean_pos ' + str(i))


    print (query + 'QQ' + '\t' + 'imp 1')
    print (query + 'QQ' + '\t' + 'mean_num_click ' + str(len(clicked_list)))

    for s in clicked_list[:-1]:
        print (query + '@itsmydelimeteryouknow@' + s + 'QD' + '\t' + 'not_last_click 1')
        print (s + 'DD' + '\t' + 'not_last_click 1')

    if len(clicked_list) > 1:
        print (query + '@itsmydelimeteryouknow@' + clicked_list[0] + 'QD' + '\t' + 'first_click 1')
        print (clicked_list[0] + 'DD' + '\t' + 'first_click 1')

        print (query + '@itsmydelimeteryouknow@' + clicked_list[-1] + 'QD' + '\t' + 'last_click 1')
        print (clicked_list[-1] + 'DD' + '\t' + 'last_click 1')

    if len(clicked_list) == 1:
        print (query + '@itsmydelimeteryouknow@' + clicked_list[0] + 'QD' + '\t' + 'only_ctr 1')
        print (clicked_list[0] + 'DD' + '\t' + 'only_ctr 1')

    for t, s in zip([int(clicked_ts[i + 1]) - int(clicked_ts[i]) for i in range(len(clicked_ts) - 1)], clicked_list):
        print (query + '@itsmydelimeteryouknow@' + s + 'QD' + '\t' + 'mean_time ' + str(t))
        print (s + 'DD' + '\t' + 'mean_time ' + str(t))

    for i, act in enumerate(session):

        if len(act[1]) > 0:
            print (query + '@itsmydelimeteryouknow@' + act[0] + 'QD' + '\t' + 'clicks ' + str(len(act[1])))
            print (query + '@itsmydelimeteryouknow@' + act[0] + 'QD' + '\t' + 'region_ctr ' + region + '@' + str(len(act[1])))
            print (query + '@itsmydelimeteryouknow@' + act[0] + 'QD' + '\t' + 'mean_pos_click ' + str(i))
            print (act[0] + 'DD' + '\t' + 'clicks ' + str(len(act[1])))
            print (act[0] + 'DD' + '\t' + 'region_ctr ' + region + '@' + str(len(act[1])))
            print (act[0] + 'DD' + '\t' + 'mean_pos_click ' + str(i))

            for click in act[1]:
                print (query + '@itsmydelimeteryouknow@' + act[0] + 'QD' + '\t' + 'num_of_click ' + str(click))
                print (act[0] + 'DD' + '\t' + 'num_of_click ' + str(click))

        if len(act[1]) > 1:
            print (query + '@itsmydelimeteryouknow@' + act[0] + 'QD' + '\t' + 'double_click ' + str(len(act[1])))
            print (query + '@itsmydelimeteryouknow@' + act[0] + 'QD' + '\t' + 'position_mass_click ' + str(i))
            print (act[0] + 'DD' + '\t' + 'double_click ' + str(len(act[1])))
        if len(act[1]) == 0:
            print (query + '@itsmydelimeteryouknow@' + act[0] + 'QD' + '\t' + 'view_no_click 1')
            print (act[0] + 'DD' + '\t' + 'view_no_click 1')


    if len(clicked_list) > 1:
        print (query + 'QQ' + '\t' + 'time ' + str(int(clicked_ts[-1]) - int(clicked_ts[0])))
