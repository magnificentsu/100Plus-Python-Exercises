# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first
# half values in one line and the last half values in one line.

#MY SOLUTION:

my_tuple = (1,2,3,4,5,6,7,8,9,10)
a = my_tuple[0:5]
b = my_tuple[5:]
print(a)
print(b)

#COURSE SOLUTION:
tpl = (1,2,3,4,5,6,7,8,9,10)

for i in range(0,5):
    print(tpl[i],end = ' ')
print()
for i in range(5,10):
    print(tpl[i],end = ' ')
    
    