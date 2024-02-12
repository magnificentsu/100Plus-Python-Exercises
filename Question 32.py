# Define a function which can generate a dictionary where the keys are numbers 
# between 1 and 20 (both included) and the values are square of keys.
# The function should just print the keys only.

#MY SOLUTION:
def my_dict_func(x):
    my_dict = {}
    for nums in range(1, (x+1)):
        my_dict[nums] = nums**2
    print(my_dict.keys())
    
    
my_dict_func(20)

#COURSE SOLUTION:
def printDict():
    dict = {i: i**2 for i in range(1, 21)}
    print(dict.keys())      # print keys of a dictionary

printDict()

