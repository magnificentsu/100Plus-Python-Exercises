# Define a class, which have a class parameter and have a same instance parameter.

#MY SOLUTION:

class MyClasses:
    class_name1 = 'My First Class'
    class_name2 = 'My Second Class'
    class_name3 = 'My Third Class'
    
    def _init__(self, class_name1=None, class_name2=None, class_name3=None):
        self.class_name1 = class_name1
        self.class_name2 = class_name2
        self.class_name3 = class_name3
        
        
class1 = MyClasses()
class1.class_name1 = 'Machine Learning'
print(class1.class_name1)

class2 = MyClasses()
class2.class_name2 = "Intro to Python Application"
print(class2.class_name2)

class3 = MyClasses()
print(class3.class_name3)

#COURSE SOLUTION:
class Car:
    name = "Car"

    def __init__(self,name = None):
        self.name = name

honda=Car("Honda")
print("%s name is %s"%(Car.name,honda.name))

toyota=Car()
toyota.name="Toyota"
print("%s name is %s"%(Car.name,toyota.name))

