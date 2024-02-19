# Write a program which accepts a string as input to print "Yes" if the string
# is "yes" or "YES" or "Yes", otherwise print "No".

#MY SOLUTION:
print('Type yes whatever way you want:')
a = str(input())

if a == 'yes':
    print('Yes')
elif a == 'YES':
    print('Yes')
elif a == 'Yes':
    print('Yes')
else:
    print('No')

#COURSE SOLUTION:
text = input("Please type something. --> ")
if text == "yes" or text == "YES" or text == "Yes":
    print("Yes")
else:
    print("No")