# Write a program which can map() to make a list whose elements are square
# of numbers between 1 and 20 (both included).

#MY SOLUTION:
def square_func(x):
    return x**2
    
my_list = list(map(square_func, range(1, 21)))
print(my_list)

#COURSE SOLUTION:
def sqr(x):
    return x*x

squaredNumbers = list(map(sqr, range(1,21)))
print (squaredNumbers)

