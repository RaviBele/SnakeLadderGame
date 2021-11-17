from models.Game import Game

if __name__=='__main__':
    game = Game()
    numberOfPlayers = int(input("Enter number of players: "))
    for i in range(numberOfPlayers):
        playerName = input("Enter name of player no "+str(i+1)+":")
        game.addPlayer(playerName)

    game.startGame()
