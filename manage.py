from board import *
import time
import os


class Manage():
    def __init__(self):
        self.__pts = 0
        self.__live = 2
        self.__time = 100

    def score(self):
        print(Back.BLUE + str("SCORE: " + str(self.__pts)))
        print("LIVES LEFT: " + str(self.__live))
        print("TIME LEFT: " + str(self.__time))
        if self.__live == 0:
            print("Game Over")
            os.system('aplay -q sound/smb2_game_over.wav&')
            quit()

    def zero(self):
        manage.__live = 0

    def update_score(self):
        self.__pts = self.__pts + 4
        if self.__pts > 16 and self.__pts <= 20:
            os.system('aplay -q sound/smb_new.wav&')
            print(Fore.RED + "WELCOME TO LEVEL 2")
            time.sleep(1)
            Board.board[17][1] = ' '
            Board.board[17][2] = ' '
            Board.board[18][1] = ' '
            Board.board[18][2] = ' '
            Board.board[17][31] = 'M'
            Board.board[17][32] = 'M'
            Board.board[18][31] = 'M'
            Board.board[18][32] = 'M'
            level = 2

    def manage_lived(self):
        self.__live = self.__live - 1
        os.system('aplay -q sound/smb2_damage.wav&')

    def incr(self):
        self.__live = self.__live + 1

    def manage_time(self):
        if self.__time == 0:
            print("TIME-OUT")
            os.system('aplay -q sound/smb2_game_over.wav&')
            quit()
        else:
            self.__time = self.__time - 1
