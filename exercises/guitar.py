class Guitar:
    def __init__(self, music, guitar_type, tune_up):
        self.The_music = music
        self.what_guitar_type = guitar_type
        self.lets_tune_up = tune_up

    def when_it_plays(self):
        print(str.format('beautiful melodies {0} when played', self))

    @property
    def the_music(self):
        return self._the_music

    @the_music.setter
    def the_music(self, num):
        self._the_music = num

    @property
    def what_guitar(self):
        return self._what_guitar

    @what_guitar.setter
    def what_guitar(self, guitar):
        self._what_guitar = guitar

    @property
    def lets_tune_up(self):
        return self._lets_tune_up

    @lets_tune_up.setter
    def roof_style(self, style):
        self.lets_tune_up = style


my_guitar = Guitar('color', 'weight', 'vibrates')
print(my_guitar.it_goes)
print(my_guitar.it_goes_not())
