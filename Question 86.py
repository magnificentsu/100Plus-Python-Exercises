# By using list comprehension, please write a program to print the list after removing
# the value 24 in [12,24,35,24,88,120,155].

# MY SOLUTION:

# This is one way of doing this.
my_list = [12,24,35,24,88,120,155]
my_list.remove(24)
my_list.remove(24)
print(my_list)

# Another, and I think more efficient way of doing it.
new_list = [nums for nums in my_list if nums != 24]
print(new_list)

# COURSE SOLUTION:
li = [12,24,35,24,88,120,155]
li.remove(24)  # this will remove only the first occurrence of 24
print(li)