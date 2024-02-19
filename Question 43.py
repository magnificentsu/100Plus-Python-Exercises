# Write a program which can filter() to make a list whose elements are even 
# number between 1 and 20 (both included).

#MY SOLUTION:

my_list = range(1, 21)
def is_even(x):
    return x % 2 == 0
    
my_new_list = list(filter(is_even, my_list))
print(my_new_list)

#COURSE SOLUTION:
def even(x):
    return x%2==0

evenNumbers = filter(even, range(1,21))
print(list(evenNumbers))

