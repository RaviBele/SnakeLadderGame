import random
from abc import abstractmethod

class Dice:
    @abstractmethod
    def roll(self):
        pass

class NormalDice(Dice):
    def __init__(self, minValue, maxValue):
        self.minValue = minValue
        self.maxValue = maxValue

    def roll(self):
        return random.randint(self.minValue, self.maxValue)

class CrookDice(Dice):
    def __init__(self, minValue, maxValue):
        self.minValue = minValue
        self.maxValue = maxValue

    def roll(self):
        return random.randrange(self.minValue+(self.minValue%2), self.maxValue+1, 2)
