import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from set_up import set_up
from getNeighbour import *
from order2D import order2D
from orderRandom import orderRandom
from swapInfo import swapInfo
from scipy import constants


# Globle setting for the figure drawing
figure(figsize=(7, 6), dpi=300)

# Globle variables
cellA = 0
cellB = 1
k = constants.value(u'Boltzmann constant in eV/K')

#######################################################################################
def alloy2D(size, fAlloy, nSweeps, nEquil, T, Eam, job, T_list):
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

    Eo = 0                  # The initial total energy of the matrix
    step = 0                # The initial step for energy record
    Etable = []             # Record the energy per 1000 step
    natoms = size**2        # Number of total atoms
    step_interval = 10

    # Calculate the initial energy
    for x in np.arange(config.shape[0]):

        for y in np.arange(config.shape[1]):
            neighbours = getNeighbour(size, x, y)   # Four nearest neighbours
            
            for pair in neighbours:
                Eo += int(config[x, y] + config[pair[0], pair[1]] == 1) * Eam

    Eo = Eo / 2
    Etable.append(Eo)       # Initial energy

    # Randomly generate the number equal to nSweeps of positions to make swaps
    positions, directions = generator(nSweeps, size)

    # Swap the atoms based on the energy change
    for step in np.arange(nSweeps):
        ixb, iyb, dE = swapInfo(positions[0][step], positions[1][step], 
                                directions[step], natoms, config,
                                size, Eam, T)
        
        # Eneregy change
        Eo += dE

        # Record the data per 1000 step
        #if step >= nEquil and step % step_interval == 0:
        Etable.append(Eo)
    

    # After reaching the equilibrium, run more steps for the 
    # phase transition temperature
    test_steps = 50000      # More steps for finding the transition temperature

    # Randomly generate two arrays for swapping atoms
    positions, directions = generator(test_steps, size)
    nStat = test_steps / step_interval

    # Run more steps
    for step in np.arange(test_steps):
        ixb, iyb, dE = swapInfo(positions[0][step], positions[1][step], 
                                directions[step], natoms, config,
                                size, Eam, T)
        
        Eo += dE

        if step % step_interval == 0:
            Etable.append(Eo)
    
    
    # Choose some states to draw the figure
    T_figure = T_list[::10]

    if T in T_figure:
        # Plot the configuration
        # Put extra zeros around border so pcolor works properly.
        config_plot = np.zeros((size+1, size+1))
        config_plot[0:size, 0:size] = config
        plt.figure(0)
        plt.pcolor(config_plot)
        plt.title("Schematic configuration of the alloy")
        plt.xlabel("X_axis boundary")
        plt.ylabel("Y_axis boundary")
        plt.savefig(r'E:\Coding\alloy_phase_transition\Config\{}---config.png'.format(job))
        plt.close(0)
        
        # Plot the energy
        plt.figure(1)
        plt.plot (Etable[0: int(nSweeps/step_interval)])
        plt.title ("Energy change to the move steps of an alloy")
        plt.xlabel("Time step / 10")
        plt.ylabel("Energy (eV)")
        plt.savefig(r'E:\Coding\alloy_phase_transition\Energy\{}---energy.png'.format(job))
        plt.close(1)

        # Plot the final neighbour distribution
        N, P = order2D(config)
        N0, P0 = orderRandom(4, fAlloy)
        plt.figure(2)
        bar_width = 0.35
        plt.bar(N, P, bar_width, label="Simulation")
        plt.bar(N0+bar_width, P0, bar_width, label="Random")
        plt.title ("Distribution of unlike neighbours")
        plt.xlabel("Number of unlike neighbours")
        plt.ylabel("Probability")
        plt.legend()
        plt.savefig(r'E:\Coding\alloy_phase_transition\order\{}-order.png'.format(job))
        plt.close(2)
    
    # Display the plots (GUI only)
    # plt.show()
    N, P = order2D(config)
    # Print statistics
    nBar = np.dot(N, P)

    # Ebar
    E_total_bar = sum(Etable[int(nSweeps/step_interval)+1:]) / nStat
    E_unit_bar = E_total_bar / natoms

    # E2bar
    Etable = np.asarray(Etable)
    E2_total_bar = sum((Etable[int(nSweeps/step_interval)+1:])**2) / nStat
    E2_unit_bar = E2_total_bar / natoms

    C = (E2_unit_bar - E_unit_bar**2) / ((k**2) * (T**2))
    print('')
    print('Heat capacity = {0:7.3f}'.format(C),' kB')
    print('The average number of unlike neighbours is = {0:7.3f}'.format(nBar))
    
    # Return the statistics
    return nBar, E_total_bar, C, Etable


def generator(N1, size):
    """
    Description:
    Ramdonly generate two arrays with the chosen atoms and the direction pointing 
    to the second atom.

    Positional arguments:
    -> N1:      limit for the number of atoms required to be swapped  

    Keyward arguments:
    -> N2:      limit for the number of steps required to equilibrate the matrix

    Return:
    -> positions:       coordinates of the first atom                  array(2, N1)
    -> directions:      number indicating the second atom              array(N2, 1)
    """
    # Randomly generate the number equal to nSweeps of positions to make swaps
    positions = np.random.randint(0, size, (2, N1), dtype='int')

    # Randomly generate the directions for each swap
    directions = np.random.randint(0, 4, (N1, 1), dtype='int')


    return positions, directions
