import numpy as np


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
    np.random.shuffle(matrix)
    
    return np.reshape(matrix, (size, size))