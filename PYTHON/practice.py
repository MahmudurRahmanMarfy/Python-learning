month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def month_in_day(year, month):

    if not 1 < month < 12:

        return 'Invalid Month'

    if month == 2 and is_leap_year(year):

        return 29

    return month_days[month]


print(month_in_day(2017, 2))
