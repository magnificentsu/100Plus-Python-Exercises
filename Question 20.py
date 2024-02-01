# Define a class with a generator which can iterate the numbers, which are divisible by 7,
# between a given range 0 and n.

# Suppose the following input is supplied to the program: 7
# Then, the output should be:
# 0
# 7
# 14

#MY SOLUTION
class GeneratorClass:
    def __init__(self, n):
        self.n = n

    def generator_function(self):
        for i in range((self.n * 2) + 1):
            if i % 7 == 0:
                yield i

x = GeneratorClass(n=int(input('Give me a mumber:  ')))

for nums in x.generator_function():
    print(nums)

#COURSE SOLUTION
'''Solution by: Seawolf159
'''
class Divisible:

    def by_seven(self, n):
        for number in range(1,n + 1):
            if number % 7 == 0: yield number


divisible = Divisible()
generator = divisible.by_seven(int(input("Please insert a number. --> ")))
for number in generator:
    print(number)






