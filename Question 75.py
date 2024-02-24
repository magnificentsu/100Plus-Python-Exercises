# Please write a program to randomly print a integer number between 7 and 15 inclusive.

#MY SOLUTION:
import random

random_number = random.choice(range(7, 16))
print(random_number)

#COURSE SOLUTION:
import random
print random.randrange(7,16)
