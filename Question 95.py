# Given the participants' score sheet for your University Sports Day, you are required to 
# find the runner-up score. You are given scores. Store them in a list and find the
# score of the runner-up.
# If the following string is given as input to the program:
# 5 2 3 6 6 5
# Then, the output of the program should be: 5

# MY SOLUTION:
my_list = [5, 2, 3, 6, 6, 5]
my_list.sort()
x = tuple(set(my_list))

print(x[-2])

# COURSE SOLUTION 1:
n = int(input())
arr = map(int, input().split())
arr = list(set(arr))
arr.sort()
print(arr[-2])

# COURSE SOLUTION 2:


num = int(input())
scores = list(map(int, input().split(' ')))
winner = max(scores)
lst = []

if len(scores) != num:
    print('length of score is greater than input given')
else:
    for score in scores:
        if winner > score:
            lst.append(score)

runnerup = max(lst)
print(runnerup)