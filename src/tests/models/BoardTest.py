import sys
  
# adding Folder_2/subfolder to the system path
sys.path.insert(0, '/mnt/snake-ladder/src/game/')
from models.Board import Board
from models.Snake import Snake
from models.Ladder import Ladder
import unittest

class BoardTest(unittest.TestCase):    
    
    def test_DefaultSizeBoard(self):
        board = Board()
        self.assertEqual(board.getEnd(), 100)
    
    def test_CustomizedSizeBoard(self):
        board = Board(80)
        self.assertEqual(board.getEnd(), 80)

    def test_CreatePlainBoard(self):
        board = Board()
        board.createBoard()
        self.assertEqual(len(board.snakes), 0)
        self.assertEqual(len(board.ladders), 0)
    
    def test_CreateBoardWithOnlySnakes(self):
        board = Board()
        board.createBoard(noOfSnakes=5)
        self.assertEqual(len(board.snakes), 5)
        self.assertEqual(len(board.ladders), 0)
    
    def test_CreateBoardWithOnlyLadders(self):
        board = Board()
        board.createBoard(noOfLadders=5)
        self.assertEqual(len(board.snakes), 0)
        self.assertEqual(len(board.ladders), 5)
    
    def test_CreateBoardWithSnakesAndLadders(self):
        board = Board()
        board.createBoard(noOfSnakes=5, noOfLadders=5)
        self.assertEqual(len(board.snakes), 5)
        self.assertEqual(len(board.ladders), 5)
    

    def test_getNextPosition(self):
        board = Board()
        board.createBoard()
        newPosition = board.getNextPosition(5, 4)
        self.assertEqual(newPosition, 9)
    
    def test_getNextPostionOnSnakeBite(self):
        board = Board()
        board.createBoard()
        board.addSnake(Snake(20, 12))
        newPosition = board.getNextPosition(17, 3)
        self.assertEqual(newPosition, 12)
    
    def test_getNextPostionOnGettingLadder(self):
        board = Board()
        board.createBoard()
        board.addLadder(Ladder(8, 12))
        newPosition = board.getNextPosition(5, 3)
        self.assertEqual(newPosition, 12)
