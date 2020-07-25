# Mario

## Rules of the Game:
1. Press 'w' for jump
2. Press 'a' to move towards right
3. Press 'd' to move towards left
4. There is timer of 90 minutes.Once the timer finishes game will be over.
5. You are having 2 lives.If you encounter a gem your live will be incresed by 1.But if you encounter the stationary enemy or boss enemy your live will be decreased by 1. 
6. To kill enemies or to break obstacles press 'b'.This will increase your score by 1 if they are killed successfully
7. Collecting coins will also increase your score by 4

## board.py
Prints 20x64 board on screen with walls , obstacles and emepty spaces.It has print function to print the board

## person.py
It contains functions for generating and moving enemy and mario.

## mario.py
It contains functions to move the mario when a key is pressed from 'w,a,d'.On pressing 'b' bomb will be planted.

## enemy.py
The Enemy class is used for generating and moving enemies

## manage.py
Manages score,lives and time of the game

## coin.py
To create coins

Highlights:
1. If mario will come in contact with the sad enemy represented by :(,Mario will change from 'M' to 'm' and the enmey will change to :).
2. Use of colorama
3. When score will be greater than 16,mario will enter into level 2 and his position will be changed
4. Sound is played when game starts,game ends,live of mario is decreased etc.
