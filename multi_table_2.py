'''
Multiplication table printer part 2
'''

def multi_table(a, b):

    for i in range(1, int(b + 1)):
        print('{0} x {1} = {2}'.format(a, i, a*i))

if __name__ == '__main__':
    a = input('Enter a number: ')
    b = float(input('How many multiples: '))
    if b > 0 and b.is_integer():
        multi_table(float(a), b)
    else:
        print("Multiple needs to be a positive integer.")
