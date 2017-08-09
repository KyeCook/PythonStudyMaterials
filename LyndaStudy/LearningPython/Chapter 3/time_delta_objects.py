######
#
#
# Introduction to time delta objects and how to use them
#
#
######

from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta


def main():
    # Constructs basic time delta and prints
    print(timedelta(days=365, hours=5, minutes=1))

    # print date
    print("Date now is " + str(datetime.now()))

    # print date in one year by adding 365days on with timedelta
    print("Date in one year will be " + str(datetime.now() + timedelta(days=365)))

    # Use timedelta that has more than one argument
    print("Date in two weeks and 3 days will be : " + str(datetime.now() + timedelta(weeks=2, days=3)))

    # Calculate time one week ago using timedelta and format
    t = datetime.now() - timedelta(weeks=1)
    s = t.strftime("%A %B %d, %Y")
    print("One week ago it was " + s)

    # ## Calculate How long it is until April fools day
    today = date.today()
    afd = date(today.year, 4, 1)

    # Compare dates to see if it has already been.
    # Use replace functin if it has

    if(afd < today):
        print("April fools day has already passed %d days ago" % ((today-afd).days))
        afd = afd.replace(year=today.year+1)

    time_to_afd = abs(afd - today)
    print(time_to_afd.days, " days until next April Fools Day")

if __name__ == '__main__':
    main()