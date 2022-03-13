# Lesson5 - Operators

# Arithmetic Operators
# These operators handle basic math

# Addition
def add_example():
    result = 10 + 5
    print(result)


# Subtraction
def subtract_example():
    result2 = 23 - 4
    print(result2)


# add_example()
# subtract_example()

# Multiplication & Division
# the example at the bottom is 2 parameters
def multi_divide(sum1, sum2):
    result_multi = sum1 * sum2
    result_divide = sum1 / sum2
    print(result_multi)
    print(result_divide)


multi_divide(10, 5)

# Modulus
# 1 argument example
# (value) is a place holder
def modulus_example(value):
    result_modulus = value % 24
    print(result_modulus)


# Exponentation
def exponent_example(value):
    result_exponent = value ** 3
    print(result_exponent)


# modulus_example(189)
# exponent_example(21)
able = 10
beta = 765


# Floor Division
def floor_example():
    result_floor = beta // able
    print(result_floor)


# floor_example()

# assignment operators
# these operators assign values to either a new variable or updates an
# existing variable.

def basic_assign(value1, value2):
    value1 += value2
    print(value1)
    value1 -= value2
    print(value1)
    value2 *= value1
    print(value2)
    value2 /= value1
    print(value2)


basic_assign(5, 3)


def basic_assign2(value):  # one argument
    value %= 32
    print(value)
    value **= 5  # exponent
    print(value)
    value //= 8  # floor division
    print(value)


basic_assign2(543)

# comparison operators
# these operators are use to compare two values with a result of either
# true or false


# equal & not equal
def compare_two(value1, value2):
    result_equal = value1 == value2  # false means equal
    result_not = value1 != value2  # true meaning the opposite
    print(result_equal)
    print(result_not)


compare_two(8, 5)

delta = 10  # external variables
echo = 34  # external variables

# Greater than and less than
def great_less():
    result1 = delta < echo  # true
    print(result1)
    result2 = delta > echo  # false
    print(result2)


great_less()

# greater than less than or equal to
def great_less_equal(num1):
    result_great = delta >= num1
    result_less = echo <= num1
    print(result_great)
    print(result_less)


great_less_equal(10)

# Logical operators
# operators that allow you to combine comparison operators

# and
def logical_and():
    result = echo > 25 and delta > 9
    print(result)


logical_and()

# or
def logical_or(num):  # parameter
    result = echo > num or num < delta
    print(result)


logical_or(30)

# not
def logical_not(num1, num2):
    result = not(num1 > num2)
    result2 = not(num1 < echo or num2 > delta)
    print(result)
    print(result2)


logical_not(23, 15)


# identity operators
# these operators check to see if the object is the same in memory
def identity_is_not(arg1, arg2, arg3):
    # is
    result1 = arg1 is arg2
    print(result1)
    result2 = arg1 is arg3
    print(result2)

    # is not
    result3 = arg2 is not arg3
    print(result3)


identity_is_not('Hello', 'Python', 'hello')

# membership operators
# these operators test to see if a sequence is in object
kilo = "some kind of words to search through"


# in & not in
def member_in(arg):
    result = arg in kilo
    print(result)
    result = arg not in kilo
    print(result)


member_in('To')























