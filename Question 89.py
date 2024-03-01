# Define a class Person and its two child classes: Male and Female. All classes have
# a method "getGender" which can print "Male" for Male class and "Female" for Female class.

# MY SOLUTION:
class Person:
    def getGender(self):
        print('Could be Male or Female')

class Male(Person):
    def getGender(self):
        print('Male')
    
class Female(Person):
    def getGender(self):
        print('Female')

male = Male()
female = Female()
male.getGender()
female.getGender()

# COURSE SOLUTION:
class Person(object):
    def __init__(self):
        self.gender = "unknown"

    def getGender(self):
        print(self.gender)

class Male(Person):
    def __init__(self):
        self.gender = "Male"

class Female(Person):
    def __init__(self):
        self.gender = "Female"

sharon = Female()
doug = Male()
sharon.getGender()
doug.getGender()