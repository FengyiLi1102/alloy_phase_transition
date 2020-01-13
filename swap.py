import numpy as np
#######################################################################################

def swapInfo(ixa, iya, dab, natoms, config, Ematrix):
    """
    Description:
    SWAPINFO returns the position of the neighbour and the energy change.

    Positional arguments:
    -> ixa:         X coordinate of first atom                          int
    -> iya:         Y coordinate of first atom                          int
    -> dab:         Direction of second atom relative to first. There are four possible 
                    directions, so this takes values between 1 and 4. Together with ixa 
                    and ixb, this allows the position of the second atom to be computed. 
                    This calculation is done by getNeighbour.           int
    -> config:      The configuration of alloy atoms                    
    -> natoms:      System size                                         int
    -> Ematrix:     The 2x2 matrix of bond energies                     array(2, 2)

    Output arguments:
    -> ixb:         X coordinate of second atom
    -> iyb:         Y coordinate of second atom
    -> dE:          Energy change following swap
    """
    #
    

    return ixb, iyb, dE