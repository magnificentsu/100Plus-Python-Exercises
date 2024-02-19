# Define a class named American which has a static method called printNationality.

#MY SOLUTION:
    
class American:
    @staticmethod
    def printNationality():
        print("This is my Nationality")
  
American.printNationality()     
a = American()
a.printNationality()

#COURSE SOLUTION:
class American():
    @staticmethod
    def printNationality():
        print("I am American")

american = American()
american.printNationality()   # this will not run if @staticmethod does not decorates the function.
                              # Because the class has no instance.

American.printNationality()   # this will run even though the @staticmethod
                              # does not decorate printNationality()