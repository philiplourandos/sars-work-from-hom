#!/bin/env python3

import arrow
import argparse
import io
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--start', help = 'Start date of WFH. ISO8601 date format')
parser.add_argument('--end', help = 'End date of WFH. ISO8601 date format')

args = parser.parse_args()

start = arrow.get(args.start)
end = arrow.get(args.end)

with open('wfh.csv', 'w') as schedule:
    schedule.write('Date, Day, Location, Comments\n')

    for current_date in arrow.Arrow.span_range('day', start, end):
        date = current_date[0]

        if(date.isoweekday() in range(1,6)):
            schedule.write(date.format("YYYY-MM-DD") + "," + date.format("dddd") + ", Home Office,,\n")

