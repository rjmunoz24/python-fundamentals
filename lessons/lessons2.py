# My Application Overview Lesson

# this function should be lowercase and if more than one word it
# should have an underscore to separate each word. You should have
# a parenthesis after the name followed by a colon. Statements that are
# part of the function should be more 4 spaces indented.
def my_function():
    print('hello')
    print('world')


# to run the function must call it by name.
my_function()


# when defining a function with arguments, those arguments go in between
# the parenthesis and separate by commas.
def my_other(arg1, arg2):
    print(arg1)
    print(arg2)


my_other('red', 'green')

# Variable Names
# - must start with a letter or an underscore
# - can not begin with a number
# - can only contain alphanumeric characters and underscores
# - are case-sensitive.

# - variables are on the left  while the literal value is on right
# - value & value2 are variables
# - blue and 10 are literals
# - combined they are filed
value = 'Blue'
value2 = 10
print(value)
print(value2)

# - Variables can even change types, although you may want to avoid this
value3 = 'Happy'
print(value3)
value3 = 20
print(value3)


# multi name statements use a backslash to continue a statement on a second line.
alpha = 1 + 2 + 3 \
    + 4 + 5
print(alpha)

# - more than one variable on the same line
beta = 10; charlie = "python"; delta = 5
up, down, left = "town", "stairs", "right"
print(up)
print(down)
print(left)



# a class is an object, which is a blueprint. an instantiation of an object.
# allows for all fields and functions to be access within.
# outside the class, you need to provide 2 empty spaces before its defined
# basic class example
class MyFirstClass:
    name = 'roberto'

    def something(self):
        print('something')

my_class = MyFirstClass()
    print(my_class.name)
    my_class.something()

































