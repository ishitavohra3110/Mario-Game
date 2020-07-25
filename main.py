import time,os
from board import *
from mario import *
from enemy import *
from coin import *
os.system('aplay -q sound/smb_new.wav&')
player = Mario('M',17,1)
x.generate()
player.generate()
for j in range(0,8000):
	if j%20 == 8:
		alien = Enemy('e',9,j)
		enemies.append(alien)
		alien.generate()
		alien = Enemy('e',10,j)
		alien.generate()
	elif j%20 == 18:
		alien = Enemy(':',17,j)
		alien.generate()
		alien = Enemy(':',18,j)
		alien.generate()
	elif j%20 == 19:
		alien = Enemy('(',17,j)
		alien.generate()
		alien = Enemy('(',18,j)
		alien.generate()
	count = 1
	while count < 17:
		if j%20 == count and Board.board[7][j]!='X' and Board.board[8][j]!='X' and j<7999:
			dollar  = Coin('$',5,j)
			dollar.generatecoin()
			dollar  = Coin('$',6,j)
			dollar.generatecoin()
			dollar  = Coin('$',5,j+1)
			dollar.generatecoin()
			dollar  = Coin('$',6,j+1)
			dollar.generatecoin()
		count = count+12
	count = 14
	while count < 17:
		if j%20 == count and Board.board[7][j]!='X' and Board.board[8][j]!='X' and j<7999:
			dollar  = Coin('G',9,j)
			dollar.generatecoin()
			dollar  = Coin('G',10,j)
			dollar.generatecoin()
		count = count+6
player.print_board()
i = 0
while True:
	count = 3
	while count:
		os.system('tput reset')
		i = 0
		for i in enemies:
			i.execute_a()
		player.print_board()
		mng.score()
		player.move()
		count = count-1
	count = 3
	while count:
		i = 0
		os.system('tput reset')
		for i in enemies:
			i.execute_d()
		player.print_board()
		mng.score()
		player.move()
		count = count-1
	mng.manage_time()

