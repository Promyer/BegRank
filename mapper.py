#!/usr/bin/env python
import sys

def click_num():
    pass

for line in sys.stdin:

    line = line.strip().split(r'\t')

    query, region = line[0].split("@")
    shown_urls = line[1].split(r',')
    clicked_list = line[2].split(r',')
    clicked_ts = line[3].split(r',')
    hosts = [parse.urlparse(known_url).netloc for known_url in shown_urls]

    for i, s in enumerate(shown_urls):
        print (query + '@itsmydelimeteryouknow@' + s + '\tQD imp 1')
        print (query + '@itsmydelimeteryouknow@' + s + '\tQD mean_position ' + str(i))

        print (s + '\tDD imp 1')
        print (s + '\tDD mean_pos ' + str(i))

    print (query + '\tQQ imp 1')


    for i, s in enumerate(clicked_list):
        print (query + '@itsmydelimeteryouknow@' + s + '\tQD clicks 1')
        print (query + '@itsmydelimeteryouknow@' + s + '\tQD region_ctr ' + region)
        print (query + '@itsmydelimeteryouknow@' + s + '\tQD mean_num_clcik ' + str(i))

        print (s + '\tDD clicks 1')
<<<<<<< HEAD
        print (s + '\tDD region_ctr ' + region)if len(clicked_list) > 1
        print (query + '\tQQ time ' + str(int(clicked_list[-1]) - int(clicked_list[0])))
=======
        print (s + '\tDD region_ctr ' + region)

>>>>>>> c175bb9e96d2cdb5afbae5bdfbad2f6be23e673c
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

    print (query + '\tQQ clicks ' + str(len(clicked_list)))

    if len(clicked_list) > 1:
        print (query + '\tQQ time ' + str(int(clicked_list[-1]) - int(clicked_list[0])))

        mean_t = 0
        for ts in clicked_ts:
            mean_t += int(ts)
        print (query + '\tQQ mean_time ' + str(mean_t))

    elif len(clicked_list) == 0:
        print (query + '\tQQ no_click 1')

    print (query + '\tQQ mean_click ' + str(len(clicked_list)))
    return
