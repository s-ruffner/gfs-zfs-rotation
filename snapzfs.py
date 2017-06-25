#!/usr/bin/env python
# Some test python code - loops, arrays and functions

# simple iteration loops

for i in range(0, 3):
    print i
    
test_array = ["a", "b", "c", "d"]

from pprint import pprint

pprint(test_array)

# start using the dt functions

# modules we need first

import datetime as dt
import calendar as calendar

# some data strutures and variables

# How many of each type of backup we are keeping

yearly = 3
monthly = 6
weekly = 4
daily = 7
hourly = 4


todays_snaps = []

today = dt.datetime.now()

# Loop through to set up the list of snapshots
# Yearly snaps - first of the calendar year

for i in range(0, yearly):   
    year = dt.datetime(today.year - i, 1, 1, 0, 0)
    print year.strftime("%Y-%m-%d-%H-%M")

# Monthly snaps - first of the calendar month
for i in range(0, monthly):
    month = dt.datetime(today.year, today.month - i, 1, 0, 0)
    print month.strftime("%Y-%m-%d-%H-%M")

# Weekly - this is a little different because we don't care about the calendar,
# but instead the day of the week; these are Saturday night (Sun at 12AM)
for i in range(0, yearly):
   #  delta = dt.timedelta(days=i*365)
    week = = dt.datetime(today.year, today.month, today.day - (today.weekday() + 1 ), 0, 0)
    print yearly.strftime("%Y-%m-%d-%H-%M")

# Daily - the past N days
for i in range(0, yearly):
   #  delta = dt.timedelta(days=i*365)
    yearly = dt.datetime(today.year - i, 1, 1, 0, 0)
    print yearly.strftime("%Y-%m-%d-%H-%M")


for i in range(0, yearly):
   #  delta = dt.timedelta(days=i*365)
    yearly = dt.datetime(today.year - i, 1, 1, 0, 0)
    print yearly.strftime("%Y-%m-%d-%H-%M")
