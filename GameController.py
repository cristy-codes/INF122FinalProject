from Board import Board
from GameConditions import GameConditions
from Tile import Tile
from TurnEvent import TurnEvent

class GameController:
    def __init__(self, conditions:GameConditions, turn:TurnEvent):
        self.board = None
        self.conditions = conditions
        self.gameTurn = turn

    def setBoard(self, board:Board):
        self.board = board

    ### called when the tile is clicked; houses all clicked functionality
    def handler(self, tile:Tile):
        self.conditions.clickEvent(tile, self.board)
        self.conditions.pointSystem(self.board)
        self.gameLoop()

    ### mechanism to determine whether to end game or proceed to next turn
    def gameLoop(self):
        ### stop game if the game is over
        if (self.conditions.determineGameOver(self.board)):
            print("GAME OVER")
            self.stop()
            ### iterate through another turn
        else:
            self.gameTurn.processTurn(self.board)
    
    ### start the game
    def start(self):
        self.gameTurn.processTurn(self.board)
    
    ### stop the game
    def stop(self):
        for tileList in self.board.table:
            for tile in tileList:
                tile.disable()