
'''
Draw the trajectory of a body in projectile motion
'''

from matplotlib import pyplot as plt
import math

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')

def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment

    return numbers

def draw_trajectory(u, theta):

    theta = math.radians(theta)
    g = 9.8

    # Time of flight
    t_flight = 2*u*math.sin(theta)/g
    print('Time of flight: {0:.2f} seconds'.format(t_flight))

    # Maximum horizontal distance
    h_max = u*math.cos(theta)*t_flight
    print('Maximum horizontal distance: {0:.2f} meters'.format(h_max))

    # Maximum vertical distance
    v_max = 2*(u*math.sin(theta)*(t_flight/2) - 0.5*g*(t_flight/2)*(t_flight/2))
    print('Maximum vertical distance: {0:.2f} meters'.format(v_max))

    # Find time intervals
    intervals = frange(0, t_flight, 0.001)
    
    # List of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)

    draw_graph(x, y)

if __name__ == '__main__':
    u_list = []
    theta_list = []
    traj_list = []
    try:
        num_trajectories = float(input('How many trajectories? '))
        count = 1
        while num_trajectories > 0: 
            u = float(input('\nEnter the initial velocity for trajectory {0} (m/s): '.format(count)))
            theta = float(input('\nEnter the angle of projection for trajectory {0} (degrees): '.format(count)))
            u_list.append(u)
            theta_list.append(theta)
            traj_list.append("Trajectory {0}".format(count))
            num_trajectories -=1
            count += 1
    except ValueError:
        print('You entered an invalid input')

    for i in range(0, len(u_list)):
        print('\nStatistics for {0}: \n'.format(traj_list[i]))
        draw_trajectory(u_list[i], theta_list[i])

    
    plt.legend(traj_list)
    plt.show()
    
