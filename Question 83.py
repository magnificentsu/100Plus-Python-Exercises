# By using list comprehension, please write a program to print the list after removing
# the 2nd - 4th numbers in [12,24,35,70,88,120,155].

# MY SOLUTION:
my_list = [12,24,35,70,88,120,155]

new_list = [v for k, v in enumerate(my_list) if k < 1 or k > 3]
print(new_list)

# COURSE SOLUTION 1
li = [12,24,35,70,88,120,155]
li = [li[i] for i in range(len(li)) if i < 3 or i > 4]
print(li)

# COURSE SOLUTION 2
lst = [12,24,35,70,88,120,155]
print([i for i in lst if lst.index(i) not in range(2,5)])

# I like COURSE SOLUTION 2. I've never, to this point, seen a solution to a similar problem
# look like this. Now I'm curious which of these would be considered the best, or the most
# efficient method of solving/answering the probem in this exercise.