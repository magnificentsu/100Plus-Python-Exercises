# Write a program which accepts a sequence of comma separated 4 digit binary numbers
# as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.

#MY SOLUTION
input_numbers = input('Enter Some Numbers:  ')
given_binary_numbers = input_numbers.split(',')
my_list = []

for numbers in given_binary_numbers:
    converted_numbers = int(numbers, 2)
    my_list.append(converted_numbers)
for digits in my_list:
    if digits % 5 == 0:
        print(bin(digits)[2:])

#COURSE SOLUTION
def check(x):                       # converts binary to integer & returns zero if divisible by 5
    total,pw = 0,1
    reversed(x)

    for i in x:
        total+=pw * (ord(i) - 48)   # ord() function returns ASCII value
        pw*=2
    return total % 5

data = input().split(",")           # inputs taken here and splited in ',' position
lst = []

for i in data:
    if check(i) == 0:               # if zero found it means divisible by zero and added to the list
        lst.append(i)

print(",".join(lst))

