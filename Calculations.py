import datetime
from calendar import monthrange


def calc_easter(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1 + 1
    return month, day


# currentDate = datetime.date.today()
currentDate = datetime.date(2016, 1, 1)
year = currentDate.year
endOfYear = datetime.date(year, 12, 31)
weekend = [5, 6]
easterMonday = calc_easter(year)

if easterMonday[1] > 3:
    month = easterMonday[0]
    friday = easterMonday[1]-3
    easterFriday = (month, friday)
else:
    month = easterMonday[0] - 1
    daysInMonth = monthrange(year, month)
    friday = easterMonday[1] - 3 + daysInMonth
    easterFriday = (month, friday)

holidays = [(1, 1,), (5, 1), (5, 8), (7, 5), (7, 6), (9, 28), (10, 28), (11, 17), (12, 24),
                            (12, 25), (12, 26)]

holidays.append(easterMonday)
holidays.append(easterFriday)

workDayHolidays = 0

for i in holidays:
    date = datetime.date(year, i[0], i[1])
    if date >= currentDate:
        if date.weekday() not in weekend:
            workDayHolidays += 1

print(workDayHolidays)

delta = datetime.timedelta(days=1)
workDays = 0
dateIterator = currentDate
while dateIterator <= endOfYear:
    if dateIterator.weekday() not in weekend:
        workDays += 1
    dateIterator += delta

workDays -= workDayHolidays
print(workDays)
