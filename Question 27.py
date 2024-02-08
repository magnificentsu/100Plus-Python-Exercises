# Define a function that can convert a integer into a string and print it in console.

#MY SOLUTION:
def integer_converter(x):
    print(str(x))
    print(type(x))
    

integer_converter(input('Enter a number:  '))

#COURSE SOLUTION:
conv = lambda x : str(x)
n = conv(10)
print(n)
print(type(n))            # checks the type of the variable

