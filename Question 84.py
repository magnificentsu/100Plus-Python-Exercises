# By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

# MY SOLUTION:

my_list = [[[0 for i in range(8)] for j in range(5)] for k in range(3)]
print(my_list)


# COURSE SOLUTION:
array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)