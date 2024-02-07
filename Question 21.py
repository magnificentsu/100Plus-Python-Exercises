# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance
# from current position after a sequence of movement and original point. If the distance is 
# a float, then just print the nearest integer.
# Example: If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be: 2

#MY SOLUTION:
import math

a = []
b = []

print('What\'s the input:')
x = input().split('\n')

for directions in x:
    y = directions.split()
    if y[0] == 'UP':
        a.append(int(y[1]))
    if y[0] == 'DOWN':
        a.append(-abs(int(y[1])))
    if y[0] == 'LEFT':
        b.append(-abs(int(y[1])))
    if y[0] == 'RIGHT':
        b.append(int(y[1]))


distance = math.sqrt((sum(a)**2) + (sum(b)**2))

print(round(distance))

#COURSE SOLUTION:
import  math

x,y = 0,0
while True:
    s = input().split()
    if not s:
        break
    if s[0]=='UP':                  # s[0] indicates command
        x-=int(s[1])                # s[1] indicates unit of move
    if s[0]=='DOWN':
        x+=int(s[1])
    if s[0]=='LEFT':
        y-=int(s[1])
    if s[0]=='RIGHT':
        y+=int(s[1])
                                    # N**P means N^P
dist = round(math.sqrt(x**2 + y**2))  # euclidean distance = square root of (x^2+y^2) and rounding it to nearest integer
print(dist)

