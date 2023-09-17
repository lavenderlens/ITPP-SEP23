''' 
This exercise is designed to use your knowledge of both conditionals and collections.
Construct a survey using branching logic based on age
the survey is of social media platforms used
and presents a different set of questions for each age range
if age is under 21, the options are, do you use...
    TikTok
    SnapChat
if between 21 - 60, options are
    Facebook
    Twitter
if over 60,
    MySpace
    Reddit
The user, once their age is taken, should be directed 
to the right questions for their age range.
Their answers to the questions should be recorded in a list.
Challenge:
IF the list contains more than one item,
The resultant list should be printed out with the user's age,
and each language choice appended with "first", or "second", in order. 
Do not use a loop for this.

'''
print("SOCIAL MEDIA SURVEY: please enter your age >>>")
age = int(input())
my_socials = []

print("Do you use either of the following: (type Y for yes, N for no)")

if age < 21:
    print("TikTok? Y/N")
    answer = input()
    if answer.upper() == "Y":
        my_socials.append("TikTok")
    print("SnapChat? Y/N")
    answer = input()
    if answer.upper() == "Y":
        my_socials.append("SnapChat")
elif age >= 21 and age <= 60:
    print("Facebook? Y/N")
    answer = input()
    if answer.upper() == "Y":
        my_socials.append("Facebook")
    print("Twitter? Y/N")
    answer = input()
    if answer.upper() == "Y":
        my_socials.append("X")
elif age > 60:
    print("MySpace? Y/N")
    answer = input()
    if answer.upper() == "Y":
        my_socials.append("MySpace")
    print("Reddit? Y/N")
    answer = input()
    if answer.upper() == "Y":
        my_socials.append("Reddit")

# list either has none, one, or two members
if len(my_socials) > 1:
    print(f'''
You are {age} and use
first: {my_socials[0]}
second: {my_socials[1]}
          ''')
elif len(my_socials) == 0:
    print(f'''
You are {age} and do not use any age-appropriate socials
          ''')
else:
    print(f'You are {age} and use {my_socials[0]}')
