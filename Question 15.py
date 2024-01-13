# Write a program that computes the value of a+aa+aaa+aaaa with a given
# digit as the value of a.

# Suppose the following input is supplied to the program: 9
# Then, the output should be: 11106

#MY SOLUTION
console_input = int(input('Give Me A Number:  '))

def manipulate_user_input(user_input):
    a = console_input
    result = a + a*11 + a*111 + a*1111
    return result

print(manipulate_user_input(console_input))

#COURSE SOLUTION
a = input()
total = int(a) + int(2*a) + int(3*a) + int(4*a)  # N*a=Na, for example  a="23", 2*a="2323",3*a="232323"
print(total)
