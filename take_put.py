
from all_cards import all_cards
new_cards = all_cards[:]
old_cards = []

# Kart goturme funksiyasi
def f_take_from_new():
    if len(new_cards) == 0:
        return None
    else:
        card = new_cards.pop()
        return card
    
# Kart qoyma funksiyasi
def f_put_to_old(card):
    old_cards.append(card)
    