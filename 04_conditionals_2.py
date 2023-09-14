# if - elif -e;se
# ONE branch

if False:
    print("IF block executed")

# TWO branches - if -else
if False:
    print("IF block executed")
else:
    print("ELSE block excuted")

#  THREE OR MORE branches - if -elif - else
if False:
    print("IF block executed")
elif True:
    print("ELIF block executed")
else:
    print("ELSE block excuted")


#  age problem - nested solution

age = int(input("Enter your age"))
if age < 18:
    print("you are a minor")
else:
    if age > 64:
        print("You are of retirement age")
    else:
        print("You are or working age")
