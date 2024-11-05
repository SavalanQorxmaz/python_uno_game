from take_put import f_take_from_new

class Gamer:
    def __init__(self, *, nick: str):
        self._nick = nick.capitalize()
        
        self._cards = set()
        for _ in range(7):
            new_card = f_take_from_new()
            self.cards.add(new_card)

    @property
    def nick(self):
        return self._nick
    @nick.setter
    def nick(self, value):
        self._nick = value

    @property
    def cards(self):
        return self._cards
    @cards.setter
    def cards(self, card=None):
        if card is not None:
            self._cards.add(card)

    @cards.deleter
    def cards(self, card):
       self._cards.discard(card)

    def __str__(self):
        return self._nick
    def __repr__(self):
        return self._nick


