'''
Graphs a particular quadratic equation for multiple values of x
'''
import matplotlib.pyplot as plt

x_values = []
y_values = []

for i in range(-5, 6):
    x_values.append(i)

for x in x_values:
    y = x**2 + 2*x + 1
    y_values.append(y)

def quad_graph():
    plt.plot(x_values, y_values, 'o-')
    plt.show()

if __name__ == '__main__':
    quad_graph()
    
