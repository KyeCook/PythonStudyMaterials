###########
#
#
# Conditional (if statements) statements introduction
#
#
###########


def main():
    x, y = 1000, 100

    # Conventional if statement
    if(x < y):
        st = "x is less than y"
    elif(x == y):
        st = "x is equal to y"
    else:
        st = "x is greater than y"
    print(st)

    # conditional statement "a if C else b"ß

    st = "x is less than y" if(x<y) else "x is greater than or equal to y"
    print(st)

if __name__ == '__main__':
    main()