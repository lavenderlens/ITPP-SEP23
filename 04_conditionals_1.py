print("Enter the first number: ")
num1 = int(input())
print("Enter the second number: ")
num2 = int(input())
# num1EqualNum2 = num1 == num2
# print("The numbers are equal: " + str(num1EqualNum2))
# num1GreaterThanNum2 = num1 > num2
# print("The first number is greater than the second: " + str(num1GreaterThanNum2))
# num1LessThanNum2 = num1 < num2
# print("The first number is less than the second: " + str(num1LessThanNum2))

if num1 == num2:
    print("The numbers are equal:")
elif num1 > num2:
    print("The first number is greater than the second: ")
elif num1 < num2:
    print("The first number is less than the second: ")
else:
    print("You must enter two numbers")
