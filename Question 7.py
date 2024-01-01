# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i _ j.*

# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

# Then, the output of the program should be:

# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

#MY SOLUTION

x = input('Enter some numbers: ')
y = x.split(',')
a = int(y[0])
b = int(y[1])

final_output = [[1 for num in range(b)] for num in range(a)]

print(final_output)

#Still working on this