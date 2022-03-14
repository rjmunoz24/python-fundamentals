# 11-3
# employee:
# write a class called employee.
# the __int__() method should take in a first name, a last name, and an annual salary.
# and store each of these annual salary by default but also accepts a different raise amount.
# Write a test a case for employee.
# write two test methods, test_give_default _raise() and test_give_raise().
# use the setup() method so you dont have to create a new emplyoee instance in each test method.
# run your test case, and make sure both tests pass
class Employee():
    """A class to represent an employee."""

    def __init__(self, f_name, l_name, salary):
        """Initialize the employee."""
        self.first = f_name.title()
        self.last = l_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Give the employee a raise"""
        self.salary += amount
