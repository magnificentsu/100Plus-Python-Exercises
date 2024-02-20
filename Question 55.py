# Write a program which accepts a sequence of words separated by whitespace as input to print
# the words composed of digits only.
# Example: If the following words is given as input to the program:
# 2 cats and 3 dogs.
# Then, the output of the program should be: ['2', '3']
# In case of input data being supplied to the question, it should be assumed to be a console input.

#MY SOLUTION:
import re

print("Type a sentence of any kind: ")

x = input()
y = []
pattern = r'-?\d+(\.\d+)?'

for words in x.split():
    if re.findall(pattern, words):
        y.append(words)

print(y)

#COURSE SOLUTION 1:
import re

email = input()
pattern = "\d+"
ans = re.findall(pattern,email)
print(ans)

#COURSE SOLUTION 2:
email = input().split()
ans = []
for word in email:
    if word.isdigit():     # can also use isnumeric() / isdecimal() function instead
       ans.append(word)
print(ans)

