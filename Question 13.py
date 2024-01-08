# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123

#MY SOLUTION
import re

user_input = input('Type Something:  ')

number_of_letters = len(re.findall(r"[a-zA-Z]", user_input))
# print(number_of_letters)

number_of_digits = len(re.findall(r"\d", user_input))
# print(number_of_digits)

print(f'LETTERS {number_of_letters}')
print(f'DIGITS {number_of_digits}')

#COURSE SOLUTION
word = input()
letter,digit = 0,0

for i in word:
    if ('a'<=i and i<='z') or ('A'<=i and i<='Z'):
        letter+=1
    if '0'<=i and i<='9':
        digit+=1

print("LETTERS {0}\nDIGITS {1}".format(letter,digit))