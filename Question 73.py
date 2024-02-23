# Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

#MY SOLUTION:
import random

my_list = range(100, 201, 2)
five_even = random.choices(my_list, k=5)

print(five_even)

#COURSE SOLUTION:
import random
resp = random.sample(range(100,201,2),5)
print(resp)
