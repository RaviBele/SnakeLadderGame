import sys
  
# adding Folder_2/subfolder to the system path
sys.path.insert(0, '/mnt/snake-ladder/src/game/')

from models.Dice import CrookDice
import unittest

class CrookedTest(unittest.TestCase):
    def test_CrookedDice(self):
        self.assertEqual(CrookDice(1, 6).roll()%2, 0)