# 10-6
# One common problem when prompting for numerical input occurs when people provide text
# instead of numbers.
# When you try to convert the input to an int, you'll get a ValueError.
# write a program that prompts for two numbers.
# Add them together and print the result. Catch the valueerror if either input value is not a number
# and print a friendly error message.
# Test your program by entering two numbers and then by entering some text instead of a number
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

try:
    result = int(num1) + int(num2)
    print(f"The result is {result}")
except ValueError:
    print("wrong value provided. Enter two numbers.")
# pretty much got the results I wanted when it came to the numbers
# but I soon as I insert a letter it gave me
# wrong value provided. Enter two numbers.

# 10-7
# Addition Calculator
# wrap your code from exercises 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake
# abd enter text instead of a number
print("Enter two numbers to add them.")
print("Enter 'q' to stop execution.")

while True:
    num1 = input("Enter first number: ")
    if num1 == 'q':
        break
    num2 = input("Enter first number: ")
    if num2 == 'q':
        break

    try:
        result = int(num1) + int(num2)
        print(f"The result is: {result}")
    except ValueError:
        print("wrong value provided. Enter two numbers")
# again same thing as the exercise 10-6 as soon as you put in a letter you get
# wrong value provided. Enter two numbers
# but once you enter 2 numbers the program continues
# to stop the loop all i have to do is type in q and it stops

# 10-8
# cats and dogs
# Make two files, cats.txt and dogs.txt.
# store at least three names of cats in the first file and three names of dogs in the second file.
# Write a program that tries to read these files and print the contents of the file to the screen.
# Wrap your code in a try except block to catch the FileNotFound error, and print a friendly message
# if a file is missing.
# Move one of the files to a different location on your system, and make sure the code in the except block
# executes properly
filename1 = 'cats.txt'
filename2 = 'dogs.txt'

print("Cats: ")
try:
    with open(filename1, endcoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename1} does not exist.")
else:
    print(contents)

print("Dogs: ")
try:
    with open(filename2, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"sorry, the file {filename2} does not exist.")
else:
    print(contents)

# 10-9
# Silent Cats and Dogs
# Modify your except block in exercise 10-8 to fail
# silently if either file is missing
filename1 = 'cats.txt'
filename2 = 'dogs.txt'

print("Cats: ")
try:
    with open(filename1, endcoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    pass
else:
    print(contents)

print("Dogs: ")
try:
    with open(filename2, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
   pass
else:
    print(contents)


