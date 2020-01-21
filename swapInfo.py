import numpy as np
from scipy import constants
from getNeighbour import *
#######################################################################################

k_B = constants.value(u'Boltzmann constant in eV/K')

def swapInfo(ixa, iya, dab, natoms, config, size, Eam, T):
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
                    0: Left; 1: Right; 2: Top; 3: Bottom             int
    -> config:      The configuration of alloy atoms                 array(size, size)                
    -> natoms:      Number of atoms                                  int
    -> Ematrix:     The 2x2 matrix of bond energies                  array(2, 2)
    -> size:        Dimension of the matrix                          int
    -> T:           Temperature in Klevin                            float

    Output arguments:
    -> ixb:         X coordinate of second atom
    -> iyb:         Y coordinate of second atom
    -> dE:          Energy change following swap
    """
    # Get the neighbour position for atom a
    neighbours_a = getNeighbour(size, ixa, iya)
    ixb, iyb = neighbours_a[dab[0]][0], neighbours_a[dab[0]][1]

    # Get all neighbours of the ataom a except atom b
    mask_a = mask(neighbours_a, ixb, iyb)
    neighbours_a_masked = np.extract(mask_a, neighbours_a).reshape(3, 2)

    # Get all neighbours of the ataom b except atom a
    neighbours_b = getNeighbour(size, ixb, iyb)
    mask_b = mask(neighbours_b, ixa, iya)
    neighbours_b_masked = np.extract(mask_b, neighbours_b).reshape(3, 2)
    
    # Initialize the original energy
    dE = 0

    # Calculate the original local energy within a defined matrix
    for pair in neighbours_a_masked:
        dE += int(config[ixa][iya] + config[pair[0]][pair[1]] == 1) * Eam
        dE -= int(config[ixb][iyb] + config[pair[0]][pair[1]] == 1) * Eam
    
    for pair in neighbours_b_masked:
        dE += int(config[ixb][iyb] + config[pair[0]][pair[1]] == 1) * Eam
        dE -= int(config[ixa][iya] + config[pair[0]][pair[1]] == 1) * Eam
    
    # Ckech if the energy decreases
    if dE > 0 and np.exp(dE / (k_B * T)) < np.random.random(1):     # Invalid
        pass

    else:          # Valid
        config[ixa][iya], config[ixb][iyb] = config[ixb][iyb], config[ixa][iya]


    return ixb, iyb, dE


def mask(neighbour, x, y):
    """

    """
    #
    mask = (neighbour[:, 0] != x) | (neighbour[:, 1] != y)
    mask = mask.reshape(4, 1)

    return np.hstack([mask, mask])