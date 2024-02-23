# Please write a program to randomly generate a list with 5 numbers, which are divisible
# by 5 and 7 , between 1 and 1000 inclusive.

#MY SOLUTION:
import random

my_list = [i for i in range(1, 1001) if i % 35 == 0]
random_list = random.choices(my_list, k=5)

print(random_list)

#COURSE SOLUTION:
import random
lst = [i for i in range(1,1001) if i%35 == 0]
resp = random.sample(lst,5)
print(resp)