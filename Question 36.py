# Define a function which can generate a list where the values are square of numbers
# between 1 and 20 (both included).
# Then the function needs to print all values except the first 5 elements in the list.

#MY SOLUTION:
def square_func(x):
    y = []
    for nums in range (1, (x+1)):
        y.append(nums**2)
    print(y[5:])
        
square_func(20)

#COURSE SOLUTION:
def printList():
    lst = [i ** 2 for i in range(1, 21)]
    for i in range(5,20):
        print(lst[i])

printList()

