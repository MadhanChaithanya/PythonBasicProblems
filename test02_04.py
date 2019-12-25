'''
Program-2
Add Two Numbers in Python
Python Program to Add Two Numbers

Our task is to simplify add two numbers input by the user.

'''
'''
Method-4 : Add two numbers using functions:
'''


# program to add two numbers using functions:

def add(a, b):  # user-defined function
    sum = a + b  # adding 2 numbers
    return sum


# taking input from the user
a = int(input('Enter your first number:     '))
b = int(input('Enter your second number:    '))

#function call
print(add(a,b))