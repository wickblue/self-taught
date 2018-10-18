'''
Creates bar chart listing weekly expenditures
'''

import matplotlib.pyplot as plt

def draw_bar(data, labels):

    # Number of bars
    num_bars = len(data)

    # This list is the point on y-axis where each bar is scentered
    positions = range(1, num_bars+1)
    plt.barh(positions, data, align='center')

    # Set the label of each bar
    plt.yticks(positions, labels)
    plt.xlabel('Amount in USD')
    plt.title('Weekly Expenses')
    
    # Turns on grid which will assist in visualization of graph

    plt.grid()
    plt.show()

if __name__ == '__main__':
    expenses = []
    categories = []

    try:
        count = float(input('Enter the number of categories: '))
        while count > 0:
            cat = input("\nEnter category: ")
            exp = float(input("Expenditure: "))
            expenses.append(exp)
            categories.append(cat)
            count -=1

    except ValueError:
        print("Invalid input.")

    draw_bar(expenses, categories)
