'''
Even-odd vending machine

INPUT: positive integer
OUTPUT: Print whether number is even or odd
'''

def even_odd_vendor(num):
    if num % 2 == 0:
        print("even")
    else:
        print('odd')
    for i in range(1,10):
        print(num + 2*i)

            

if __name__ == '__main__':
    a= float(input('Enter a number: '))
    if a > 0 and a.is_integer():
        even_odd_vendor(int(a))
    else:
        a = ("Please enter a positive integer.")

