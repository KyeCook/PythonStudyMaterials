#####
#
# Simple HTML parsing in python
#
#####

from html.parser import HTMLParser

metacount = 0


class MyHTMLParser(HTMLParser):

    # ## TODO this doesnt work : Due to this being python 3 ##
    # Function to handle opening tag
    def handle_starttag(self, tag, attrs):
        global metacount
        print("Encountered a meta tag : ", tag)
        if(tag == "meta"):
            metacount += 1

        pos = self.getpos()
        print("At line : ", pos[0], " position ", pos[1])
        if attrs.__len__> 0:
            print("\tAttributes:")
            for a in attrs:
                print("\t", a[0], "=", a[1])

    # Function to handle closing tag
    def handle_endtag(self, tag):
        print("Encounted Endtag:", tag)
        pos = self.getpos()
        print("At line : ", pos[0], " position ", pos[1])

    # Handles character and text data (Tag contents)
    def handle_data(self, data):
        print("Encounted some data : ", data)
        pos = self.getpos()
        print("At line : ", pos[0], " position ", pos[1])

    # Handles comments
    def handle_comment(self, data):
        print("Encountered comment : ", data)
        pos = self.getpos()
        print("At line : ", pos[0], " position ", pos[1])


def main():

    # Initiate parser and feed HTML
    parser = MyHTMLParser()

    # Open sample HTML File and read it
    f = open("samplehtml.html")

    if f.mode == "r":
        contents = f.read() # reads entire file
        parser.feed(contents)

    print("Meta total was ", metacount)

if __name__ == '__main__':
    main()
