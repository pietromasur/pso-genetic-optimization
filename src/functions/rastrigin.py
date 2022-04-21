from typing import List
import math
#Based on function described at https://www.sfu.ca/~ssurjano/rastr.html
def rastrigin(values: List):
    """This function calculates the Rastrigin function's value for the given N-dimensional array."""
    # Initialize the function's value
    value=10*len(values)
    # Calculate the function's value
    for x in values:
        value+=(x**2-10*(math.cos(2*math.pi*x)))
    return value

#Domain x in [-5.12, 5.12]
def get_rastrigin_domain():
    return [-5.12, 5.12]