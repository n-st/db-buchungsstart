#!/usr/bin/env python
# coding: utf-8

import datetime

def timetable_startday(year: int):
    # DB timetable changeover is always on (the start of) the second Sunday in December
    startpoint = datetime.date(year=year, month=12, day=8)
    # 0=Monday ... 6=Sunday
    startpoint_weekday = startpoint.weekday()
    # We want Sunday (weekday 6), so add however many days we're missing
    actualdate = startpoint + datetime.timedelta(days=6-startpoint_weekday)
    return actualdate

def booking_startday(year: int):
    # Bookings for after the timetable changeover are usually possible from "mid October"
    # Although there is no official rule, this date seems to always be the Wednesday exactly 60 days before the timetable changeover. (Verified for 2021, 2022, 2023)
    return timetable_startday(year) - datetime.timedelta(days=60)

def get_earliest_booking_date(date: datetime.date):
    # in the given year, we can only "easily" book dates until the day before the timetable change
    easyrange_end = timetable_startday(date.year) - datetime.timedelta(days=1)
    # and we can only start booking in October, so "easy" booking starts at (October date + 180 days)
    easyrange_start = booking_startday(date.year-1) + datetime.timedelta(days=179)

    if easyrange_start <= date <= easyrange_end:
        return date - datetime.timedelta(days=179)
    elif date < easyrange_start:
        return easyrange_start - datetime.timedelta(days=179)
    else:
        return booking_startday(date.year)


def human_readable():
    today_year = datetime.date.today().year
    for year_offset in [0, 1]:
        year = today_year + year_offset
        d = datetime.date(year=year, month=1, day=1)
        while d.year == year:
            print('Tickets for', d, 'are expected to be bookable from', get_earliest_booking_date(d))
            d += datetime.timedelta(days=1)

def ical_output():
    import icalendar
    import pytz
    cal = icalendar.Calendar()
    cal.add('prodid', '-//DB-Buchungsstart-Rechner//mxm.dk//')
    cal.add('version', '2.0')
    today_year = datetime.date.today().year
    for year_offset in [0, 1]:
        year = today_year + year_offset
        d = datetime.date(year=year, month=1, day=1)
        while d.year == year:
            bookable_from = get_earliest_booking_date(d)
            event = icalendar.Event()
            event.add('summary', 'DB-Buchung ab %s' % bookable_from.isoformat())
            event.add('dtstart', d)
            event.add('dtstamp', datetime.datetime.now())
            cal.add_component(event)
            d += datetime.timedelta(days=1)
    print(cal.to_ical().decode("utf-8")) 
