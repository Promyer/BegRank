#!/usr/bin/env python
import sys
from urlparse import urlparse

def click_num():
    pass

for ln in sys.stdin:
    line = ln.strip().split('\t')
    query, region = line[0].split("@")
    shown_urls = line[1].split(r',')
    clicked_list = line[2].split(r',')
    clicked_ts = line[3].split(r',')
    hosts = [urlparse(known_url).hostname for known_url in shown_urls]
    clicked_hosts = [urlparse(known_url).hostname for known_url in clicked_list] #Bad. TODO

    session = [[x, []] for x in shown_urls]

    last_viewed = 0
    for i, site in enumerate(clicked_list):
        url_pos = shown_urls.index(site)
        session[url_pos][1].append(i)
        last_viewed = max(last_viewed, url_pos)

    session = session[:last_viewed]


    for i, (url, host) in enumerate(zip(shown_urls, hosts)):
        print (query + '@itsmydelimeteryouknow@' + url + '\tQD imp 1')
        print (query + '@itsmydelimeteryouknow@' + url + '\tQD mean_position ' + str(i))

        print (query + '@itsmydelimeteryouknow@' + host + '\tQH imp 1')
        print (query + '@itsmydelimeteryouknow@' + host + '\tQH mean_position ' + str(i))


        print (url + '\tDD imp 1')
        print (url + '\tDD mean_pos ' + str(i))

        print (host + '\tHH imp 1')
        print (host + '\tHH mean_pos ' + str(i))


    print (query + '\tQQ imp 1')


    for i, s in enumerate(clicked_list):
        print (query + '@itsmydelimeteryouknow@' + s + '\tQD clicks 1')
        print (query + '@itsmydelimeteryouknow@' + s + '\tQD region_ctr ' + region)
        print (query + '@itsmydelimeteryouknow@' + s + '\tQD mean_num_clcik ' + str(i))

        print (s + '\tDD clicks 1')
        print (s + '\tDD region_ctr ' + region)

	print (s + '\tDD mean_num_clcik ' + str(i))

    for s in clicked_list[:-1]:
        print (query + '@itsmydelimeteryouknow@' + s + '\tQD not_last_click 1')
        print (s + '\tDD not_last_click 1')

    if len(clicked_list) > 0:
        print (query + '@itsmydelimeteryouknow@' + clicked_list[0] + '\tQD first_click 1')
        print (clicked_list[0] + '\tDD first_click 1')

        print (query + '@itsmydelimeteryouknow@' + clicked_list[-1] + '\tQD last_click 1')
        print (clicked_list[-1] + '\tDD last_click 1')

    if len(clicked_list) == 1:
        print (query + '@itsmydelimeteryouknow@' + clicked_list[0] + '\tQD only_ctr 1')
        print (clicked_list[0] + '\tDD only_ctr 1')
        print (query + '\tQQ only_one 1')

    for t, s in zip([int(clicked_ts[i + 1]) - int(clicked_ts[i]) for i in range(len(clicked_ts) - 1)], clicked_list):
        print (query + '@itsmydelimeteryouknow@' + s + '\tQD mean_time ' + str(t))
        print (s + '\tDD mean_time ' + str(t))

    for act in session:
        if len(act[1]) > 1:
            print (query + '@itsmydelimeteryouknow@' + act[0] + '\tQD double_click 1')
            print (act[0] + '\tDD double_click 1')
        if len(act[1]) == 0:
            print (query + '@itsmydelimeteryouknow@' + act[0] + '\tQD view_no_click 1')
            print (act[0] + '\tDD view_no_click 1')

    print (query + '\tQQ clicks ' + str(len(clicked_list)))

    if len(clicked_list) > 1:
        print (query + '\tQQ time ' + str(int(clicked_ts[-1]) - int(clicked_ts[0])))

        mean_t = 0
        for ts in clicked_ts:
            mean_t += int(ts)
        print (query + '\tQQ mean_time ' + str(mean_t))

    elif len(clicked_list) == 0:
        print (query + '\tQQ no_click 1')

    print (query + '\tQQ mean_click ' + str(len(clicked_list)))
