name = "Alan"
number = 1234
country_code = "IE"
balance = 20.99
has_overdraft = True

# printing strings using Python 2 methods
# could print all these, comma sep,
# automatically running each variable's __str__ builtin metho,
# automatically inserting a space between each entry:
print("Customer name: ", name, "Account No:", number, "Country:", country_code,
      "Account balance: ", balance, "Overdraft facility:", has_overdraft)
# concatenating variales and labels (little strings) into one whole string
print("Customer name: " + name + "Account No:" + str(number) + "Country:" + country_code +
      "Account balance: " + str(balance) + "Overdraft facility:" + str(has_overdraft))
# refactored for spaces
print("Customer name: " + name + " Account No: " + str(number) + " Country: " + country_code +
      " Account balance: " + str(balance) + " Overdraft facility:" + str(has_overdraft))
# refactored for new line characters
print("Customer name: " + name + "\nAccount No: " + str(number) + "\nCountry: " + country_code +
      "\nAccount balance: " + str(balance) + "\nOverdraft facility: " + str(has_overdraft))

# Python 3 placeholders
# successive 3 release improved this greatly for developers
print("Python 3 placeholders")
print("Customer name: {}\nAccount No: {}\nCountry: {} \nAccount balance: {}\nOverdraft facility: {}".format(
    name, number, country_code, balance, has_overdraft))
print("Python 3.5 > placeholders with f-strings")
# lines may be split in editor on a \ character
print(f"Customer name: {name}\nAccount No: {number}\nCountry: {country_code}\
       \nAccount balance: {balance}\nOverdraft facility: {has_overdraft}")
print("Python 3.7 > placeholders with f-strings and triple quotes - single or double")
# no need to split lines on a \ character
# triple quoted strings retain line breaks in code AND indents from LH Margin
print(f"""
Customer name: {name}
Account No: {number + 1}
Country: {country_code}
Account balance: {balance}
Overdraft facility: {has_overdraft}
""")
# values in placeholders may be expressions

# there is an intermediate method using %s and %f placeholders, superceded by the above 3.5-3.7 methods
print("Customer name: %s\nAccount No: %s\nCountry: %s \nAccount balance: %s\nOverdraft facility: %s" % (
    name, number, country_code, balance, has_overdraft))
# we can round numbers using %f for float placeholder
print("Customer name: %s\nAccount No: %s\nCountry: %s \nAccount balance: %f\nOverdraft facility: %s" % (
    name, number, country_code, balance, has_overdraft))  # 20.99
# we can round numbers using %f and padding/rounding number argumants for float placeholder
print("Customer name: %s\nAccount No: %s\nCountry: %s \nAccount balance: %.1f\nOverdraft facility: %s" % (
    name, number, country_code, balance, has_overdraft))  # 21.0
