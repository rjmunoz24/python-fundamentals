# lesson10 Encapsulation in python is considered weak as it is done by convention
# rather than enforced.

# protected members use a single underscore and should not be accessed
# outside the class or subclass.

class MyClass:
    # protected class variable
    _hi = 'hello'

    # constructor
    def __init__(self):
        # protected instance variable
        self._ = 'world'
        # private variable
        self.__you = 'You'


# properties can allow enforcing encapsulation and access protected
# and private members
class Feet:
    # constructor
    def __init__(self, length2):
        self.length = length2

    def to_inches(self):
        return self.get_length() * 12

    # getter
    def get_length(self):
        return self._length

    # setter
    def set_length(self, value):
        self._length = value

    # deleter
    def del_length(self):
        del self._length

    # creating the property
    length = property(get_length, set_length, del_length)


measure = Feet(4)
print(measure.length)
print(measure.to_inches())
measure.length = 6
print(measure.to_inches())


# The property decorator annotation allows the creation of the methods to replace
# the need for the property method
class Centimeter:
    def __init__(self, size):
        self._size = size

    def to_millimeters(self):
        return self._size * 10

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value


my_cent = Centimeter(3)
print(my_cent.size)
my_cent.size = 5
print(my_cent.to_millimeters())


# begin with the main function
if __name__ == '__main__':
    obj2 = MyClass()
    print(obj2._hi)
    # trying to access a private variable will result in error
    # print(obj2.__you)

    # create a new object
    # measure = Feet(3)

    # get the length attribute
    # print(measure.length)

    # get the to_inches method result
    # print(measure.to_inches())

    # assign a new value to length
    # measure.length = 5
    pass

    # get the to_inches method result again
    print(measure.to_inches())
