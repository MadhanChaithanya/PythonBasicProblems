'''
Program-2
Add Two Numbers in Python
Python Program to Add Two Numbers

Our task is to simplify add two numbers input by the user.

'''
'''
Method-5 : Add two numbers using functions:
'''
# program to add two numbers using bitwise functions:
def add_without_plus_operator(a, b):
    while b != 0:
        data = a & b
        a = a^b
        b = data << 1
    return a

a = int(input('Enter your first input:  '))
b = int(input('Enter your second input: '))
print(add_without_plus_operator(a,b))