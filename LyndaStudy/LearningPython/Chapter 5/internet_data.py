#####
#
#
# Intro to working with web data
#
#####

import urllib.request

def main():
    # Open connection to URL using urllib
    webUrl = urllib.request.urlopen("http://google.com")

    # Get result code and print it
    ## Example 200 = good, 404 = error etc
    print("Result code : " +str(webUrl.getcode()))

    # Call read funtion from URL and print it
    data = webUrl.read()
    print(data)

if __name__ == '__main__':
    main()
