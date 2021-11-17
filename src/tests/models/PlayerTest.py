import sys
  
# adding Folder_2/subfolder to the system path
sys.path.insert(0, '/mnt/snake-ladder/src/game/')

from models.Player import Player
from models.Game import Game
from ..mocks.MockDice import MockDice
import unittest

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()
    
    def test_getPosition(self):
        p = Player("Alice")
        self.game.setDice(MockDice())
        self.game.play(p)
        self.assertEqual(p.getPosition(), 5)
    
    def test_setPosition(self):
        p = Player("Bob")
        p.setPosition(6)
        self.assertEqual(p.getPosition(), 6)
    
    def test_setPositionToCheckPlayerWon(self):
        p = Player("Ravi")
        p.setPosition(95)
        self.game.setDice(MockDice())
        self.game.play(p)
        self.assertEqual(p.won, True)
    