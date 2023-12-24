# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8
# Then, the output should be:40320

#MY ORIGINAL SOLUTION

def factorial_function(num):
    factorial = 1
    for numbers in range(1, num+1):
        factorial = factorial * numbers
    return factorial

print(factorial_function(int(input('What number do you want a factorial of? '))))

#COURSE SOLUTION 1

#COURSE SOLUTION 2  (USING WHILE LOOP)
n = int(input()) #input() function takes input as string type
                 #int() converts it to integer type
fact = 1
i = 1
while i <= n:
    fact = fact * i;
    i = i + 1
print(fact)

#COURSE SOLUTION 3 (USING FOR LOOP)
n = int(input()) #input() function takes input as string type
                #int() converts it to integer type
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)


