#####
#
# Intro to JSON parsing in python
#
#####

import urllib.request
import json


def printResults(data):
    # Use json module to load string data into a dictionary
    theJSON = json.loads(data.decode('utf-8'))
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    # Output number of events
    count = theJSON["metadata"]["count"]
    print(str(count) + " events recorded")

    # # For each event, print where it occured
    # for p in theJSON["features"]:
    #     print(p["properties"]["place"])

    # # Print events thats magnitude is greater than 4
    # for p in theJSON["features"]:
    #     if p["properties"]["mag"] >= 4.0:
    #         # formatting means 2 digits with 1 decimal point that is a floating number (%2.1f)
    #         print("%2.1f" % p["properties"]["mag"], p["properties"]["place"])

    # Print events where something was felt
    print("Events were felt : ")
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if(feltReports != None) & (feltReports > 0):
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + " times.")


def main():
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    webUrl = urllib.request.urlopen(urlData)
    print(webUrl.getcode())
    if(webUrl.getcode() == 200):
        data = webUrl.read()

        # print out results
        printResults(data)
    else:
        print("Error Not Available")

if __name__ == '__main__':
    main()
