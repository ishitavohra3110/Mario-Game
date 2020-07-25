import os
import time
from person import *
from board import *
from check import *
enemies = []


class Enemy(Person):
    def generate(self):
        Board.board[self.x][self.y] = self.char
