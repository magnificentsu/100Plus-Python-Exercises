# Define a function that can receive two integer numbers in string form and compute
# their sum and then print it in console.

#MY SOLUTION:
def sum_function(a, b):
    c = int(a) + int(b)
    print(c)
    
sum_function(5, 3)

#COURSE SOUTION 1:
sum = lambda s1,s2 : int(s1) + int(s2)
print(sum("10","45"))      # 55

#COURSE SOUTION 2:
