import random
from card import Card
from all_cards import f_all_cards
allowed_cards = set(f_all_cards())
# [print(f'{x}') for x in allowed_cards]

class Gamer:
    def __init__(self, *, nick: str):
        self._nick = nick.capitalize()
        
        self._cards = set()
        for _ in range(7):
            self.cards.add(allowed_cards.pop())

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
       
    def attack(self, *, last_card:Card):
        color = last_card.color
        number = last_card.number
        def f_check_if_allow(x:Card):
            if x.color == color or x.number == number:
                return True
            return False
        allowed_cards = set(filter(f_check_if_allow, self.cards ))
        selected_card = random.choice(allowed_cards)
        self.cards.discard(selected_card)

    def __str__(self):
        return self._nick
    def __repr__(self):
        return self._nick


# first = Gamer(nick='first')
# print(first)

# for i in range(10):
#     first.cards = i

# print(first.cards)

# first.cards.discard(3)
# print(first.cards)


