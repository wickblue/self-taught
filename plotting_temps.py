'''
Plots temperature at different times of day in San Francisco
'''

from matplotlib import pyplot as plt
import math

def plot_temps():

    time_of_day = ['5 AM', '8 AM', '11 AM', '2 PM',
                   '5 PM', '8 PM', '11 PM', '2 AM']
    sf_temps = [58, 57, 64, 72, 67, 61, 61, 62]
    ny_temps = [56, 59, 61, 65, 68, 56, 54, 55]
    time_interval = range(1, len(time_of_day) + 1)

    plt.plot(time_interval, sf_temps, 'o-')
    plt.plot(time_interval, ny_temps, 'o-')
    plt.xticks(time_interval, time_of_day)
    plt.title('Temperature in SF vs. NYC')
    plt.legend(['SF', 'NYC'])
    plt.show()

if __name__ == '__main__':
    plot_temps()

    
        
