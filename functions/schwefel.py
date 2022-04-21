import math
from typing import List
#Based on function described at https://www.sfu.ca/~ssurjano/schwef.html
#Domain x in [-500,+500]
def schwefel(values: List):
    """This function calculates the Rastrigin function's value for the given N-dimensional array."""
    # Initialize the function's value
    value = 418.9829*len(values)
    # Calculate the function's value
    for x in values:
        value-=(x*math.sin(math.sqrt(x)))
    return value