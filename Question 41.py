# Write a program which can map() to make a list whose elements
# are square of elements in [1,2,3,4,5,6,7,8,9,10].

#MY SOLUTION:
my_list = [1,2,3,4,5,6,7,8,9,10]
def square_func(x):
    return x**2
    
new_list = list(map(square_func, my_list))
print(new_list)
    
#COURSE SOLUTION:
# No different way of code is written as the requirment is specificly mentioned in problem description

li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)  # returns map type object data
print(list(squaredNumbers))               # converting the object into list

