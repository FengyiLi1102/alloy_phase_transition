import numpy as np
#######################################################################################


def getNeighbour (size, ix1, iy1, d12):
    """
    Description:
    GETNEIGHBOUR returns the position of a neighbouring atom.

    Input arguments:
    -> size:                  The size of the simulation box                        int
    -> ix1:                   X coordinate of first atom                            int
    -> iy1:                   Y coordinate of first atom                            int
    -> d12:                   Direction of second atom relative to first
                              1: above; 2: down; 3: left; 4: right                  int

    Output arguments:
    -> ix2:                   X coordinate of second atom                           int
    -> iy2:                   Y coordinate of second atom                           int
    """
    #
    d12 = np.random.randint(1, 5, 1, dtype='int')
    if d12 == 1:
        ix2 = ix1 + 1
        iy2 = iy1

    # Return the new coordinates
    return ix2, iy2


def periodic_check(x, y, size):
    """

    """

    if x > (size - 1):
        x = 0
    
    else x < 0:
        x = size - 1
    
    if y > 

        