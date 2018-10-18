'''
Unit converter
'''

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Kilograms to Pounds')
    print('4. Pounds to Kilograms')
    print('5. Celsius to Fahrenheit')
    print('6. Fahrenheit to Celsius')

def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609

    print('Distance in miles: {0}'.format(miles))

def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609

    print('Distance in kilometers: {0}'.format(km))

def kg_pounds():
    kg = float(input('Enter a weight in kilograms: '))
    pounds = kg * 2.20462

    print('Weight in pounds: {0}'.format(pounds))

def pounds_kg():
    pounds = float(input('Enter a weight in pounds: '))
    kg = pounds / 2.20462

    print('Weight in kilograms: {0}'.format(kg))

def cels_far():
    cels = float(input('Enter temperature in Celsius: '))
    far = ((cels*9)/5) + 32

    print('Temperature in Fahrenheit: {0}'.format(far))

def far_cels():
    far = float(input('Enter temperature in Fahrenheit: '))
    cels = (far - 32) * (5/9)

    print('Temperature in Celsius: {0}'.format(cels))

if __name__ == '__main__':
    while True:
        print_menu()
        choice = input('Which conversion would you like to do?: ')

        if choice == '1':
            km_miles()
            
        if choice == '2':
            miles_km()

        if choice == '3':
            kg_pounds()
            
        if choice == '4':
            pounds_kg()

        if choice == '5':
            cels_far()
            
        if choice == '6':
            far_cels()

        answer = input("Enter (e) to exit, enter to continue: ")
        if answer == 'e':
            break
        

        
