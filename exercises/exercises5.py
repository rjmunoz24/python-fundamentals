# on page 78 of your book, do 5-1 of the try it yourself
# put all your code in your exercise5.py file.
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict false.")
print(car == 'audi')

# 5-1 example
car = 'bmw'
print(car == 'bmw')
print(car != 'bmw')

car = 'audi'
print(car != 'bmw')

# 5-2
car = 'Audi'
print(car.lower() == 'audi')

number = 12
print(number <= 13)
print(number >= 13)

names = ['roberto', 'munoz', 'peter']
print('john' in names)
print('john' not in names)

# write a function that will take 2 arguments.
# inside the function provide examples of all the arithmetic operators.
# provide a variable for each solution and print the results for each

def arithmetic_not(arg1, arg2):
    result = arg1 + arg2
    print(result)
    result = arg1 - arg2
    print(result)
    result = arg1 * arg2
    print(result)
    result = arg1 / arg2
    print(result)


# arithmetic_not(40, 5)


# write a function that take only 1 argument.
# inside the function provide examples of assignment operators:
# modulus equals, minus equals, exponent equals&plus equals.
# provide a variable for each solution and print the results of each
def assign_example(value):
    value %= 40
    print(value)
    value -= 100
    print(value)
    value *= 50
    print(value)
    value /= 5
    print(value)


assign_example(400)




















