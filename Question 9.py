# Write a program that accepts sequence of lines as input and prints the lines after
# making all characters in the sentence capitalized.
#
# Suppose the following input is supplied to the program:

#Hello world
#Practice makes perfect

#Then, the output should be:
#HELLO WORLD
#PRACTICE MAKES PERFECT

#MY SOLUTION
print("Type some words:  ")

input_lines = []

while True:
    line = input()
    if not line:
        break
    input_lines.append(line.upper())

for capitalized_line in input_lines:
    print(capitalized_line)

#COURSE SOLUTION
lst = []

while True:
    x = input()
    if len(x)==0:
        break
    lst.append(x.upper())

for line in lst:
    print(line)