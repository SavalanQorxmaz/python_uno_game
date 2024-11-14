import unittest
from card import Card
from gamer import Gamer


class UnoTest(unittest.TestCase):
    card = Card(color='green',symbol='3')
    card2 = Card(color='yellow',symbol='3')
    gamer = Gamer(nick='NewGamer')
    def test_card(self): 
        self.assertEqual(self.card.__str__(), '\x1b[1;37;42m 3 \x1b[1;39;49m')

    def test_card_color(self): 
        self.assertEqual(self.card2.color, '\x1b[1;30;43m ')
        print(' \x1b[1;39;49m')

    def get_gamer_nick(self):
        self.assertEqual(self.gamer.nick, 'NewGamer')

    def empty_card(self):
        self.assertIsNone(self.gamer.cards)

    def add_card(self):
        self.gamer.cards.add(self.card)
        self.assertIsNotNone(self.gamer.cards)

if __name__ == '__main__':
    unittest.main(verbosity=2)