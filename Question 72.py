# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

#MY SOLUTION
import random

my_list = range(100, 201)
generated_list = random.choices(my_list, k=5)

print(generated_list)

#COURSE SOLUTION:
import random
resp = random.sample(range(100,201),5)
print(resp)

