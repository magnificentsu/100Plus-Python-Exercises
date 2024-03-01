# Please write a program which accepts a string from console and print it in reverse order.
# Example: If the following string is given as input to the program:*
# rise to vote sir
# Then, the output of the program should be:
# ris etov ot esir

# MY SOLUTION:
print('Please enter a string:  ')
x = str(input())
y = x[::-1]
z = reversed(x)
print(y)
print(''.join(z))

# COURSE SOLUTION:
s = input()
s = ''.join(reversed(s))
print(s)

