# Write a program that accepts a sentence and calculate the number of upper case letters
# and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!

#MY SOLUTION
import re

user_input = input('Type Something:  ')

upper_case_letters = len(re.findall(r'[A-Z]', user_input))
# print(upper_case_letters)
lower_case_letters = len(re.findall(r'[a-z]', user_input))
# print(lower_case_letters)

print(f'UPPER CASE {upper_case_letters}')
print(f'LOWER CASE {lower_case_letters}')

#COURSE SOLUTION
word = input()
upper,lower = 0,0

for i in word:
    if 'a'<=i and i<='z' :
        lower+=1
    if 'A'<=i and i<='Z':
        upper+=1

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))
