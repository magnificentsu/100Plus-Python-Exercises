# Please write a program which prints all permutations of [1,2,3]

# MY SOLUTION:
from itertools import permutations

my_list = [1, 2, 3]

my_list_permutations = permutations(my_list)
for all_permutations in my_list_permutations:
    print(all_permutations)

# COURSE SOLUTION:

from itertools import permutations

def permuation_generator(iterable):
    p = permutations(iterable)
    for i in p:
        print(i)


x = [1,2,3]
permuation_generator(x)