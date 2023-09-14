# name = input("Enter the account name: ")
# number = int(input("Enter the account number: "))
# balance = float(input("Enter the account balance: "))
isTaxable = input("Enter the taxable flag (True or False): ")

if isTaxable == "True":
    isTaxable = True
elif isTaxable == "False":
    isTaxable = False
else:
    print("Enter True or False value only")

print(isTaxable)
