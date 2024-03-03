# You are given a string S and width W. Your task is to wrap the string into a paragraph of width.
# If the following string is given as input to the program: 
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Then, the output of the program should be:
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

# MY SOLUTION:
def string_wrapper(string, width):
    lines = []
    for itms in range(0, (len(string)+1), width):
        lines.append(string[itms: itms+width])
    return lines
    
string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
width = 4

x = string_wrapper(string, width)
for y in x:
    print(y)

# COURSE SOLUTION 1:
import textwrap

def wrap(string, max_width):
    string = textwrap.wrap(string,max_width)
    string = "\n".join(string)
    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
# COURSE SOLUTION 2:
import textwrap

string = input()
width = int(input())

print(textwrap.fill(string,width))


# COURSE SOLUTION 3:
import itertools
string = input("> ")
width_length = int(input("What is the width of the groupings? "))

def grouper(string, width):
    iters = [iter(string)] * width
    return itertools.zip_longest(*iters, fillvalue='')

def displayer(groups):
    for x in groups:
        if x == '':
            continue
        else:
            print(''.join(x))

displayer(grouper(string, width_length))