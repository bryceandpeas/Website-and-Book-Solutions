"""
Monday 25th April 2016

Codewars Kata - 8 Kyu - Remove the Time

Description:

You're re-designing a blog and the blog's posts have the following format for showing the date and time a post was made:

Weekday Month Day, time e.g., Friday May 2, 7pm

You're running out of screen real estate, and on some pages you want to display a shorter format, Weekday Month Day that omits the time.

Write a function, shortenToDate, that takes the Website date/time in its original string format, and returns the shortened format.

Assume shortenToDate's input will always be a string, e.g. "Friday May 2, 7pm". Assume shortenToDate's output will be the shortened string, e.g., "Friday May 2".

"""

import re

def shorten_to_date(long_date):
    #your code here
    long_date = re.findall('.*?[A-Z].*?[\d]+', long_date)
    return ''.join(long_date)