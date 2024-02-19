# Define a class named American and its subclass NewYorker.

#MY SOLUTION:
class American:
    pass

class NewYorker(American):
    pass

an_american = American()
a_new_yorker = NewYorker()

#COURSE SOLUTION:
class American():
    pass

class NewYorker(American):
    pass

american = American()
newyorker = NewYorker()

print(american)
print(newyorker)