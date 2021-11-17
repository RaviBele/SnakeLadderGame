from models.Dice import NormalDice, CrookDice
from models.Board import Board
from models.Player import Player
from exceptions.InvalidPlayerException import InvalidPlayerException
from exceptions.GameOverException import GameOverException

class Game:
    def __init__(self, numberOfSnakes=1, numberOfLadders=0, boardSize=100, dice=NormalDice(1, 6)):
        self.board = Board(boardSize)
        self.players = []
        self.dice = dice
        self.rankCounter = 1
        self.board.createBoard(numberOfSnakes, numberOfLadders)
    
    def setDice(self, dice):
        self.dice = dice
    
    def addPlayer(self, playerName):
        self.players.append(Player(playerName))
    
    def getNextPlayer(self):
        if len(self.players) == 0:
            raise GameOverException()
        return self.players.pop(0)

    def checkReachedToEnd(self, player):
        return player.getPosition() == self.board.getEnd()

    def play(self, player):
        if not self.checkReachedToEnd(player):
            diceValue = self.dice.roll()
            currentPostion = player.getPosition()
            newPostion = self.board.getNextPosition(currentPostion, diceValue)
            print("Player: "+player.getName()+" moving from "+str(currentPostion)+" to "+str(newPostion)+" with dice value: "+ str(diceValue))
            player.setPosition(newPostion)
            self.updateGameStatus(player)
        else:
            raise InvalidPlayerException("Player: "+player.getName()+" has already won this game.")
        
    def updateGameStatus(self, player):
        if self.checkReachedToEnd(player):
            player.setWon(self.rankCounter)
            print("Player: "+player.getName()+" won with rank: "+str(player.getRank()))
            self.rankCounter += 1
        else:
            self.players.append(player)

    
    #Automated game
    def startGame(self):
        while True:
            player = self.players.pop(0)
            self.play(player)
            
            if len(self.players) == 0:
                print("Game over")
                break
    
            

