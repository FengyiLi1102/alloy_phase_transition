import numpy as np
import math as m
import matplotlib.pyplot as plt
from scipy.stats import binom


#######################################################################################
# GLOBAL VALUES
#######################################################################################
cellA = 0 # Matrix atom
cellB = 1 # Alloy atom


def orderRandom(Z, f):
    """
    ORDERRANDOM produces a distribtion function of the order parameter for a
    random alloy. The order parameter is just the number of AB bonds around a
    site. The distribution is computed from the binomial distribution.

    Input arguments
    Z The number of neighbouring sites per site
    f The fraction of alloy atoms

    Output arguments
    N List of possible number of neighbours
    P The probability distribution of the order parameter
    """

    # Initialise the probability distribution
    N = np.linspace(0,Z,Z+1)
    P = np.linspace(0,0,Z+1)

    # Run over allowed number of AB bonds around each site and compute the
    # probability distribution
    

    return N, P


def order2D(config):
"""
ORDER2D produces a distribtion function of the order
parameter. The order parameter is just the number of AB bonds
around a site.
Input arguments
config The configuration
Output arguments
N List of possible number of neighbours
P The probability distribution of the order parameter
""" ADD CODE HERE
return N, P
def swapInfo(ixa, iya, dab, nBox, config, Ematrix):
"""
SWAPINFO Returns the position of the neighbour and the energy change following a swap
Input arguments
ixa X coordinate of first atom
iya Y coordinate of first atom
dab Direction of second atom relative to first. There are four
possible directions, so this takes values between 1 and
4. Together with ixa and ixb, this allows the position
of the second atom to be computed. This calculation is
done by getNeighbour
config The configuration of alloy atoms
nBox System size
Ematrix The 2x2 matrix of bond energies
Output arguments
ixb X coordinate of second atom
iyb Y coordinate of second atom
dE Energy change following swap
""" ADD CODE HERE
return ixb, iyb, dE
def getNeighbour (nBox, ix1, iy1, d12):
"""
GETNEIGHBOUR returns the position of a neighbouring atom
Input arguments
nBox The size of the simulation box
ix1 X coordinate of first atom
iy1 Y coordinate of first atom
d12 Direction of second atom relative to first
Output arguments
ix2 X coordinate of second atom
iy2 Y coordinate of second atom
""" ADD CODE HERE
#
# Return the new coordinates
return ix2, iy2

##########################################
# MAIN FUNCTION
##########################################
#
# This invokes the operations in the required order
