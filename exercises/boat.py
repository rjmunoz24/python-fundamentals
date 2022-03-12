# in your boar.py file, write your boat object using your notes from the intro
# to programming class.
# Refine your attributes for your constructor. Utilize the property() along with the getter
# and setter for each of your variable attributes. Be sure to test your class and properties

class MyClass:
    # protected class variable
    _my = 'Boat'

    # constructor
    def __init__(self):
        # protected instance variable
        self._ = 'yacht'
        self.__you = 'ship'





class Feet:
    # constructor
    def __init__(self, length2):
        self._length = length2

    def to_inches(self):
        return self.get_length() * 10

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
    self = property(get_length, set_length, del_length)


measure = Feet(2)
print(measure._length)
print(measure.to_inches())
measure.length = 4
print(measure.to_inches())


# begin with the main function

if __name__ == '__main__':
    obj2 = MyClass()
    print(obj2._my)
    pass


