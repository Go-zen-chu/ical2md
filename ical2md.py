#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import os
import exceptions
from dateutil import parser
from icalendar import Calendar

def event2md(event):
    title = event['summary']
    # in some case, description is none
    description = event['description'] if 'description' in event else ''
    return '# {}\n{}\n'.format(title, description)

def export_md(export_path, md_date_str, md_list):
    md_path = os.path.join(export_path, md_date_str + '.md')
    if os.path.exists(export_path) == False:
        return exceptions.Exception('No such path : {}'.format(export_path))
    with open(md_path, 'w') as f:
        for md in md_list:
            # md is unicode and has to be encoded
            f.write(md.encode('utf-8'))
    return None

def convert_ical2md(ical_path, export_path, from_date, to_date):
    # summarize in each date
    daily_md = {}
    with open(ical_path) as ic:
        content = ic.read()
        cal = Calendar.from_ical(content)
        event_cnt = 1
        for event in cal.walk('vevent'):
            # check event date
            start_dt = event['dtstart'].dt
            if from_date <= start_dt and start_dt <= to_date:
                md = event2md(event)
                if md != None and len(md) > 0:
                    start_dt_str = start_dt.strftime('%Y-%m-%d')
                    if start_dt_str in daily_md:
                        daily_md[start_dt_str].append(md)
                    else:
                        daily_md[start_dt_str] = [md]
            event_cnt += 1
    # iteritems is only vailable in 2.x
    for md_date_str, md_list in daily_md.iteritems():
        err = export_md(export_path, md_date_str, md_list)
        if err != None:
            return exceptions.Exception("Error while exporting md : {}".format(str(err)))
    return None
