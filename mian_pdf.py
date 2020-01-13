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
def alloy2D(nBox, fAlloy, nSweeps, nEquil, T, Eam, job):
"""
ALLOY2D Performs Metropolis Monte Carlo of a lattice gas model of an alloy
A random alloy is represented as a 2 dimensional lattice gas in which
alloying atoms can exchange position with matrix atoms using the
Metropolis alogorithm. The purpose is to show how alloys become more
random as the temperature increases.
Input arguments
nBox The size of the 2-D grid
fAlloy The fraction of sites occupied by alloying atoms
nSweeps The total number of Monte Carlo moves
nEquil The number of Monte Carlo moves used to equilibrate the system
T The temperature (K)
Eam Alloy-matrix interaction energy (eV)
job Name or number given to this simulation. Useful for creating file names
Output arguments
nBar The average number of unlike neighbours
Ebar The average energy
C The heat capacity
""" ADD CODE HERE
#
# Plot the configuration
# Put extra zeros around border so pcolor works properly.
config_plot = np.zeros((nBox+1, nBox+1))
config_plot[0:nBox, 0:nBox] = config
plt.figure(0)
plt.pcolor(config_plot)
plt.savefig(job+'-config.png')
plt.close(0)
#
# Plot the energy
plt.figure(1)
plt.plot (Etable[0:nTable+1])
plt.title ("Energy")
plt.xlabel("Time step / 1000")
plt.ylabel("Energy")
plt.savefig(job+'-energy.png')
plt.close(1)
#
# Plot the final neighbour distribution
N, P = order2D(config)
N0, P0 = orderRandom(4, fAlloy)
plt.figure(2)
bar_width = 0.35
plt.bar(N , P, bar_width, label="Simulation")
plt.bar(N0+bar_width, P0, bar_width, label="Random")
plt.title ("Distribution of unlike neighbours")
plt.xlabel("Number of unlike neighbours")
plt.ylabel("Probability")
plt.legend()
plt.savefig(job+'-order.png')
plt.close(2)
#
# Display the plots (GUI only)
# plt.show()
#
# Print statistics
nBar = np.dot(N,P)
Ebar = Ebar/nStats
E2bar = E2bar/nStats
C = (E2bar - Ebar*Ebar)/(kT*kT)
print('')
print('Heat capacity = {0:7.3f}'.format(C),' kB')
print('The average number of unlike neighbours is = {0:7.3f}'.format(nBar))
#
# Return the statistics
return nBar, Ebar, C
##########################################
# MAIN FUNCTION
##########################################
#
# This invokes the operations in the required order
