import random
from models.Snake import Snake
from models.Ladder import Ladder

class Board:
    def __init__(self, size=100):
        self.start = 1
        self.end = size
        self.snakes = []
        self.ladders = []
    
    def getEnd(self):
        return self.end

    def addSnake(self, snake):
        self.snakes.append(snake)
    
    def addLadder(self, ladder):
        self.ladders.append(ladder)
    
    def createBoard(self, noOfSnakes=0, noOfLadders=0):
        positionOfSnakeAndLadders = set()

        # Adding snakes
        for i in range(noOfSnakes):
            while True:
                snakeTail = random.randint(self.start+2, self.end-3)
                snakeHead = random.randint(snakeTail+2, self.end-1)
                headTailPair = (snakeHead, snakeTail)
                if headTailPair not in positionOfSnakeAndLadders:
                    snake = Snake(snakeHead, snakeTail)
                    self.addSnake(snake)
                    positionOfSnakeAndLadders.add(headTailPair)
                    break

        # Adding ladders
        for i in range(noOfLadders):
            while True:
                ladderStart = random.randint(self.start+2, self.end-3)
                ladderEnd = random.randint(ladderStart+2, self.end-1)
                startEndPair = (ladderStart, ladderEnd)
                if startEndPair not in positionOfSnakeAndLadders:
                    ladder = Ladder(ladderStart, ladderEnd)
                    self.addLadder(ladder)
                    positionOfSnakeAndLadders.add(startEndPair)
                    break
                

    def getNextPosition(self, currentPostion, diceValue):
        nextPosition = currentPostion + diceValue
        if nextPosition > self.end:
            return currentPostion
        
        for snake in self.snakes:
            if nextPosition == snake.getHead():
                print("snake head", snake.getHead(), "snake tail", snake.getTail())
                print("Snake bites me. Going down.")
                return snake.getTail()
        
        for ladder in self.ladders:
            if nextPosition == ladder.getStart():
                print("ladder start", ladder.getStart(), "ladder end", ladder.getEnd())
                print("Yey, Got ladder, going up.")
                return ladder.getEnd()
        
        return nextPosition
        