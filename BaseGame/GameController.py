from BaseGame.Board import Board
from BaseGame.Score import Score
from BaseGame.SaveScore import SaveScore

from abc import abstractmethod, ABC

class GameController(ABC):
    def __init__(self):
        self.board = None
        self.score = Score() ## for tracking score

    # set board variable
    def setBoard(self, board:Board):
        self.board = board

    # CORE CLICK FUNCTIONALITY, ALL THIS STUFF HAPPENS ONCE A TILE IS CLICKED
    def processPlayerMove(self, tile):
        self.processPlayerClick(tile, self.board)
        self.pointSystem(self.score, self.board)
        self.gameOverCondition()

    # publishes score to text file
    def save_score(self, score, gameName):
        dialog = SaveScore(score, gameName)
        dialog.exec_()

    # Modifies the board in some way once a tile is clicked
    @abstractmethod
    def processPlayerClick(self, tile, board):
        pass
    
    # Calculates the score based on the board state
    @abstractmethod 
    def pointSystem(self, score, board):
        pass 
    
    # Determines whether or not to end or continue the game
    @abstractmethod 
    def gameOverCondition(self):
        pass