# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
# Example: If the following n is given as input to the program: 5
# Then, the output of the program should be: 3.55
# In case of input data being supplied to the question, it should be assumed to be a console input.

#MY SOLUTION:
print('Give me a number: ')
x = int(input())
y = []
for nums in range(x+1):
    z = (nums/(nums+1))
    y.append(z)

print(round(sum(y), 2))

#COURSE SOLUTION:
n = int(input())
sum = 0
for i in range(1, n+1):
    sum+= i/(i+1)
print(round(sum, 2))  # rounded to 2 decimal point


    
