import itertools
import random
from card import Card


# Kartlarin hazirlanmasi
all_cards = [
                [
                    [Card(color=color, symbol=x)] 
                    if x == '0' 
                    else [Card(color=color, symbol=x), Card(color=color, symbol=x)]
                    for x in [*map(str,[*range(10)]), 'pass', 'reverse', '+2']
                ]
                    for color in ('red', 'green', 'yellow', 'blue')
                ] 

        
            
all_cards = [[*itertools.chain.from_iterable(x)] for x in all_cards]
all_cards.extend([[Card(color='uni', symbol='unicolor+4'), Card(color='uni', symbol='unicolor')]
                    for _ in range(4)
                    ] ) 
all_cards = [*itertools.chain.from_iterable(all_cards)]
# print(all_cards)
# [print(card.symbol, card.color) for card in all_cards]
random.shuffle(all_cards)