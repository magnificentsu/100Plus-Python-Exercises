#Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

#MY SOLUTION
class StringManipulator:
    def __init__(self):
        self.user_prompt = ''

    def get_string(self):
        self.user_prompt = input('Enter a sentence:  ')

    def print_string(self):
        print(self.user_prompt.upper())


user_string = StringManipulator()
user_string.get_string()
user_string.print_string()






