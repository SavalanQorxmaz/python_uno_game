import random
from gamer import Gamer
from card import Card
from take_put import f_take_from_new, f_put_to_old, old_cards

def f_attack(*, gamer:Gamer):
    last = old_cards[-1]
    last_color = last.color
    last_symbol = last.symbol
    cards = list(gamer.cards)
    print(f'Oyuncu: {gamer} Elindeki kartlar:{cards}')
    def f_check_if_allow(x:Card):
            if x.color == last_color or x.symbol == last_symbol:
                return True
            return False
    allowed_cards = [*filter(f_check_if_allow, cards)]
    if len(allowed_cards) == 0:
        new_card = f_take_from_new()
        if new_card:
            cards.append(new_card)
            allowed_cards = [*filter(f_check_if_allow, cards)]
            print(f'Bazardan goturduyu kart: {new_card}')
            gamer.cards.add(new_card)
    if len(allowed_cards) == 0:
        print(f'{gamer} bazardan {new_card} goturdu, oynaya bilmedi ve onnan kecdi')
        return 'next'
    else:
        print(f'Oynanila bilecek kartlar: {allowed_cards}')
        selected = random.choice(allowed_cards)
        print(f'Oynanilan kart{selected}')
        gamer.cards.discard(selected)
        f_put_to_old(selected)
        if len(gamer.cards) == 0:
            return 'win'
        return 'next'
    