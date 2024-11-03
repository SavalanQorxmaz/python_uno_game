

class Card:
    def __init__(self, *, color=''):
        self._color = color

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        self._color = value

    @color.deleter
    def color(self):
        del self._color


    def __str__(self):
        return self._color

    # def __repr__(self):
    #     pass

color = Card()
print(color)
color.color = 'Black'
# del color.color
print(color)