from gamer import Gamer
from attack import f_attack
import random
import time
from take_put import f_put_to_old, f_take_from_new,old_cards


if __name__ == '__main__':
    # Oyuncu sayinin mueyyen edilmesi
    gamers_count = int(input('Oyuncu sayini daxil et: '))
    gamers = []
    
    # Oyuncularin niklerinin teyin edilmesi
    for i in range(gamers_count):
        gamers.append(Gamer(nick=input(f'{i+1}-ci Oyuncunun nikini daxil et: ')))
    # [print(f'{gamer.nick}: {gamer.cards}') for gamer in gamers]

    
    finish = False
    last_card = None
    current_gamer = None
    current_index = None
    already_done = True
    while not finish:
        [print(f'{gamer.nick}: {gamer.cards}') for gamer in gamers]
        if not old_cards:
            temp = f_take_from_new()
            f_put_to_old(temp)
        if not current_gamer:
            current_gamer = random.choice(gamers)
            current_index = gamers.index(current_gamer)
        last_card = old_cards[-1]
        print(f'Yere son acilan kart: {last_card}')
        attack_result = f_attack(gamer=current_gamer, already_done=already_done)
        if attack_result == 'win':   
            print(f'Winner: {current_gamer}')
            finish = True
        elif attack_result == 'next':
            current_index = (current_index + 1) % len(gamers)
            current_gamer = gamers[current_index]
        elif attack_result == 'pass':
            current_index = (current_index + 2) % len(gamers)
            current_gamer = gamers[current_index]
        elif attack_result == 'reverse':
            gamers.reverse()
            current_index = (len(gamers) - current_index ) % len(gamers)
            current_gamer = gamers[current_index]
        elif attack_result == 'unicolor':
            current_index = (current_index + 1) % len(gamers)
            current_gamer = gamers[current_index]
        elif attack_result == '+2':
            current_index = (current_index + 1) % len(gamers)
            current_gamer = gamers[current_index]
            already_done = False
        elif attack_result == 'unicolor+4':
            current_index = (current_index + 1) % len(gamers)
            current_gamer = gamers[current_index]
            already_done = False
        elif attack_result == 'already_done':
            current_index = (current_index + 1) % len(gamers)
            current_gamer = gamers[current_index]
            already_done = True
        
        time.sleep(2)
            
[print(f'{gamer.nick}: {gamer.cards}') for gamer in gamers]