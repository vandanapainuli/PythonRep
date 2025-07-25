
import datetime
import inspect

print(inspect.getfile(datetime))

#this program gave the path of all in built mython modules in my system
#when I run this program, it gave the path of datetime module
#below is the content of datetime.py file

"""For when pip wants to check the date or time.
"""

import datetime


def today_is_later_than(year: int, month: int, day: int) -> bool:
    today = datetime.date.today()
    given = datetime.date(year, month, day)

    return today > given
