option = int(input("Enter an option in the range 1-3: "))

# traditionally, the swithc functionality in Python was coded other ways:
# there is no switch statement in Python
# for instance as a function using if - elif - else


def switch(option):
    if option == 3:
        print("coleslaw")
        print("fries")
        print("burger")
        print("drink")
    elif option == 2:
        print("fries")
        print("burger")
        print("drink")
    elif option == 1:
        print("burger")
        print("drink")
    else:
        print("Please enter 1, 2 or 3 only")


# switch(option)

# as of Python 3.10 there are the new "soft" keywords match, and case

# match = 1 # they may be used as variable names
# but are also reserved as keywords

match option:
    case 3:
        print("coleslaw")
        print("fries")
        print("burger")
        print("drink")
    case 2:
        print("fries")
        print("burger")
        print("drink")
    case 1:
        print("burger")
        print("drink")
    case _:
        print("Please enter 1, 2 or 3 only")

# match / case statements in Python automatically include "break" functionality in each case
# therefore, the match - case may not be used with additive logic, to cut down on code duplication in each case statement
