# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.
# >Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9
# Then, the output should be: 1,9,25,49,81

#MY SOLUTION

a = input('Give Me Some Numbers:   ')
b = a.split(',')

l2 = [str(x) for x in [int(d)**2 for d in b if int(d) % 2 != 0]]
print(','.join(l2))

#COURSE SOLUTION
lst = [str(int(i)**2) for i in input().split(',') if int(i) % 2]
print(",".join(lst))


