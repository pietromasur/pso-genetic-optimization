import math
from typing import List
#Based on function described at https://www.sfu.ca/~ssurjano/levy.html
def levy(values: List):
    """This function calculates the Rastrigin function's value for the given N-dimensional array."""
    # Initialize the function's value
    wi = 1 + (values[0]-1)/4
    wf = 1 + (values[len(values)-1]-1)/4
    return_value = math.sin(math.pi*wi)**2 + ((wf-1)**2)*(1+math.sin(2*math.pi*wf)**2)

    # Calculate the function's value
    for i in range(len(values)):
        if (i!=0 and i!=values[len(values)-1]):
            w = 1 + (values[i]-1)/4
            return_value+=((w-1)**2)*(1+10*math.sin(math.pi*w+1)**2)
    return return_value

#Domain x in [-10, 10]
def get_levy_domain():
    return [-10,10]