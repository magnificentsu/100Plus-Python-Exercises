# Please write assert statements to verify that every number in the list [2,4,6,8] is even.

#MY SOLUTION:
my_list = [2, 4, 6, 8]

for nums in my_list:
    assert nums % 2 == 0
    
#COURSE SOLUTION:
data = [2,4,5,6]
for i in data:
    assert i%2 == 0, "{} is not an even number".format(i)