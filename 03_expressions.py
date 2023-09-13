x = 5
y = int("5")
# print(x == y)

# NOT operator and negation

result = 5 != 4  # != is binary not
print(result)  # True
print(not result)  # False
print(result)  # True - value of result not changed
print(5 != 5)  # != is binary not
print(5 == 5)  # != is binary not

has_camera = True
price = 99.95

print(has_camera and price <= 100)  # True
result = has_camera and price <= 100
print(result)  # True
result = not has_camera and price <= 100
print(result)  # False
result = not (has_camera and price <= 100)
print(result)  # False

# compound operators += works for strings and numbers

x = 1
x += 1
x += 1
print(x)

sentence = ''
sentence += 'I '
sentence += 'love '
sentence += 'Python.'

print(sentence)
