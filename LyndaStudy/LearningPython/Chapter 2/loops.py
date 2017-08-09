########
#
#
# Introduction to loops
#
#
########

def main():
    x = 0

    # Defining a while loop
    while (x < 5):
        print(x)
        x =+ 1

    # Defining a for loop
        for x in range(5,10):
            print(x)

    # Looping over a collection (array, list etc.)
        days = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]
        for d in days:
            print(d)

    # Using break and continue in loops
        for x in range(5, 10):
            if(x==7):
                break
            if(x % 2 == 0):
                continue
            print(x)

    # Using enumerate() to get index
        days = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]
        for i, d in enumerate(days):
            print(i, d)


if __name__ == "__main__":
    main()