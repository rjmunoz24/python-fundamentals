# lesson 9 classes & functions

# basic class definition
class Cat:
    # class variable
    kind = 'feline'

    # constructor
    def __init__(self, name, color):
        # instance variables
        self.name = name
        self.color = color

    # basic method
    def cat_color(self):
        return self.color

    def cat_name(self):
        return self.name


# object creation
my_cat = Cat('Felix', 'white')
my_other = Cat('Garfield', 'orange')

# method is shared by all created object
print(my_cat.cat_name())
print(my_cat.cat_color())
print(my_other.cat_color())

# name is unique to the create object
print(my_cat.name)
print(my_other.name)

# kind is shared by all created objects
print(my_other.kind)


# Function Review
# keyword argument allows you to change the order of the function parameters
# when calling that method.
def my_fancy_function(arg, arg2):
    print(arg + ' = ' + arg2)


# normal function call
# my_fancy_function('Friday', 'Fun')

# keyword = function call
# my_fancy_function(arg2 = 'weekend', arg='saturday')

# arbitrary arguments allow for many arguments that are unknown
# using *args and **kwargs will help define these arguments


# *args will allow a tuple of arguments
def favorite_color(*colors):
    print('My favorite color is ' + colors[1])


# favorite_color('red', 'blue', 'green')

# tuple of colors
# *args takes a tuple in values, but not as a variable. You will generate
# an error if you push a tuple variable directly
# favs = ('red', 'green', 'blue', 'yellow', 'orange')
# favorite_color(favs)

# the arguments we pass into the function as a tuple, when execute create
# the tuple inside the function. this is why we cant pass a tuple directly.


# using **kwags will allow a dictionary of argument
def vehicles(**truck):
    print('My truck is a ' + truck['model'])


# vehicles(make='chevy', model='silverado')


# using the default argument allows you to have more than one with one
# given a default value. these defaults can after arguments
def my_hello(arg, arg2='hi'):
    print(arg2 + ' ' + arg)


# my_hello('Tom')
# my_hello('Tim', 'Hello')


# Using a return keyword will return the value back out the function to
# a variable you define to the left of the function
def simple_add(value1, value2):
    return value1 + value2


# total = simple_add(12, 23)
# print(total)
# print(simple_add(5, 10))


# main function is what is called a python file is ran through
# compiler. It will perform all actions in the file accept function unless
# they are called directly.


if __name__ == '__main__':
    total = simple_add(12, 23)
    print(total)
    
















