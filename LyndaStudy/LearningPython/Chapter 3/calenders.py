######
#
#
# Intro to using calenders within python
#
#
######

import calendar

# Creates a plain text calender

c = calendar.TextCalendar(calendar.SUNDAY)
textCalender = c.formatmonth(2017, 1, 0, 0)
print("TEXT CALENDER\n\n", textCalender)

hc = calendar.HTMLCalendar(calendar.SUNDAY)
htmlCal = hc.formatmonth(2017, 1)
print("HTML CALENDER\n\n", htmlCal)

# Loop over days within the month
# Zeros indicate days that lie within another month

for d in c.itermonthdays(2017, 8):
    print(d)

# Prints days in month for current local
for day in calendar.day_name:
    print(day)

# ###  Calculate days based upon a rule   ###

# Scenario is team is meeting first friday every month
for m in range(1,13):
    # returns array of weeks
    cal = calendar.monthcalendar(2013, m)

    # First friday has to be within two weeks

    weekOne = cal[0]
    weekTwo = cal[1]

    if weekOne[calendar.FRIDAY] != 0:
        meetday = weekOne[calendar.FRIDAY]
    else:
        # If its not in first week must be in second
        meetday = weekTwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))
