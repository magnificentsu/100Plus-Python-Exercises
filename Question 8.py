# Write a program that accepts a comma separated sequence of words as input
# and prints the words in a comma-separated sequence after sorting them alphabetically.

# Suppose the following input is supplied to the program:

# without,hello,bag,world

# Then, the output should be:

# bag,hello,without,world

#MY SOLUTION
user_words = input('Enter some words:  ')
x = user_words.split(',')
y = sorted(x)

print(y[0], y[1], y[2], y[3], sep=',')

#COURSE SOLUTION
lst = input().split(',')
lst.sort()
print(",".join(lst))