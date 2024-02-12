# Define a function which can generate and print a list where the values are 
# square of numbers between 1 and 20 (both included).

#MY SOLUTION:
def square_func(x):
    y = []
    for nums in range(1, (x+1)):
        y.append(nums**2)
    print(y)
        
square_func(20)

#COURSE SOLUTION:
def printList():
    lst = [i ** 2 for i in range(1, 21)]
    print(lst)

printList()

