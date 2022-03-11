# on page 137 of your book do 8-3 through 8-5 of the try it yourself
from typing import List


def make_shirt(size, message):
    """summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')


make_shirt('large', 'I love Python!')
make_shirt(message="readability counts.", size='medium')

def make_shirt(size='large', message='I love python!'):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')


make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')


def describe_city(city, country='chile'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)


describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')


# On page 146 of your book, do 8-9 through 8-11 try it yourself.
# 8-9 & 8-11
def show_messages(message):
    """Print all messages in the list."""
    for message in messages:
        print(message)


messages = ["hello there", "how are u", ":)"]
show_messages(messages)


# 8-10
def show_messages(messages, sent_messages):
    """Print each message, and then move it to sent_messages."""
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


messages = ["hello there", "how are u?"]
# show_messages(messages)

# 8-11
def show_messages(message):
    """print all message in the list"""
    print("showing all messages:")
    for message in messages:
        print(message)

def send_messages(message):
    """Print each message, and then move it to sent_messages."""
    print("\nSending all messages")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


messages: list[str] = ["hello there", "how are u?", ":)"]

sent_messages = []
send_messages(messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)

# 9-1
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

# 9-2
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")


restaurant_1 = Restaurant("roberto's", "fast food")
Restaurant_2 = Restaurant("elijah", "fast food")
Restaurant_3 = Restaurant("ezekiel", "fast food")

# restaurant_1.open_Restaurant()
print(f"{restaurant_1.cuisine_type}")
print(f"{restaurant_1.restaurant_name}")
print()

Restaurant_2.open_Restaurant()
print(f"{Restaurant_2.cuisine_type}")
print(f"{Restaurant_2.restaurant_name}")
print()

Restaurant_3.open_Restaurant()
print(f"{Restaurant_3.cuisine_type}")
print(f"{Restaurant_3.restaurant_name}")
print()


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


# 9-4
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restauant_name} is open")

    def set_number_served(self, new_number_served):
        self.number_served = new_number_served


restaurant = Restaurant('Burger King', 'Fast Food')
restaurant.open_restaurant()
print(f"{restaurant.cruisine_type}")
print(f"{restaurant.restaurant_name}")
print()
print(f"number of clients served: {restaurant.set_number_served}")
restaurant.set_number_served(50)
print(f"number of clients served: {restaurant.set_number_served}")

# 9-5
class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self. last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name}, {self.last_name}, age: {self.age}")
        print()

    def greet_user(self):
        print(f"Hi, {self.first_name}")
        print()

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0


new_user3 = User("The", "Batman", 25)
new_user3.describe_user()
print(f"login attempts value: {new_user3.login_attempts}")
new_user3.reset_login_attempts()
print(f"login attempts value: {new_user3.login_attempts}")






































