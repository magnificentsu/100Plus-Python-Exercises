# Write a program which can map() and filter() to make a list whose elements
# are square of even number in [1,2,3,4,5,6,7,8,9,10].

#MY SOLUTION:
reg_list = [1,2,3,4,5,6,7,8,9,10]

def even_func(x):
    return x % 2 == 0
    
def square_func(y):
    return y**2

even_list = filter(even_func, reg_list)
even_list_squared = map(square_func, even_list)


print(list(even_list_squared))

#COURSE SOLUTION:
def even(x):
    return x%2==0

def squer(x):
    return x*x

li = [1,2,3,4,5,6,7,8,9,10]
li = map(squer,filter(even,li))   # first filters number by even number and the apply map() on the resultant elements
print(list(li))
