# With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list
# after removing all duplicate values with original order reserved.

# MY SOLUTION:
my_list = [12,24,35,24,88,120,155,88,120,155]

for nums in my_list:
    if my_list.count(nums) > 1:
        my_list.remove(nums)
        
print(my_list)

# COURSE SOLUTION:

li = [12,24,35,24,88,120,155,88,120,155]
for i in li:
    if li.count(i) > 1:
        li.remove(i)
print(li)

