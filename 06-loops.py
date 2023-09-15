band = ["Patti", "Max", "Gary", "Soozie", "Stevie",
        "Nils",
        "Tom", "Clarence", "Jake", "Danny", "Roy"]

# there are two main types of looping or iterative staement in Python:
# for
# while
# that may be used interchangeably but are slightly tweaked to better suit particular applications
# for loops useful where you know the number of iterations in advance
# this could be a counter
# or a collection (which has a length property)
# while loops are more suited for continuous iteration until a stop condition is met

print('using for loop ')
for member in band:
    print(member)

# first variable is arbitarty and stands for each element
# we can call it what we like
# its lifespan is short -
# only as long as it takes for the loop to run
# second variable has to be an iterable
# these include lists and other collection types
# this has to be a real variable name in scope (that the loop code can see)
# its a good idea to name our list variables with plural
# its a good idea to name our first variable in the singular

# while loop
print("while loop with increment")
counter = 0
while counter < len(band):
    # counter is a dynamic variable and changes with each iteration
    print(band[counter])
    counter += 1  # very important to increment/decrement counter here
# print("while loop with decrement")#TODO fix
# counter2 = len(band)
# while counter2 < 0:
#     # counter2 is a dynamic variable and changes with each iteration
#     print(band[counter2 - 1])
#     counter2 -= 1  # very important to increment/decrement counter2 here

# while loop with break
print("using while loop with break")
counter3 = 0
while counter3 < len(band):
    if band[counter3] == "Tom":
        break
    print(band[counter3])
    counter3 += 1
# while loop with continue - skips one iteration only
print("using while loop with continue")
counter4 = 0
while counter4 < len(band):
    if band[counter4] == "Tom":
        counter4 += 1
        continue
        # unreachable code
    print(band[counter4])
    counter4 += 1

# where to use w hile loop without a counter

print('enter any song lyric or x to quit')
lyric = ""
song = ""
# while True:
#     lyric = input()
#     if lyric.lower() == "x":
#         break
#     song += lyric + "\n"
# print(song)

# lower() builtin function converts string to lower case
# upper() builtin function converts string to upper case
# casefold() builtin function converts to lower case and is locale-specific
# in German caps SS is ß

print('SS'.lower())  # ss
print('ss'.upper())  # SS
print('ß'.lower())  # ß
print('ß'.casefold())  # ss
