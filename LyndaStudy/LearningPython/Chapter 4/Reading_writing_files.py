##########
#
#
# Intro to files
#
##########

def main():
    # # Opens designated file and creates if it doesnt exist
    # # Opens with write functionality
    # file = open("textfile.txt", "w+")

    # Opens with appending text at the end functionality
    # file = open("textfile.txt", "a+")

    # Open file to read
    file = open("textfile.txt", "r")

    #checks that file was opened
    if file.mode== 'r':
    #     # .read() is used to read entire file
    #     contents = file.read()
    #     print(contents)

        fileLine = file.readlines()
        for l in fileLine:
            print(l)

    # # Writes lines to the txt file
    # for i in range(10):
    #     file.write("This is line number %d\r\n" % (i + 1))

    # close the file when finished
    file.close()

if __name__ == '__main__':
    main()
