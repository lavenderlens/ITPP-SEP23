# name = input("Enter the account name:")#no coercion necessary

name = 'Alan'

# number = int(input("Enter the account number:"))
# #need to coerce to whole number type
number = 123456

# countryCode = input("Enter the country code")
countryCode = "IE"

# balance = float(input("Enter the account opening balance:"))
# #need to coerce to floating point number type
balance = 89.99

hasOverdraft = input("Overdraft facility? True or False")
#need to coerce to Boolean
# hasOverdraft = False

# print(bool(''))
# print(bool(0))
# print(bool('any string at all'))
# print(bool(1))

if hasOverdraft.lower() == "y" or hasOverdraft.lower() == "true":
    hasOverdraft = True
elif hasOverdraft.lower() == "n" or hasOverdraft.lower() == "false":
    hasOverdraft = False
else:
    hasOverdraft = "Please enter exactly True or False"

print(type(hasOverdraft))

#inside a print statement, print() works out the string values of each different type
print(name)
print(number)
print(countryCode)
print(balance)
print('has od?', hasOverdraft)

#inside a print statement with string concatenation
print('name: ' + name)
print(type(name))
print('account number: ' + str(number))
print(type(number))
print('country code: ' + countryCode)
print(type(countryCode))
print('account balance: ' + str(balance))
print(type(balance))
print('Overdraft enabled? ' + str(hasOverdraft))
print(type(hasOverdraft))

#Python 3 placeholders
print("Using placeholders, Python 3>")
print(
    'Account no. {} Name: {} country code: {} balance: £{} has overdraft? {}.'
.format(number, name, countryCode, balance, hasOverdraft)
)
#for this you must have the same number, and right order of arguments

print("Using placeholders with f, Python 3.5>")
print(
    f'Account no. {number} \nName: {name} \ncountry code: {countryCode} \nbalance: £{balance} \nhas overdraft? {hasOverdraft}.'
)

number = 987654

print(
    f'Account no. {number} \nName: {name} \ncountry code: {countryCode} \nbalance: £{balance} \nhas overdraft? {hasOverdraft}.'
)#placeholder variables update if their value changes

print("Using placeholders with f string ''', Python 3.7>")

print(
f'''
Account no. {number} 
Name: {name} 
country code: {countryCode} 
balance: £{balance} 
has overdraft? {hasOverdraft}.
'''
)




