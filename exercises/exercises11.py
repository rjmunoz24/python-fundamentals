
# 9-1
import self as self

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")


Restaurant = Restaurant("roberto's", "fast food")
print(f"{Restaurant.cuisine_type}")
print(f"{Restaurant.restaurant_name}")

# 9-6
# an ice cream stand is a specific kind of restaurant.
# write a class called IceCreamStand that inherits from the restaurant class you wrote n exercise 9-1.
# Either version of the class will work; just pick the one you like better.
# add an attribute called flavors that store's a list of ice cream flavors.
# write a method that displays these flavors.
# create an instance of IceCreamStand, and call this method.
class IceCreamStand:
    def __init__(self, name, cuisine_type='ice_cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"-{flavor.title()}")


big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']
big_one.describe_restaurant()
big_one.show_flavors()


# 9-7
# administrator is a special kind of user.
# Write a class called admin that inherits from the user class you wrote in exercise 9-3.
# add an attribute privileges that stores a list of strings "can" add "post", "can delete post", can ban user
# write a method called show_privilage() that lists the admin set of privileges.
# create an instance of Admin and call your method

# 9-3
class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self. last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"{self.first_name}, {self.last_name}, age: {self.age}")
        print()

    def greet_user(self):
        print(f"Hi, {self.first_name}")
        print()


new_user1 = User("Jack", "Jones", 28)
new_user1.describe_user()
new_user1.greet_user()

new_user2 = User("Aqua", "Man", 20)
new_user2.describe_user()
new_user2.greet_user()

new_user3 = User("The", "Batman", 25)
new_user3.describe_user()
new_user3.greet_user()


class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"-{privilege}")


eric = Admin('eric', 'munoz', 'e_munoz', 'e_munoz@example.com', 'kansas')
eric.describe_user()

eric.privileges = [
    'can reset password'
    'can moderate discussions',
    'can suspend accounts'
]

eric.show_privileges()


# write a separate privileges class. The class should have one attribute, privileges, that stores a list
# of strings as described in exercise 9-7.
# move the show_privileges() method to this class. Make a privileges instance as an attribute in the admin class.
# create a new instance of admin and use your method to show its privileges.

class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges")
        if self.privileges:
            for privilege in self.privileges:
                print(f"-{privilege}")
        else:
            print("- This user has no privileges")


eric = Admin('eric', 'munoz', 'e_munoz', 'e_munoz@example.com', 'kansas')
eric.describe_user()

eric.privileges.show_privileges()
print("\nAdding privileges...")
eric_privileges = [
    'can reset password'
    'can moderate discussions',
    'can suspend accounts'
    ]
eric.privileges.privileges = eric_privileges
eric.show_privileges()


