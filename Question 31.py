# Define a function which can print a dictionary where the keys are numbers 
# between 1 and 20 (both included) and the values are square of keys.

#MY SOLUTION:
def my_dict_func(x):
    my_dict = {}
    y = range(1, (x+1))
    for nums in y:
        my_dict[nums] = nums**2
    print(my_dict)
        
my_dict_func(20)

#COURSE SOLUTION 1:
def printDict():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    print d

printDict()

#COURSE SOLUTION 2:
def printDict():
    dict={i:i**2 for i in range(1,21)}   # Using comprehension method and
    print(dict)

printDict()
