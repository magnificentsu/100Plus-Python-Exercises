# Write a program that computes the net amount of a bank account
# based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

#MY SOLUTION
print('Give me the transactions:')
transactions = []
balance = 0

while True:
    x = input()
    if len(x)== 0:
        break
    transactions.append(x)

for each_separate_transaction in transactions:
    y = each_separate_transaction.split(' ')
    if y[0] == 'D':
        balance += int(y[1])
    else:
        balance -= int(y[1])

print(balance)
print(f'Your current blance is ${balance}.00.')

#COURSE SOLUTION
total = 0
while True:
    s = input().split()
    if not s:            # break if the string is empty
        break
    cm,num = map(str,s)    # two inputs are distributed in cm and num in string data type

    if cm=='D':
        total+=int(num)
    if cm=='W':
        total-=int(num)

print(total)
