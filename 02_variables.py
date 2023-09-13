# variables in Python need to be initialised - declared and assigned a value at the same time
# my_number  # NameError: name 'my_number' is not defined
print("carrying on with rest of program")
my_number = 42

print(my_number)  # 42

print(type(my_number))  # <class 'int'>

# python variables may change their data type and often do, either coerced by us or automatically

my_number = True

print(type(my_number))  # <class 'bool'>

my_number = 43

print(type(my_number))

# in Python, whole numbers are type int, decimal point numbers are type float

division = 9 / 4
print(division)  # 2.25
print(type(division))  # <class 'float'> - shows decimals

my_string = "42"

print(my_string)  # 42
print(type(my_string))  # <class 'str'>

# multiplication
print(my_number * 2)
print(my_string * 2)
print("*" * 50)

# concatenation
print(my_number + my_number)
print(my_string + my_string)

# TypeError: can only concatenate str (not "int") to str
# print(my_string + my_number)
print(my_string + ", " + str(my_number))
print(my_string, my_number)  # also valid

# copying of references:
my_number_2 = my_number
print(my_number_2)
my_number_2 = 99
print(my_number_2)
print(my_number)

# we have looked so far at the Python print() function, for stdout
# let's look at the input() function, for stdin

# print("Enter a number: ")
# my_new_num = input()
# OR, in one line
# my_new_num = input("Enter a number: ")
# print(my_new_num)
# print(type(my_new_num))  # <class 'str'>
# input() always returns a string
# if we want to do math on this string
# we have to convert it to a number

# my_new_num = int(my_new_num)#ValueError: invalid literal for int() with base 10: '2.5'
# ValueError: invalid literal for int() with base 10: '2.5'
# my_new_num = float(my_new_num)  # <class 'float'>
# print(type(my_new_num))  # <class 'int'>

# OR, in one line
my_new_num = float(input("Enter a number: "))
print(type(my_new_num))  # <class 'float'>
# this is not robust if non-digit characters are input
# leads to error:
# ValueError: could not convert string to float:

# to avoid the error and give a chance for the program to recover
# we may use EXCEPTION HANDLING:

# constants are not supported out of the box in Python
# but we may use SCREAMING_SNAKE_CASE to indicate a variable should not be reassigned
