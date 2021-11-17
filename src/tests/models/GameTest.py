import sys
  
# adding Folder_2/subfolder to the system path
sys.path.insert(0, '/mnt/snake-ladder/src/game/')

from exceptions.InvalidPlayerException import InvalidPlayerException
from exceptions.GameOverException import GameOverException
from models.Board import Board
from models.Game import Game
from models.Player import Player
from ..mocks.MockDice import MockDice


import unittest

class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game(numberOfSnakes=0, boardSize=20, dice=MockDice())
        self.game.addPlayer("Alice")
        self.game.addPlayer("Bob")

    def test_play(self):
        p = Player("Alice")
        self.game.play(p)
        self.assertEqual(p.getPosition(), 5)
    
    def test_play_game_till_end(self):
        currentPlayer = self.game.getNextPlayer()
        self.game.play(currentPlayer)
        self.assertEqual(5, currentPlayer.getPosition())
        currentPlayer = self.game.getNextPlayer()
        self.game.play(currentPlayer)
        self.assertEqual(5, currentPlayer.getPosition())
        currentPlayer = self.game.getNextPlayer()
        self.game.play(currentPlayer)
        self.assertEqual(10, currentPlayer.getPosition())
        currentPlayer = self.game.getNextPlayer()
        self.game.play(currentPlayer)
        self.assertEqual(10, currentPlayer.getPosition())
        currentPlayer = self.game.getNextPlayer()
        self.game.play(currentPlayer)
        self.assertEqual(15, currentPlayer.getPosition())
        currentPlayer = self.game.getNextPlayer()
        self.game.play(currentPlayer)
        self.assertEqual(15, currentPlayer.getPosition())
        currentPlayer = self.game.getNextPlayer()
        self.game.play(currentPlayer)
        self.assertEqual(20, currentPlayer.getPosition())
        currentPlayer = self.game.getNextPlayer()
        self.game.play(currentPlayer)
        self.assertEqual(20, currentPlayer.getPosition())

        self.assertRaises(GameOverException, self.game.getNextPlayer)
    
    def test_GameOver(self):
        player = self.game.getNextPlayer()
        player.setPosition(15)
        self.game.play(player)
        player = self.game.getNextPlayer()
        player.setPosition(15)
        self.game.play(player)
        self.assertRaises(GameOverException, self.game.getNextPlayer)
    
    def test_InvalidPlayer(self):
        player = Player("Bob")
        player.setPosition(20)
        self.assertRaises(InvalidPlayerException, self.game.play, player)
