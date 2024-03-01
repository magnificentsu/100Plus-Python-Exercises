# Please write a program which accepts a string from console and print the characters that have even indexes.
# Example: If the following string is given as input to the program:
# H1e2l3l4o5w6o7r8l9d
# Then, the output of the program should be: Helloworld

# MY SOLUTION:
print('Please enter a string:  ')
x = str(input())
print(x[0])
y = []

for k, v in enumerate(x):
    if k % 2 == 0:
        y.append(v)
print(''.join(y))
 
z = [x[i] for i in range(len(x)+1) if i % 2 == 0]
print(''.join(z))




# COURSE SOLUTION:
s = "H1e2l3l4o5w6o7r8l9d"
s = [ s[i] for i in range(len(s)) if i%2 ==0 ]
print(''.join(s))