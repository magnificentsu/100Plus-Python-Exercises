# Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

#MY SOLUTION:
ascii_string = 'what it is what it do'
unicode_string = ascii_string
encoded_string = unicode_string.encode('utf-8')
print(encoded_string)

#COURSE SOLUTION:
s = input()
u = s.encode('utf-8')
print(u)

