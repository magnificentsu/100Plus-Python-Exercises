# Write a program which will find all such numbers which are divisible by 7,
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.


#MY SOLUTION
special_list = []
for numbers in range(2000, 3201):
    if numbers % 7 == 0 and numbers % 5 != 0:
        special_list.append(numbers)

print(special_list)

#COURSE SOLUTION 1
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print (','.join(l))

#COURSE SOLUTION 2
for i in range(2000,3201):
    if i%7 == 0 and i%5!=0:
        print(i,end=',')
print("\b")
