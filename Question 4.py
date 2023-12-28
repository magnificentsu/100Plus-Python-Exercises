# Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98

#MY SOLUTION
given_numbers = input('Give me some values:   ')
my_list = given_numbers.split(',')
print(my_list)


tuple_list = tuple(my_list)
print(tuple_list)

#COURSE SOLUTION
lst = input().split(',')  # the input is being taken as string and as it is string it has a built in
                          # method name split. ',' inside split function does split where it finds any ','
                          # and save the input as list in lst variable

tpl = tuple(lst)          # tuple method converts list to tuple

print(lst)
print(tpl)
