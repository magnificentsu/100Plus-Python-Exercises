# Define a function which can compute the sum of two numbers.

#MY SOLUTION:
def sum_function(x, y):
    return x + y
    
def sum_function2(a, b):
    print(a + b)
    
z = sum_function(1, 2)
print(z)

sum_function2(2, 2)

#COURSE SOLUTION:
sum = lambda n1,n2 : n1 + n2      # here lambda is use to define little function as sum
print(sum(1,2))

