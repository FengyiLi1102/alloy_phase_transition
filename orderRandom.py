import numpy as np
import math


def orderRandom(Z, f):
    """
    Description:
    ORDERRANDOM produces a distribtion function of the order parameter for a random 
    alloy. The order parameter is just the number of AB bonds around a site. The 
    distribution is computed from the binomial distribution.

    Input arguments:
    -> Z:               The number of neighbouring sites per site
    -> f:               The fraction of alloy atoms

    Output arguments:
    -> N:               List of possible number of neighbours
    -> P:               The probability distribution of the order parameter
    """
    # Initialise the probability distribution
    N = np.linspace(0,Z,Z+1)
    P = np.linspace(0,0,Z+1)

    # Run over allowed number of AB bonds around each site and compute the
    # probability distribution in the form of binomial distribution
    for n in N:
        Z_C_n = math.factorial(Z) / (math.factorial(n) * math.factorial(Z - n))
        P[int(n)] = Z_C_n * (f * (f**(Z-n)) * ((1 - f)**n)
               + (1 - f) * (f**n) * (1 - f)**(Z - n)) 

    return N, P


if __name__ =='__main__':
    print(orderRandom(4, 0.1))