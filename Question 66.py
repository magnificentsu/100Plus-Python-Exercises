# Please write a program which accepts basic mathematic expression from console
# and print the evaluation result.
# Example: If the following n is given as input to the program: 35 + 3
# Then, the output of the program should be: 38

#MY SOLUTION:
print('Give me a basic mathematic problem to solve: ')
y = input()
response = eval(y)
print(response)

#COURSE SOLUTION:
expression = input()
ans = eval(expression)
print(ans)

