# Write a function to compute 5/0 and use try/except to catch the exceptions.

#MY SOLUTION:
def div_func(x, y):
    if y == 0:
        raise RuntimeError('Integers are not divisible by 0')
    else:
        return  x/y
        
try:
    div1 = div_func(5, 0)
    print(div1)
except RuntimeError as err:
    print('There was an error:', err)
    
#COURSE SOLUTION:
def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print("Why on earth you are dividing a number by ZERO!!")
except:
    print("Any other exception")
    
    