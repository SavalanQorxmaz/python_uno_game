from gamer import Gamer
from gamer import allowed_cards

# Oyuncu sayinin mueyyen edilmesi

if __name__ == '__main__':
    gamers_count = int(input('Oyuncu sayini daxil et: '))
    gamers = []
    print(len(allowed_cards))
    for i in range(gamers_count):
        gamers.append(Gamer(nick=input(f'{i+1}-ci Oyuncunun nikini daxil et: ')))
    [print(f'{gamer.nick}: {gamer.cards}') for gamer in gamers]
    print(len(allowed_cards))
