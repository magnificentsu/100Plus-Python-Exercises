# Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# In case of input data being supplied to the question, it should be assumed to be a console input.

#MY SOLUTION
import sys

input1 = int(sys.argv[1])
input2 = int(sys.argv[2]) + 1

final_nums = []

for number in range(input1, input2):
    if all(int(digit) % 2 == 0 for digit in str(number)):
        final_nums.append(str(number))

print(','.join(final_nums))

#COURSE SOLUTION
lst = []

for i in range(1000,3001):
    flag = 1
    for j in str(i):          # every integer number i is converted into string
        if ord(j)%2 != 0:     # ord returns ASCII value and j is every digit of i
            flag = 0          # flag becomes zero if any odd digit found
    if flag == 1:
        lst.append(str(i))    # i is stored in list as string

print(",".join(lst))
