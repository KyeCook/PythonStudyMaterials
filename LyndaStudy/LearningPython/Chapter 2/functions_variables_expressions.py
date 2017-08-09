##############
#
#
# Learning Python Lynda.com Course 1
#   Introduction to functions and variables
#
##############

# Variables
f = 0


def main():
    print("hello world")

    # Below line errors as int and string values can not be concatenated within Python
    # print("printing variable f : " + f)

    # str converts to string to fix previous error
    print("printing variable f : " + str(f))

# If executed as program use below else don't use this.
if __name__ == "__main__":
    main()


def some_function():
    global f
    f = "global variable testing"


# Below Function takes arguments
def function_2(argument1, argument2):
    print(argument1, " ", argument2)


# Function returns value
def function_3(x):
    return x*x*x


# Sets a function that has a default value for one of its arguments
def function_4(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result


# Sets function that can take multiple arguments
def function_5(*args):
    result = 0

    # Loops through given arguments and performs an action
    for x in args:
        result = result + x
    return result


# Calls the function
some_function()
print(f)

# Below shows how to delete via code
# del f

# Sets the arguments for the function
function_2(10, 20)

# prints function output
print(function_3(3))

# ######### Shows function with default argument ####### #

# x has defaulted to 1 so doesn't need to be given
print(function_4(2))

# Python can tell order of arguments so no need to be explicitly stated
print(function_4(2,3))

# Can input arguments in any order if stated explicitly
print(function_4(x=3, num=2))

# Shows function that can take multiple arguments
print(function_5(4, 5, 10, 4))






