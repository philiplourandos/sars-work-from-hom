#!/bin/env python3

import arrow
import argparse
import io
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--start', help = 'Start date of WFH. ISO8601 date format')
parser.add_argument('--end', help = 'End date of WFH. ISO8601 date format')
parser.add_argument('--office', help = 'File containing ISO-8601 dates when present at the office')

args = parser.parse_args()

start = arrow.get(args.start)
end = arrow.get(args.end)
officeFile = args.office

holidays = []
office = []

if officeFile is not None:
    with open(officeFile, 'r') as at_office:
        file_content = at_office.readlines()

        for office_date in file_content:
            office.append(office_date.strip())

with open('holidays.txt', 'r') as publicHolidays:
    file_content = publicHolidays.readlines()

    for current_line in file_content:
        holidays.append(current_line.strip())

with open('wfh.csv', 'w') as schedule:
    schedule.write('Date, Day, Location\n')

    for current_date in arrow.Arrow.span_range('day', start, end):
        date = current_date[0]

        if date.isoweekday() in range(1,6):
            str_date = date.format("YYYY-MM-DD")

            if str_date in holidays:
                schedule.write(str_date + "," + date.format("dddd") + ",Public Holiday\n")
            elif str_date in office:
                schedule.write(str_date + "," + date.format("dddd") + ",Working at employers office\n")
            else:
                schedule.write(str_date + "," + date.format("dddd") + ",Working from home\n")

