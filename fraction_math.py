'''
Fraction operations
'''

from fractions import Fraction

def add(a,b):
    print('Result of Addition: {0}'.format(a+b))

def sub(a,b):
    print('Result of Subtraction: {0}'.format(a-b))

def mult(a,b):
    print('Result of Multiplication: {0}'.format(a*b))

def div(a,b):
    print('Result of Division: {0}'.format(a/b))

if __name__ == '__main__':
    a = Fraction(input('Enter first fraction: '))
    b = Fraction(input('Enter second fraction: '))
    op = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
    if op == 'Add':
        add(a,b)
    if op == 'Subtract':
        sub(a,b)
    if op == 'Divide':
        div(a,b)
    if op == 'Multiply':
        mult(a,b)

    answer = input("Enter (e) to exit, enter to continue: ")
    if answer == 'e':
        break
        
