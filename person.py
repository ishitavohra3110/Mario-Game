from board import *
import time


class Person(Board):
    def __init__(self, alp, i, j):
        # print(i,j,alp)
        self.x = i
        self.y = j
        self.char = alp

    def execute_a(self):
        Board.board[self.x][self.y] = ' '
        Board.board[self.x + 1][self.y] = ' '
        Board.board[self.x + 1][self.y - 1] = self.char
        Board.board[self.x][self.y - 1] = self.char
        self.y = self.y - 1

    def execute_d(self):
        Board.board[self.x][self.y + 1] = self.char
        Board.board[self.x + 1][self.y + 1] = self.char
        Board.board[self.x][self.y] = ' '
        Board.board[self.x + 1][self.y] = ' '
        self.y = self.y + 1
