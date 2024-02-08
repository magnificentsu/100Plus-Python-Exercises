# Define a function that can accept two strings as input and concatenate them and then print it in console.

#MY SOLUTION:
def concatenate_func(a, b):
    c = a + b
    print(c)
    
concatenate_func('hello ', 'world')

#COURSE SOLUTION 1:
def printValue(s1,s2):
    print s1 + s2

printValue("3","4") #34

#COURSE SOLUTION 2:
sum = lambda s1,s2 : s1 + s2
print(sum("10","45"))        # 1045



