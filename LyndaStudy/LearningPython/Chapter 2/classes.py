########
#
#
# Intro to classes
#
########


class myClass():
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2: " + someString)


class anotherClass(myClass):
    def method1(self):
        print("anotherClass method 1")


def main():
    # Exercise class methods

    c = myClass()

    # calls class methods
    c.method1()
    c.method2("String testing")

    c2 = anotherClass()
    c2.method1()
    c2.method2("This is from the second class")

if __name__ == '__main__':
    main()
