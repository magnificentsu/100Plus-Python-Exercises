# Define a function which can generate and print a tuple where the value are square
# of numbers between 1 and 20 (both included).

#MY SOLUTION:
def squared_tuple(x):
    y = tuple(nums**2 for nums in range(1, (x+1)))
    print(y)
    
squared_tuple(20)

#COURSE SOLUTION:

def printTupple():
    lst = [i ** 2 for i in range(1, 21)]
    print(tuple(lst))

printTupple()

        


