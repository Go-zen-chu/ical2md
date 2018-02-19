#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from dateutil import parser
from icalendar import Calendar

def event2md(event):
    title = event['summary']
    # in some case, description is none
    description = event['description'] if 'description' in event else ''
    return '# {}\n{}\n'.format(title, description)

def convert_ical2md(ical_path, from_date, to_date):
    # summarize in each date
    daily_md = {}
    with open(ical_path) as ic:
        content = ic.read()
        cal = Calendar.from_ical(content)
        event_cnt = 1
        for event in cal.walk('vevent'):
            if event_cnt % 10 == 0:
                print("Working on {} event".format(event_cnt))
            start_dt = event['dtstart'].dt
            if from_date <= start_dt and start_dt <= to_date:
                md = event2md(event)
                if md != None and len(md) > 0:
                    if start_dt in daily_md:
                        daily_md[start_dt].append(md)
                    else:
                        daily_md[start_dt] = [md]
            event_cnt += 1
            # import pprint
            # pprint.pprint(event)
            # event2md(event)
            # break
    print(daily_md)
    # iteritems is only vailable in 2.x
    # for k, v in daily_md.iteritems():
    #
    #     with open()
