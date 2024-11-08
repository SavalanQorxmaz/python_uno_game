import random
from gamer import Gamer
from card import Card
from take_put import f_take_from_new, f_put_to_old, old_cards

def f_functiona_cards(*, symbol):
    if symbol == '+2':
        return '+2'
    

def f_attack(*, gamer:Gamer, already_done=True):
    last = old_cards[-1]
    last_color = last.color
    last_symbol = last.symbol
    cards = list(gamer.cards)
    print(f'Oyuncu: {gamer} Elindeki kartlar:{cards}')
    if already_done:
        def f_check_if_allow(x:Card):
            if x.color == '\x1b[1;30;47m ' or last_color == '\x1b[1;30;47m ' or x.color == last_color or x.symbol == last_symbol:
                return True
            else:
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
            print(f'Oynanilan kart: {selected}')
            gamer.cards.discard(selected)
            f_put_to_old(selected)
            if len(gamer.cards) == 0:
                return 'win'
            elif selected.color == '\x1b[1;30;47m ' and selected.symbol =='unicolor+4':
                return 'unicolor+4'
            elif selected.color == '\x1b[1;30;47m ':
                return 'unicolor'
            elif selected.symbol == '+2':
                return '+2'
            elif selected.symbol == 'pass':
                return 'pass'
            elif selected.symbol == 'reverse':
                return 'reverse'
            return 'next'
    else:
        def take_cards(count):
            new_cards = []
            for _ in range(count):
                new_card = f_take_from_new()
                if new_card:
                    cards.append(new_card)
                    gamer.cards.add(new_card)
                    new_cards.append(new_card)
            print(f'Bazardan goturduyu kartlar: {new_cards}')    
        if last_symbol == '+2':
            take_cards(2)
        elif last_symbol == 'unicolor+4':
            take_cards(4)
        return 'already_done'