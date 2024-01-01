# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 _ C _ D)/H]

# Following are the fixed values of C and H:
# C is 50. H is 30.

# D is the variable whose values should be input to your program in a comma-separated sequence.
# For example Let us assume the following comma separated input sequence is given to the program:

#100,150,180
# The output of the program should be:
# 18,22,24

#MY SOLUTION
import math

c = 50
h = 30
given_d = input('Input some numbers:  ')
actual_d = given_d.split(',')

var1 = int(actual_d[0])
var2 = int(actual_d[1])
var3 = int(actual_d[2])

q1 = round(math.sqrt((2 * c * var1)/h))
q2 = round(math.sqrt((2 * c * var2)/h))
q3 = round(math.sqrt((2 * c * var3)/h))


print(q1,q2,q3, sep=', ')

#COURSE SOLUTION
from math import sqrt # import specific functions as importing all using *
                      # is bad practice

C,H = 50,30

def calc(D):
    return sqrt((2*C*D)/H)

D = [int(i) for i in input().split(',')] # splits in comma position and set up in list
D = [int(i) for i in D]   # converts string to integer
D = [calc(i) for i in D]  # returns floating value by calc method for every item in D
D = [round(i) for i in D] # All the floating values are rounded
D = [str(i) for i in D]   # All the integers are converted to string to be able to apply join operation

print(",".join(D))