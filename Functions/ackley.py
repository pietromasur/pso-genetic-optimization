from typing import List
import math


def ackley(values: List(int)):
    """This function calculates the Ackley function's value for the given N-dimensional array."""
    # Initialize the function's value
    value = 0
    # Calculate the function's value
    for i, _ in enumerate(values):
        value += values[i]**2
    value = -20*(math.exp(-0.2*math.sqrt(value/len(values)))) - math.exp(1) - 20 + math.e
    return value


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from numpy import arrange
    from pylab import meshgrid, cm, imshow, title, show
    from mpl_toolkits.mplot3d import Axes3D
    
    x = arrange(-3.0, 3.0, 0.1)
    y = arrange(-3.0, 3.0, 0.1)
    
    X, Y = meshgrid(x, y)
    Z = 
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    
    fig.colorbar(surf, shrink=0.5, aspect=5)
    
    plt.show()