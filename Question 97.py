# You are given an integer, N. Your task is to print an alphabet rangoli of size N.
# (Rangoli is a form of Indian folk art based on creation of patterns.)
# Different sizes of alphabet rangoli are shown below:

# #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# MY SOLUTION:

def rangoli_func(n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = alphabet[0:n]
    rangoli= []
    for i in range(n):
        
    rangoli.append('-'.join(letters[::-1]))
    rangoli.append('-'.join(letters[1:]))
    
    print('-'.join(rangoli))
    
rangoli_func(3)

#part one done, need to get the other lines and replicate it
#once replicated the job is to simplify