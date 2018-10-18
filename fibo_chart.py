'''
Plots graph of consecutive Fibonacci numbers' ratios
'''
import matplotlib.pyplot as plt

def fibo(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    # n > 2

    a = 1
    b = 1
    # First two members of the series
    series = [a, b]
    for i in range(n):
        c = a + b
        series.append(c)
        a = b
        b = c
        
    return series

def draw_fibo(n):
    fibos = fibo(n)
    ratios = []
    for i in range(1, n):
        ratios.append(fibos[i]/fibos[i-1])

    plt.plot(range(1, n), ratios, '-')
    plt.xlabel('No.')
    plt.ylabel('Ratio')
    plt.title('Ratio between Consecutive Fibonacci numbers')
    plt.show()

if __name__ == '__main__':
    n = int(input("How many Fibonacci numbers should we count to? "))
    draw_fibo(n)
            
