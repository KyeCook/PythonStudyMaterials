#########
#
#
# Introduction to importing libraries contained within Python (specifically dates)
#
#
##########


from datetime import date
from datetime import time
from datetime import datetime


def main():
    # **** Date objects ****

    # Get todays date
    today = date.today()
    print("Todays date is ", today)

    # Individual Dates
    print("Date components are : ", today.day, today.month, today.year)

    # Retrieve todays weekday number (index)
    print("Todays index is : ", today.weekday())

    # **** Date Time Objects ***
    today = datetime.now()
    print("The current date and time is ", today)

    # Finding current time
    currentTime = datetime.time(datetime.now())
    print("the current time is ", currentTime)

    # Weekday returns index for current weekday (0 for monday through 6 for Sunday)
    wd = date.weekday(today)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    print("Today is day number %d" % wd)
    print("Today is a ", days[wd])

if __name__ == '__main__':
    main()
