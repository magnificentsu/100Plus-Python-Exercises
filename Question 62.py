# The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n input by console.
# Example: If the following n is given as input to the program: 7
# Then, the output of the program should be: 0,1,1,2,3,5,8,13
# In case of input data being supplied to the question, it should be assumed to be a console input.

#MY SOLUTION:
print("Please enter a number: ")

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)
        
n = int(input())
        
x = [str(f(nums)) for nums in range(n+1)]
print(','.join(x))

#COURSE SOLUTION
def f(n):
    if n < 2:
        fibo[n] = n
        return fibo[n]
    fibo[n] = f(n-1) + f(n-2)
    return fibo[n]

n = int(input())
fibo = [0]*(n+1)  # initialize a list of size (n+1)
f(n)              # call once and it will set value to fibo[0-n]
fibo = [str(i) for i in fibo]   # converting integer data to string type
ans = ",".join(fibo)    # joining all string element of fibo with ',' character
print(ans)