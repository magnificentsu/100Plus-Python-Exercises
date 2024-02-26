# By using list comprehension, please write a program to print the list after removing
# the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

# MY SOLUTION:
my_list = [12,24,35,70,88,120,155]

new_list = [v for k, v in enumerate(my_list) if k != 0 and k != 4 and k != 5]
print(new_list)

# COURSE SOLUTION:

li = [12,24,35,70,88,120,155]
li = [li[i] for i in range(len(li)) if i not in (0,4,5)]
print(li)


