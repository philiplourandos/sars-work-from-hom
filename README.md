# Introduction

Quick python script to generate a `schedule` of when you worked from home and in the office. The assumution is you spent more time working at home than in the office. SARS require this schedule if you plan on claiming expenses for WFH.

# Setup

* You will need `python3`
* You will need to have `pip` installed
* You will need to install the `arrow` date library: `pip install -U arrow`

# Usage:

`./log --start 2020-03-01 --end 2021-02-28` you will see a file: `wfh.csv`

If you had days in the office you want accounted for on the spreadsheet then use: `./log --start 2020-03-01 --end 2021-02-28 --office office.csv`
Note that the office file will assume that every date(in ISO-8601 format) will be on a new line


