#####
#
# Formatting Dates within Python (Possibly Older method)
#
#####

from datetime import datetime

def main():
    # Time and date formatting
    now = datetime.now()

    # #### Date Formatting ####

    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month

    # strftime takes the control code and pulls it out of the given datetime argument
    # Below string prints full year || If lower case used would just show year (Y = 2017 y = 17)
    print(now.strftime("%Y"))

    # Abbreviated day, month, year string.
    print(now.strftime("%A, %d %B, %Y\n\n ###### \n"))

    # %c = locale control code, %x = locale date, %X locales time
    print(now.strftime("%c \n%x \n%X"))

    # #### Time Formatting ####

    # %I/%H - 12/24hr, %M - minute, %S - second, %p locales AM/PM
    print(now.strftime("%I:%M:%S %p"))

if __name__ == '__main__':
    main()