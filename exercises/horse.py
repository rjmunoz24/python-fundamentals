class Horse:
    def __init__(self, moves, eats, fearful):
        self.He_moves = moves
        self.it_eats = eats
        self.not_fearful = fearful

    def it_gets_angry(self):
        print(str.format('The {0} gets angry', self))

    @property
    def he_moves(self):
        return self._he_moves

    @he_moves.setter
    def he_moves(self, num):
        self._he_moves = num

    @property
    def it_eats(self):
        return self._it_eats

    @it_eats.setter
    def it_eats(self, eats):
        self._it_eats = eats

    @property
    def not_fearful(self):
        return self._it_moves

    @not_fearful.setter
    def roof_style(self, style):
        self._not_fearful = style


my_horse = Horse('food', 'run', 'brown')
print(my_horse.it_goes)
print(my_horse.it_goes_not())
