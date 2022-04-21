from typing import List
import math

#Based on function described at https://www.sfu.ca/~ssurjano/ackley.html
#Domain x in [-32.768, 32.768]
def ackley(values: List):
    """This function calculates the Ackley function's value for the given N-dimensional array."""
    # Initialize the function's value and constants
    a = 20
    b = 0.2
    c = 2*math.pi
    return_value = 0
    # Calculate the function's value
    b_exp_value = 0 
    c_exp_value = 0 
    for i, _ in enumerate(values):
        b_exp_value += values[i]**2
        c_exp_value += math.cos(c*values[i])
    return_value = -a*(math.exp(-b*math.sqrt(b_exp_value/len(values)))) - math.exp(c_exp_value/len(values)) + a + math.exp(1)
    return return_value