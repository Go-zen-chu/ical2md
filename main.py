#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import pytz
import argparse
from datetime import datetime, timedelta
from dateutil import parser
import ical2md

jp_tz = pytz.timezone('Asia/Tokyo')

def parse_args():
    parser = argparse.ArgumentParser(description='Convert ical to markdown')
    today = datetime.today()
    three_day_before = today - timedelta(days=3)
    yesterday = today - timedelta(days=1)

    parser.add_argument('-i', '--ical', type=str, required=True, help='ical file path for input')
    # from/to date for conversion
    parser.add_argument('-f', '--from-date', type=str, default=three_day_before.strftime('%Y-%m-%d'), help='From date')
    parser.add_argument('-t', '--to-date', type=str, default=yesterday.strftime('%Y-%m-%d'), help='To date')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    if os.path.exists(args.ical) == False:
        sys.exit('No such file : {}'.format(args.ical))
    from_dt = parser.parse(args.from_date)
    to_dt = parser.parse(args.to_date)
    jp_from = jp_tz.localize(from_dt)
    jp_to = jp_tz.localize(to_dt)
    ical2md.convert_ical2md(args.ical, jp_from, jp_to)
