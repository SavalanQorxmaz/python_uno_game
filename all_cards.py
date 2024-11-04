import itertools
import random
from card import Card
from gamer import Gamer


# Kartlarin hazirlanmasi
def f_all_cards():
    all_cards = [
                [[Card(color=color, number=i)] 
                if i == 0  
                else [Card(color=color, number=i),Card(color=color, number=i)]
                for i in range(10)]
                for color in('red', 'green', 'yellow', 'blue')
                ]
    all_cards = [[*itertools.chain.from_iterable(x)] for x in all_cards]
    all_cards = [*itertools.chain.from_iterable(all_cards)]
    random.shuffle(all_cards)
    return all_cards