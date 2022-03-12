# House examples from OOP
class House:
    def __init__(self, window, foundation, roof_style, door_color):
        self.window_size = window
        self._foundation_type = foundation
        self._roof_style = roof_style
        self._door_color = door_color

    def door_open_close(self):
        print(str.format('The {0} door is open', self._door_color))

    @property
    def window_size(self):
        return self._window_size

    @window_size.setter
    def window_size(self, num):
        self._window_size = num

    @property
    def foundation_type(self):
        return self._foundation_type

    @foundation_type.setter
    def foundation_type(self, type):
        self._foundation_type = type

    @property
    def roof_style(self):
        return self._roof_style

    @roof_style.setter
    def roof_style(self, style):
        self._roof_style = style

    @property
    def door_color(self):
        return self._door_color

    @door_color.setter
    def door_color(self, color):
        self._door_color = color


my_house = House(23, 'concrete', 'shingle', 'red')
print(my_house.door_color)
print(my_house.door_open_close())



