import numpy as np
from getNeighbour import *


def order2D(config):
    """
    Description:
    ORDER2D produces a distribtion function of the order parameter. The order parameter 
    is just the number of AB bonds around a site.

    Input arguments:
    -> config:     The configuration                                  array(size, size)

    Output arguments:
    -> N:          List of possible number of neighbours                    array(1, 4)
    -> P:          The probability distribution of the order parameter      array(1, 4)
    """
    size = config.shape[0]            # Scale of the alloy matrix
    Z = 4                             # Number of the nearest neighbours
    N = np.linspace(0, Z, Z+1)        # List of possible number of neighbours
    P = np.zeros(5)                   # Probability distribution

    # Count the number of each order paramenter
    for x in np.arange(config.shape[0]):

        for y in np.arange(config.shape[1]):            # Pointwise atom from (0, 0)
            count = 0                                   # Number of unlike pairs
            neighbours = getNeighbour(size, x, y)       # Neighbour array

            for pair in neighbours:                     # Count unlike pairs
                if config[x][y] + config[pair[0]][pair[1]] == 1:
                    count += 1
            
            P[count] += 1                               # Update the order parameters
    
    P = P / (size**2)                                   # Probability distribution
    

    return N, P


