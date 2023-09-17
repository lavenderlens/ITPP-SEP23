# what is a function?
# a function is one or more LOC wrapepd up in a variable name
# that may be called one or more times at some point in the future
# Python functions must be defined, using the def keyword, before they are used
# a function can be as little as one line
# a function can be  any number of lines but should be kept as short as possible.
# why?
# if we get to say 50 lines a function may well have external dependencies
# it may reference some other part of your code
# a function should be idempotent - it should give the same result for multiple calls
# it won't do this if it has an external dependency

import copy
my_name = "alan"  # external dependency
# define function
# impure function - has external dep


def greet_impure():
    print("Hello " + my_name)


# call function
greet_impure()
greet_impure()

my_name = "Mark"  # external dependency changes

greet_impure()  # different result - not idempotent

# pure function - no deps


def greet_pure(my_name):
    print("Hello " + my_name)


greet_pure("Alan")
greet_pure("Alan")
greet_pure("Alan")
greet_pure("Mark")

# ideally, all our function sshould be pure
# external deps make testing harder
# function looking too big? compose it from smaller individual functions

# function syntax
# functions can have:
# input
# output
# both
# neither

# input: parameters in the round brackets
# output: a return statement
# print output is not considered function output
# once print runs, data passed to it does not persist
# a return statement enables the coder to capture data
# and pass it on to other parts of the app


# candidate staements for a function:
print('Hello')
print('World')
print('How are you?')

# 1. no input, no output


def greet():  # define function
    print('Hello')
    print('World')
    print('How are you?')


greet()  # call function
output = greet()  # output may not be persisted
print(output)  # None (equivalent of null in other languages)

# 2. no input, output


def greet2():
    return 'Hello greet2 \nWorld \nHow are you?'


greet2()  # can't see output printed anywhere
print(greet2)  # <function greet2 at 0x102ec1800>
print(greet2())  # output passed as input to print() function
output2 = greet2()
print(output2)

# 3. input, output


def greet3(name):
    return f'Hello greet3 \n{name} \nHow are you?'
    # unreachable


print(greet3("Amy"))

# rules of return statements
# return should always be the LAST statement in a function
# code underneath the return statement in the same block is unreachable
# a function may have multiple return statements
# but each will be at the end of their particular block
# multiple returns just means multiple branching logic within the function
# a return state,emt must only return ONE value or expression
# that may be a complex expression

# example multiple returns


def isYourNameAlan():
    name = input("Enter your name: ")
    if name.lower() != "alan":
        return None  # return 1
    return name  # return 2

# 4. input, no output


def greet4(name):
    print('Hello greet4')
    print(name)
    print('How are you?')


greet4("Peter")


###################
# COPYING IN PYTHON
###################

my_list = [1, 2, 3]

# SHALLOW copying copies reference only
# DEEP copying copies contents and breaks reference to the original

# shallow copy of reference only
my_list_copy = my_list
# are these truly independent
# or does one still maintain a ref to the other?
print(my_list_copy)
print(my_list)
my_list_copy.append(4)
print(my_list_copy)
print(my_list)  # original affected through the new ref

# shallow copy using copy()
my_list = [1, 2, 3]  # reset
my_list_copy = copy.copy(my_list)
my_list_copy.append(4)
print(my_list_copy)
print(my_list)  # original unchanged

my_recursive_list = [1, 2, 3, [4, 5, 6]]
my_recursive_list_copy = copy.copy(my_recursive_list)
my_recursive_list_copy.append(4)
print(my_recursive_list_copy)
print(my_recursive_list)  # original unchanged

my_recursive_list_recursive_copy = copy.copy(my_recursive_list)
my_recursive_list_recursive_copy[3].append(7)
print(my_recursive_list_recursive_copy)  # [1, 2, 3, [4, 5, 6, 7]]
print(my_recursive_list)  # [1, 2, 3, [4, 5, 6, 7]] - original changed

# deep copying using copy.deepcopy()
my_recursive_list = [1, 2, 3, [4, 5, 6]]  # reset
my_recursive_list_recursive_copy = copy.deepcopy(my_recursive_list)
my_recursive_list_recursive_copy[3].append(7)
print(my_recursive_list_recursive_copy)  # [1, 2, 3, [4, 5, 6, 7]]
print(my_recursive_list)  # [1, 2, 3, [4, 5, 6]]
