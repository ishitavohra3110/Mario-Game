from person import *
from board import *


class Coin(Person):
    def generatecoin(self):
        Board.board[self.x][self.y] = self.char
