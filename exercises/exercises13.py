# 8-15
# printing models
# put the functions for the example printing_models.py in a separate file called printing_functions
# write an import statement at the top of printing_models.py, and modify the file to use
# the imported functions
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until there are none left.
        Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

import printing_models

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_models.print_models(unprinted_designs, completed_models)
printing_models.show_completed_models(completed_models)

# 9-10
# imported Restaurant: Using your latest Restaurant class, store it in a module.
# make a separate file that imports Restaurant . make a restaurant instance.
# and call on of restaurants methods to show that the import statement is working.
# properly

import restaurant

duck_eat_dog = restaurant.Restaurant("duck eat dog", "Random")
duck_eat_dog.open_restaurant()
duck_eat_dog.describe_restaurant()

# 9-11
# imported admin
# start with your work from exercise 9-8
# store the class's user, privileges and admin in one module. create a separate
# file make an admin instance and call show_privileges() to show that
# everything is working correctly
import admin

new_admin = admin.admin("Super", "NovaGuy", 35)
new_admin.greet_user()
new_admin.describe_user()
new_admin.show_privileges()

# 9-12
# multiple modules store the user class in one module, and store the
# privileges and admin classes in a separate module.
# in a separate file, create
# an admin instance and call show_privileges() to show that everything is still
# working correctly

import user, admin_and_privileges

super_new_strict_admin = admin_and_privileges("bully", "the bad boy" 35)
super_new_strict_admin.privileges.show_privileges()

# 9-16
# one excellent resource for exploring the python standard library is a site called
# python module of the week.
# find a module that looks interesting to you and read about it
# perhaps starting with the random module

# I read about the time-clock time
# how the time module provides access to several types of clocks
# Each are useful for different purposes.
# clock can be used to measure elapsed time in a long-running process
# because it is guaranteed never to move backwards.
# how the cpu time is available through clock()
# and process_time() returns the combined processor time and system time



