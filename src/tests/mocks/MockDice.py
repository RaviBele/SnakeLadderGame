import sys
  
# adding Folder_2/subfolder to the system path
sys.path.insert(0, '/mnt/snake-ladder/src/game/')

from models.Dice import Dice

class MockDice(Dice):
    def roll(self):
        return 5
