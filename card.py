from colors import colors

    
class Card:
    def __init__(self, *, color: str, symbol: int):
        self._color = color.upper()
        self._symbol = symbol

    @property
    def color(self):
        return colors[self._color]

    @property
    def symbol(self):
        return self._symbol
    
    def __str__(self):
        return f'{colors[self._color]}{self._symbol}{colors['RESET']}'
    
    def __repr__(self):
        return f'{colors[self._color]}{self._symbol}{colors['RESET']}'
    