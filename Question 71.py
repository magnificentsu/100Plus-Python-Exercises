# Please write a program to output a random number, which is divisible by 5 and 7,
# between 10 and 150 inclusive using random module and list comprehension.

#MY SOLUTION:
import random

my_list = [i for i in range(10, 151) if i % 5 == 0 and i % 7 == 0]
random_number = random.choice(my_list)
print(random_number)

#COURSE SOLUTION:
import random
resp = [i for i in range(10,151) if i % 35 == 0 ]
print(random.choice(resp))

