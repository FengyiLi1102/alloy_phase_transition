import numpy as np
from getNeighbour import *
#######################################################################################

def swapInfo(ixa, iya, dab, natoms, config, Ematrix, size):
    """
    Description:
    SWAPINFO returns the position of the neighbour and the energy change.

    Positional arguments:
    -> ixa:         X coordinate of first atom                       int
    -> iya:         Y coordinate of first atom                       int
    -> dab:         Direction of second atom relative to first. There are four possible 
                    directions, so this takes values between 1 and 4. Together with ixa 
                    and ixb, this allows the position of the second atom to be computed. 
                    This calculation is done by getNeighbour.
                    1: above; 2: down; 3: right; 4: left             int
    -> config:      The configuration of alloy atoms                 array(size, size)                
    -> natoms:      Number of atoms                                  int
    -> Ematrix:     The 2x2 matrix of bond energies                  array(2, 2)
    -> size:        Dimension of the matrix                          int

    Output arguments:
    -> ixb:         X coordinate of second atom
    -> iyb:         Y coordinate of second atom
    -> dE:          Energy change following swap
    """
    # Get the neighbour position
    ixb, iyb = getNeighbour(size, ixa, iya, dab)


    

    # Calculate the original local energy within a defined matrix
    Eo = 0

    Eo = int(config[ixa][iya] + config[ixb][iyb] == 1) * 
    E0 += int()

    # Atom a:


    

    return ixb, iyb, dE


def allNeighbours(x, y):
    """

    """
    # Array of neighbour coordinates
    neighbours = np.array([
        [x - 1, y],
        [x + 1, y],
        [x, y + 1],
        [x, y - 1]
    ])
    