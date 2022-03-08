# on page 89 of your book, do 5-8 & 5-9 of try it yourself
# 5-8 & 5-9
usernames = ['eric', 'willie', 'admin', 'erin', 'ever']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report")
    else:
        print(f"hello {username}, thank you for logging in again")

usernames = []

if username:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again")
    else:
        print("We need to find some users!")


# 5-11
numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2 :
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")


# 6-1
person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': '43',
    'city': 'sitka',
    }
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])


