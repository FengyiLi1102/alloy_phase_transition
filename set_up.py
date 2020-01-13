import numpy as np
#######################################################################################

def set_up(cellA, cellB, side, fraction):
    """
    Description:
    SET_UP initiates the simulation environment which is the alloy matrix.

    Positional arguments:
    -> cellA:       Host atom (1)                       int8
    -> cellB:       Alloy atom (2)                      int8     
    -> side:        Length of the matrix                int8
    -> fraction:    Composition of the alloy atom       float

    Return:
    -> Matrix:      Alloy matrix                        array(side, side)
    """
    # Initiates the alloy matrix
    natoms = int(side**2)
    nB = int(fraction * (natoms))
    nA = int(natoms - nB)

    # Concatenate host atoms and alloy atoms, and shuffle the positions
    matrix = np.concatenate((np.zeros((1, nA)), np.ones((1, nB))), axis=None)
    np.random.shuffle(matrix)
    
    return np.reshape(matrix, (side, side))

print(set_up(0, 1, 10, 0.1))
