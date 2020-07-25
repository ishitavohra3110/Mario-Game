from board import *
from manage import *
from check import *
from enemy import *
temp1 = [[] for i in range(0, 4096)]
x = Board()
mng = Manage()
find = deter()
jmp = 0


class key:
    def live_or_die(self):
        flag = 0
        for j in enemies:
            if Board.board[j.x][j.y] == j.char:
                if Board.board[j.x + 2][j.y] != '-':
                    j.char = 'E'

        for i in range(0, 20):
            for j in range(0, 64):
                cur = find.checkboard(i, j)
                cur1 = find.checkboard(i, j + 2)
                cur2 = find.checkboard(i + 1, j)
                cur3 = find.checkboard(i, j + 3)
                if cur == 'mario' and cur1 == 'small':
                    flag = 1
                    mng.manage_lived()
                    Board.board[i][j + 2] = ')'
                    Board.board[i + 1][j + 2] = ')'
                    Board.board[i][j] = 'm'
                    Board.board[i + 1][j - 1] = 'm'
                    Board.board[i][j - 1] = 'm'
                    Board.board[i + 1][j] = 'm'
                elif cur == 'mario' and cur1 == 'enemy':
                    flag = 1
                    mng.manage_lived()
                    break
                elif cur == 'mario' and cur1 == 'gem':
                    os.system('aplay -q sound/smb2_coin.wav&')
                    mng.incr()
                    Board.board[i][j + 2] = ' '
                    Board.board[i + 1][j + 2] = ' '
                    flag = 1
                    break

            if flag:
                break
        for i in range(0, 20):
            temp1[i].clear()

    def execute_a(self):
        for i in range(0, 20):
            for j in range(0, 8000):
                temp1[i].append(Board.board[i][j])
        for i in range(0, 20):
            Board.board[i].clear()
        for i in range(0, 20):
            Board.board[i].append('X')
            for j in range(1, 7999):
                if temp1[i][j] == 'e' or temp1[i][j +
                                                  1] == 'e' or temp1[i][j] == 'E' or temp1[i][j +
                                                                                              1] == 'E':
                    Board.board[i].append(temp1[i][j])
                elif j == 62:
                    Board.board[i].append(temp1[i][j + 2])
                elif i == 0 or i == 19 or j == 0 or j == 63 or temp1[i][j] == 'M' or temp1[i][j + 1] == 'M' or temp1[i][j] == 'm' or temp1[i][j + 1] == 'm':
                    Board.board[i].append(temp1[i][j])
                else:
                    Board.board[i].append(temp1[i][j + 1])
            Board.board[i].append(' ')
        self.live_or_die()

    def execute_d(self):
        for i in range(0, 20):
            for j in range(0, 8000):
                temp1[i].append(Board.board[i][j])
        for i in range(0, 20):
            Board.board[i].clear()
        for i in range(0, 20):
            Board.board[i].append('X')
            for j in range(1, 7999):
                if temp1[i][j] == 'e' or temp1[i][j -
                                                  1] == 'e' or temp1[i][j] == 'E' or temp1[i][j -
                                                                                              1] == 'E':
                    Board.board[i].append(temp1[i][j])
                elif temp1[i][1] == '$' and j == 1:
                    Board.board[i].append(' ')
                elif temp1[i][1] == '*' and j == 1:
                    Board.board[i].append(' ')
                elif i == 0 or i == 19 or j == 0 or j == 63 or j == 1 or temp1[i][j] == 'M' or temp1[i][j] == 'm' or temp1[i][j - 1] == 'M' or temp1[i][j - 1] == 'm':
                    Board.board[i].append(temp1[i][j])
                elif j == 64:
                    Board.board[i].append(temp1[i][j - 2])
                else:
                    Board.board[i].append(temp1[i][j - 1])
            Board.board[i].append(' ')
        self.live_or_die()
