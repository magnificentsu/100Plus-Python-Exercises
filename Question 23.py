# Write a method which can calculate square value of number.

#MY SOLUTION:
print('Enter a number:')

class RandomClass:
    def square_val(self, x):
        return x**2
        
y = RandomClass()
print(y.square_val(int(input())))

#COURSE SOLUTION 1:
n=int(input())
print(n**2)

#COURSE SOLUTION 2:
def square(num):
    return num ** 2

print square(2)
print square(3)




        