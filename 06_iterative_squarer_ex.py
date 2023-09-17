proceed = True
# while True:
while proceed:
    number = int(input("Enter a number to square, or 0 to quit"))
    if number == 0:
        # break
        proceed = False
    else:
        print(number * number)
