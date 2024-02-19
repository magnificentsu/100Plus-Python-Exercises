# Define a custom exception class which takes a string message as attribute.

#MY SOLUTION:
class MyException(Exception):
    "This is my own personal exception class"
    def __init__(self, message):
        self.message = message
        
error = MyException('something must\'ve went wrong, try again')
print(error)



#COURSE SOLUTION
class CustomException(Exception):
    """Exception raised for custom purpose

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


num = int(input())

try:
    if num < 10:
        raise CustomException("Input is less than 10")
    elif num > 10:
        raise CustomException("Input is grater than 10")
except CustomException as ce:
    print("The error raised: " + ce.message)
