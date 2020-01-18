import numpy as np
import matplotlib.pyplot as plt
from set_up import set_up
from alloy2D import alloy2D
from getNeighbour import *
from order2D import order2D
from orderRandom import orderRandom
from swapInfo import swapInfo

#######################################################################################
def alloy2D(size, fAlloy, nSweeps, nEquil, T, Eam, job):
    """
    Description:
    ALLOY2D Performs Metropolis Monte Carlo of a lattice gas model of an alloy.
    A random alloy is represented as a 2 dimensional lattice gas in which alloying 
    atoms can exchange position with matrix atoms using the Metropolis alogorithm. The 
    purpose is to show how alloys become more random as the temperature increases.

    Input arguments:
    -> size:    The dimension of the matrix                                     int
    -> fAlloy:  The fraction of sites occupied by alloying atoms                float
    -> nSweeps: The total number of Monte Carlo moves                           int
    -> nEquil:  The number of Monte Carlo moves used to equilibrate the system  int
    -> T:       The temperature (K)                                             float 
    -> Eam:     Alloy-matrix interaction energy (eV)                            float
    -> job:     Name or number given to this simulation.                        string
                Useful for creating file names

    Output arguments:
    -> nBar:    The average number of unlike neighbours                         int
    -> Ebar:    The average energy                                              float
    -> C:       The heat capacity                                               float
    """ 
    # Set up the matrix
    config = set_up(cellA, cellB, size, fAlloy)

    # The initial total energy of the matrix
    Eo = 0
    for x in config.shape[0]:

        for y in config.shape[1]:
            neighbours = getNeighbour(size, x, y)   # Four nearest neighbours
            
            for pair in neighbours:
                Eo += int(config[x, y] + config[pair[0], pair[1]] == 1) * Eam

    # Swap the atoms based on the energy change

    # Plot the configuration
    # Put extra zeros around border so pcolor works properly.
    config_plot = np.zeros((size+1, size+1))
    config_plot[0:size, 0:size] = config
    plt.figure(0)
    plt.pcolor(config_plot)
    plt.savefig(job+'-config.png')
    plt.close(0)
    
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