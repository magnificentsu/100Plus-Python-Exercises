# Please write a program to print the running time of execution of "1+1" for 100 times.

#MY SOLUTION:
import time
x = 1+1

def my_func():
    return 1+1

time_before = time.time()
for _ in range(101):
    my_func()
time_after = time.time()
run_time = time_after - time_before
print(run_time)

#COURSE SOLUTION:
import time

before = time.time()
for i in range(100):
    x = 1 + 1
after = time.time()
execution_time = after - before
print(execution_time)