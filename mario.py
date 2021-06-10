import signal
import time
import os
from board import *
from person import *
from alarmexception import *
from press import _GetchUnix as getChar
from key import *
from manage import *
x = Board()
x1 = key()
temp1 = [[] for i in range(0, 8000)]
k = 0


class Mario(Person):
    def generate(self):
        Board.board[self.x][self.y] = self.char
        Board.board[self.x][self.y + 1] = self.char
        Board.board[self.x + 1][self.y] = self.char
        Board.board[self.x + 1][self.y + 1] = self.char

    def move(self):
        def alarmhandler(signum, frame):
            raise AlarmException

        def user_input(timeout=0.1):
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                text = getChar()()
                signal.alarm(0)
                return text
            except AlarmException:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''

        char = user_input()
        if char == 'b':
            os.system('aplay -q sound/smb2_jump.wav&')
            flag = 0
            for i in range(0, 20):
                for j in range(0, 8000):
                    if Board.board[i][j] == 'M' or Board.board[i][j] == 'm':
                        cur_X = i
                        cur_Y = j
                        flag = 1
                        break
                if flag:
                    break
            os.system('tput reset')
            Board.board[cur_X][cur_Y + 2] = 'B'
            Board.board[cur_X + 1][cur_Y + 2] = 'B'
            mng.update_score()
            x.print_board()
            mng.score()
            time.sleep(1)
            for i in range(cur_X, cur_X + 2):
                for j in range(cur_Y + 2, cur_Y + 5):
                    Board.board[i][j] = ' '
        if char == 'd':
            x1.execute_a()
        elif char == 'q':
            os.system('aplay -q sound/smb2_game_over.wav&')
            print("GAME OVER")
            quit()
        elif char == 'a':
            x1.execute_d()
        elif char == 'w':
            os.system('aplay -q sound/smb_jump.wav&')
            jmp = 0
            for i in range(0, 20):
                for j in range(0, 8000):
                    if Board.board[i][j] == 'M' or Board.board[i][j] == 'm':
                        cur_X = i
                        cur_Y = j
                        Board.board[i][j] = ' '
            cur_X = cur_X - 1
            cur_Y = cur_Y - 1
            os.system('tput reset')
            now = find.checkboard(cur_X - 12, cur_Y)
            while cur_X != 5:
                os.system('tput reset')
                now1 = find.checkboard(cur_X + 1, cur_Y)
                Board.board[cur_X - 1][cur_Y] = 'M'
                Board.board[cur_X - 1][cur_Y + 1] = 'M'
                Board.board[cur_X + 1][cur_Y] = ' '
                Board.board[cur_X + 1][cur_Y + 1] = ' '
                x.print_board()
                mng.score()
                then1 = find.checkboard(cur_X - 2, cur_Y)
                if then1 == 'pf' and now1 == 'mario':
                    cur_X = cur_X - 1
                    break
                x2 = user_input()
                if x2 == 'a':
                    x1.execute_d()
                elif x2 == 'd':
                    x1.execute_a()
                cur_X = cur_X - 1
            then = find.checkboard(cur_X, cur_Y)
            if now == 'coin' and then == 'mario':
                os.system('aplay -q sound/smb2_coin.wav&')
                mng.update_score()
            while(cur_X != 17):
                #	os.system('aplay -q sound/smb_jump.wav&')
                os.system('tput reset')
                now = find.checkboard(cur_X + 3, cur_Y)
                Board.board[cur_X][cur_Y] = ' '
                Board.board[cur_X][cur_Y + 1] = ' '
                Board.board[cur_X + 2][cur_Y] = 'M'
                Board.board[cur_X + 2][cur_Y + 1] = 'M'
                then = find.checkboard(cur_X + 1, cur_Y)
                cur_X = cur_X + 1
                x.print_board()
                mng.score()
                if now == 'pf' and then == 'mario':
                    jmp = 1
                    then = find.checkboard(cur_X + 2, cur_Y + 2)
                    if then == 'enemy':
                        mng.zero()
                        os.system('aplay -q sound/smb2_game_over.wav&')
                        print("GAME OVER")
                        quit()
                    else:
                        Board.board[cur_X][cur_Y + 3] = 'G'
                        Board.board[cur_X + 1][cur_Y + 3] = 'G'
                        time.sleep(0.1)
                    break
                x2 = user_input()
                if x2 == 'a':
                    x1.execute_d()
                elif x2 == 'd':
                    x1.execute_a()
