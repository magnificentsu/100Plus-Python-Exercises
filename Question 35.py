# Define a function which can generate a list where the values are square of numbers
# between 1 and 20 (both included).
# Then the function needs to print the last 5 elements in the list.

#MY SOLUTION:
def square_func(x):
    y = []
    for nums in range (1, (x+1)):
        y.append(nums**2)
    print(y[-5:])
        
square_func(20)

#COURSE SOLUTION 1:
def printList():
    lst = [i ** 2 for i in range(1, 21)]
    for i in range(19,14,-1):
        print(lst[i])

printList()

#COURSE SOLUTION 2:
def squares(n):
    squares_list = [i**2 for i in range(1,n+1)]
    print(squares_list[-5:])
squares(20)


