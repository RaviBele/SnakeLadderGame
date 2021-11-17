class Player:
    def __init__(self, Name):
        self.name = Name
        self.won = False
        self.position = 0
        self.rank = 0
    
    def getName(self):
        return self.name
        
    def setPosition(self, position):
        self.position = position
    
    def getPosition(self):
        return self.position
    
    def setWon(self, rank):
        self.won = True
        self.rank = rank
    
    def getRank(self):
        return self.rank