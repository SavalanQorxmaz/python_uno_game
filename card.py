colors = dict(
    BLACK   = '\x1b[1;39;40m ',
    RED     = '\x1b[1;39;41m ',
    GREEN   = '\x1b[1;37;42m ',
    YELLOW  = '\x1b[1;30;43m ',
    BLUE    = '\x1b[1;37;46m ',
    WHITE   = '\x1b[1;30;47m ',
    UNI     = '\x1b[1;30;47m ',
    RESET   = ' \x1b[1;39;49m',
)

    

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
    