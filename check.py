from board import *


class deter():
    def checkboard(self, x, y):
        if x > 19 or y > 7999 or x < 0 or y < 0:
            return 'free'

        if Board.board[x][y] == 'M' or Board.board[x][y] == 'm':
            return 'mario'
        elif Board.board[x][y] == '*':
            return 'pf'
        elif Board.board[x][y] == 'e' or Board.board[x][y] == 'E':
            return 'enemy'
        elif Board.board[x][y] == '(':
            return 'small'
        elif Board.board[x][y] == ')':
            return 'big'
        elif Board.board[x][y] == '$':
            return 'coin'
        elif Board.board[x][y] == 'X':
            return 'wall'
        elif Board.board[x][y] == 'G':
            return 'gem'
        else:
            return 'free'
