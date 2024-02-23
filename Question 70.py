# Please write a program to output a random even number between 0 and 10 inclusive using random 
# module and list comprehension

#MY SOLUTION:
import random

#This is one way of doing it.
random_even = [random.randrange(0, 11, 2)]
print(random_even)

#Another way of doing it.
my_list = [i for i in range(11) if int(i) % 2 == 0]
random_even2 = random.choice(my_list)
print(random_even2)

#COURSE SOLUTION:
import random
resp = [i for i in range(0,11,2)]
print(random.choice(resp))