# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:

# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
#or:2
# to:1

#MY SOLUTION:
print('Type a sentence:')
x = input().split()
count = {}

for words in x:
    if words in count:
        count[words] += 1
    else:
        count[words] = 1


for key, value in sorted(count.items()):
    print(f'{key}: {value}')
    
#COURSE SOLUTION 1:
ss = input().split()
dict = {}
for i in ss:
    i = dict.setdefault(i,ss.count(i))    # setdefault() function takes key & value to set it as dictionary.

dict = sorted(dict.items())               # items() function returns both key & value of dictionary as a list
                                          # and then sorted. The sort by default occurs in order of 1st -> 2nd key
for i in dict:
    print("%s:%d"%(i[0],i[1]))
    
#COURSE SOLUTION 2:
from collections import Counter

ss = input().split()
ss = Counter(ss)         # returns key & frequency as a dictionary
ss = sorted(ss.items())  # returns as a tuple list

for i in ss:
    print("%s:%d"%(i[0],i[1]))

#COURSE SOLUTION 3:
ss = input().split()
dict = {i:ss.count(i) for i in ss}     # sets dictionary as i-> split word & ss.count(i) -> total occurrence of i in ss
dict = sorted(dict.items())            # items() function returns both key & value of dictionary as a list
                                       # and then sorted. The sort by default occurs in order of 1st -> 2nd key
for i in dict:
    print("%s:%d"%(i[0],i[1]))
    
    
        