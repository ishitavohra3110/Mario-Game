from colorama import *


class Board():
    wall = ""
    obstacle = ""
    normal = ""
    board = [[] for i in range(0, 8000)]
    for j in range(0, 8000):
        wall += 'X'
    for j in range(0, 8000):
        if j == 0 or j == 63:
            normal += 'X'
        else:
            normal += ' '
    for j in range(0, 8000):
        if j % 20 == 13 or j % 20 == 14:
            obstacle += '#'
        else:
            obstacle += ' '

    def generate(self):
        for i in range(0, 20):
            for j in range(0, 8000):
                if i == 0 or i == 19:
                    self.board[i].append(self.wall[j])
                else:
                    if self.normal[j] == 'X':
                        self.board[i].append(self.normal[j])
                    elif i == 18 or i == 17:
                        self.board[i].append(self.obstacle[j])
                    else:
                        self.board[i].append(' ')
        for j in range(0, 8000):
            if j % 20 == 5 or j % 20 == 6 or j % 20 == 7 or j % 20 == 8 or j % 20 == 9 or j % 20 == 10 or j % 20 == 4:
                self.board[11][j] = '*'
                self.board[12][j] = '*'

    def print_board(self):
        temp = ['' for i in range(0, 64)]
        for i in range(0, 20):
            for j in range(0, 64):
                temp[i] = temp[i] + self.board[i][j]
        for i in range(0, 20):
            if i < 11:
                print(Back.BLUE + temp[i])
            else:
                print(Back.GREEN + temp[i])
