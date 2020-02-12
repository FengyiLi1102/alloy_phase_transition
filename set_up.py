import numpy as np
import matplotlib.pyplot as plt


def set_up(cellA, cellB, size, fraction):
    """
    Description:
    SET_UP initiates the simulation environment which is the alloy matrix.

    Positional arguments:
    -> cellA:       Host atom (1)                       int8
    -> cellB:       Alloy atom (2)                      int8     
    -> size:        Length of the matrix                int8
    -> fraction:    Composition of the alloy atom       float

    Return:
    -> Matrix:      Alloy matrix                        array(side, side)
    """
    # Initiates the alloy matrix
    natoms = int(size**2)
    nB = int(fraction * (natoms))
    nA = int(natoms - nB)

    # Concatenate host atoms and alloy atoms, and shuffle the positions
    matrix = np.concatenate(
        (np.zeros((1, nA), dtype='int'), np.ones((1, nB), dtype='int')),
        axis=None
    )
    np.random.shuffle(matrix)       # Randomly distribute atoms
    
    
    # Reshape into the required dimension
    return np.reshape(matrix, (size, size))


###############################################################################
################################TEST ONLY######################################
###############################################################################
if __name__ == '__main__':
    size = 10
    fraction = 0.1
    config = set_up(0, 1, size, fraction)
    config_plot = np.zeros((size+1, size+1))
    config_plot[0:size, 0:size] = config
    plt.figure(0)
    plt.pcolor(config_plot)
    plt.title("Schematic configuration of the alloy")
    plt.xlabel("X axis boundary")
    plt.ylabel("Y axis boundary")
    plt.show()
