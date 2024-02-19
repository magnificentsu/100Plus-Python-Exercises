# Please raise a RuntimeError exception.

#MY SOLUTION:
def sum_func(x, y):
    if x + y < 8:
        raise RuntimeError('Sum is is less than 8')
    else:
        return x + y
        
total1 = sum_func(4, 4)
print(total1)
total2 = sum_func(2, 2)
print(total2)

#COURSE SOLUTION
raise RuntimeError('something wrong')