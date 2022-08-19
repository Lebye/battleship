import random
import os
print("WELCOME TO MY GAME CALLED BATTLESHIP HIT")
print('____________________________________')
print('|  1   |  2   |  3   |   4  |  5   |')
print('|  6   |  7  |   8   |   9  |  10  |')
print('|  11  |  12  |  13  |  14  |  15  |')
print('|  16  |  17  |  18  |  19  |  20  |')
print('|  21  |  22  |  23  |  24  |  25  |')
print('_____________________________________')

print('this is the map of the sea, I have divided this map into 25 segments. The segments which contains the enemy ship!!!')
print('You are the commander of the ship, only one enemy ship is left to hit in a single shot. If we dont hit, they will do it for sure')
print('xxxxx')

i= input('choose the segment to hit from (1 to 25):-')
g= random.randint(1, 5)
j= int(i)

if (j==g):
    print('\n we won commander!! enemy ship is destroyed')
else:
    print('\n we lost xxxxx the ship was at',g)