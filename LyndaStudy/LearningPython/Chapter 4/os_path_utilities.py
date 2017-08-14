#####
#
#
# Intro to path utilities in python
#
#####

import os
from os import path

import time
import datetime
from  datetime import date, timedelta


def main():
    # Prints name of os
    print(os)

    # Check for item existence
    print("Item exits : " + str(path.exists("textfile.txt")))
    print("Item is a file : " + str(path.isfile("textfile.txt")))
    print("Item is a directory : " + str(path.isdir("textfile.txt")))

    # Use file paths
    print("Items file path (pwd) : " + str(path.realpath("textfile.txt")))
    # Split files name and path to allow each to be manipulated separably
    print("Items path and name is : " + str(path.split(path.realpath("textfile.txt"))))

    # Check modifcation time
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # Calculate how long ago file was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been " + str(td) + " since the file was modified")
    print("Or, " +str(td.total_seconds()) + " seconds")

if __name__ == '__main__':
    main()
