import math
from typing import List
#Based on function described at https://www.sfu.ca/~ssurjano/rosen.html
#Domain x in [-2.048, 2.048]
def rosenbrock(values: List):
    """This function calculates the Rastrigin function's value for the given N-dimensional array."""
    # Initialize the function's value
    value = 0 
    # Calculate the function's value
    for i in range(len(values)):
        if i!=len(values)-1:
            value+=(100*(values[i+1]-values[i]**2)**2 + (values[i]-1)**2)
    return value
