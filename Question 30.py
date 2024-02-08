# Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.

#MY SOLUTION:
def string_print_func(a, b):
    if len(a) > len(b):
        print(a)
    elif len(b) > len(a):
        print(b)
    elif len(a) == len(b):
        print(a)
        print(b)

string_print_func('abababababa', 'abababababac')

#COURSE SOLUTION:
def printVal(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        print(s1)
    elif len1 < len2:
        print(s2)
    else:
        print(s1)
        print(s2)

s1,s2=input().split()
printVal(s1,s2)