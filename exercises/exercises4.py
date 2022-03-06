# page 29 of your book
# try it yourself section do the following tasks.
# addition
# subtraction
# multiplication
# division
print(4+4)
print(10-2)
print(2*4)
print(16/2)

# page 29 2-9
fav_number = 12
message = "Do you know what my favourite number is {12}?"
print(message)

# assign variables to following sets of numbers.
# use underscores to make them more readable.
# write a function called number_sets print each variable inside the function
# call all the function to verify your results
def number_set():
    able = "456234"
    print(able)
    able = "68423791"
    print(able)
    able = "13794628"
    print(able)
    able = "96374"
    print(able)


number_set()


# Write a function that will take 2 arguments.
# using type conversion, convert the first argument from int to float.
# convert the second argument from float to int.
# call the function and provide the correct values
# for each argument to verify your results.
# one argument should be a float and the other an int.
def number_set2(arg1, arg2):
    value1 = float(34)
    print(value1)
    value2 = int(34.5)
    print(value2)


number_set2('34', 34.5)

# write a function that will have two inputs.
# the first input method should ask "What is your favorite movie"
# the second input method should ask "How many times have you seen it".
# The second input should be inside an int function.
# Each input method should be assigned to a variable.
# In a print statement using placeholders, the output result should be
# "I have seen{favorite movie}{number of times}times".
def function_name(data_1, data_2):
    movie = input("what is your favorite movie")
    time = input("How many times have you seen it")

    message = 'I have seen {0} {1}times'
    print(message.format(movie, time))


function_name('movie', 'time')




























