# Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

# MY SOLUTION

my_list = [5,6,77,45,22,12,24]

no_even_numbers_list = [nums for nums in my_list if nums % 2 != 0]
print(no_even_numbers_list)

# COURSE SOLUTION:
def isEven(n):
    return n%2!=0

li = [5,6,77,45,22,12,24]
lst = list(filter(isEven,li))
print(lst)

