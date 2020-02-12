import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from set_up import set_up
from getNeighbour import *
from order2D import order2D
from orderRandom import orderRandom
from swapInfo import swapInfo
from scipy import constants
import gc
import matplotlib.pylab as pylab


# Globle setting for the figure drawing
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (10, 8),
          'axes.labelsize': 20,
          'axes.titlesize':20,
          'xtick.labelsize':'x-large',
          'ytick.labelsize':'x-large',
          'patch.edgecolor': 'white'}
pylab.rcParams.update(params)

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
    -> T_list:  Temperature list                                                list

    Output arguments:
    -> nBar:    The average number of unlike neighbours                         int
    -> Ebar:    The average energy                                              float
    -> C:       The heat capacity                                               float
    -> Etable:  Energy to move steps under a fixed temperature                  list
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

    Eo = Eo / 2             # Doubled energy by calculating each bond energy twice
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
        if step >= nEquil and step % step_interval == 0:
            Etable.append(Eo)
    

    # After reaching the equilibrium, run more steps for the 
    # phase transition temperature
    test_steps = 50000      # More steps for finding the transition temperature

    # Randomly generate two arrays for swapping atoms
    positions, directions = generator(test_steps, size)
    nStat = test_steps

    # Run more steps
    for step in np.arange(test_steps):
        ixb, iyb, dE = swapInfo(positions[0][step], positions[1][step], 
                                directions[step], natoms, config,
                                size, Eam, T)
        
        Eo += dE
        Etable.append(Eo)
    
    
    # Choose some states to draw the figure
    # The interval is adjustable for request
    T_figure = T_list[::10]

    if T in T_figure:
        # Plot the configuration
        # Put extra zeros around border so pcolor works properly.
        config_plot = np.zeros((size+1, size+1))
        config_plot[0:size, 0:size] = config
        fig = plt.figure(dpi=300)
        ax = fig.add_subplot(111)
        ax.pcolor(config_plot)
        ax.set_title("Schematic configuration of the alloy")
        ax.set_xlabel("X axis boundary")
        ax.set_ylabel("Y axis boundary")
        fig.savefig(r'E:\Coding\alloy_phase_transition\Config\{}---config.png'.format(job))
        plt.close(fig)
        gc.collect()
        
        diff = nSweeps - nEquil
        # Plot the energy change with fixed fraction and interaction energy under a temperature
        fig = plt.figure(dpi=300)
        ax = fig.add_subplot(111)
        ax.plot(Etable[0: int(diff/step_interval)], linewidth=1.5)
        ax.set_title ("Energy change to the move steps of an alloy")
        ax.set_xlabel("Time step / 10")
        ax.set_ylabel("Energy (eV)")
        ax.ticklabel_format(axis='x', style='sci', scilimits=(0,0))
        ax.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
        ax.xaxis.major.formatter._useMathText = True
        ax.yaxis.major.formatter._useMathText = True
        ax.xaxis.get_offset_text().set_fontsize(15)
        ax.get_xaxis().get_major_formatter().set_useOffset(True)
        ax.yaxis.get_offset_text().set_fontsize(15)
        ax.get_yaxis().get_major_formatter().set_useOffset(True)
        fig.savefig(r'E:\Coding\alloy_phase_transition\Energy\{}---energy.png'.format(job))
        plt.close(fig)
        gc.collect()

        # Plot the final neighbour distribution
        N, P = order2D(config)
        N0, P0 = orderRandom(4, fAlloy)
        fig = plt.figure(dpi=300)
        ax = fig.add_subplot(111)
        bar_width = 0.35
        ax.bar(N, P, bar_width, label="Simulation")
        ax.bar(N0+bar_width, P0, bar_width, label="Random")
        ax.set_title ("Distribution of unlike neighbours")
        ax.set_xlabel("Number of unlike neighbours")
        ax.set_ylabel("Probability")
        ax.legend(loc=0)
        fig.savefig(r'E:\Coding\alloy_phase_transition\order\{}-order.png'.format(job))
        plt.close(fig)
        gc.collect()
    

    # Average order parameter
    N, P = order2D(config)
    nBar = np.dot(N, P)

    # Average energy for each atom
    Etable = np.asarray(Etable)
    E_unit_bar_square = ((sum(Etable[-nStat:]) / nStat)**2)

    # Average energy square for each atom
    E2_unit_bar = sum(Etable[-nStat:]**2) / (nStat)

    # Heat capacity for each atom in the unit per K_B
    C = (E2_unit_bar - E_unit_bar_square) / ((k**2) * (T**2))

    print('')
    print('Heat capacity = {0:7.7f}'.format(C),' kB')
    print('The average number of unlike neighbours is = {0:7.3f}'.format(nBar))
    
    # Return the statistics
    return nBar, E_unit_bar_square, C, Etable


def generator(N1, size):
    """
    Description:
    Ramdonly generate two arrays with the chosen atoms and the direction pointing 
    to the second atom.

    Positional arguments:
    -> N1:      limit for the number of atoms required to be swapped  
    -> size:    The scale of the alloy matrix

    Return:
    -> positions:       coordinates of the first atom                  array(2, N1)
    -> directions:      number indicating the second atom              array(N1, 1)
    """
    # Randomly generate the number equal to nSweeps of positions to make swaps
    positions = np.random.randint(0, size, (2, N1), dtype='int')

    # Randomly generate the directions for each swap
    directions = np.random.randint(0, 4, (N1, 1), dtype='int')


    return positions, directions
