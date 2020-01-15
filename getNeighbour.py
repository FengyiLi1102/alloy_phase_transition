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
                              1: above; 2: down; 3: right; 4: left                  int

    Output arguments:
    -> ix2:                   X coordinate of second atom                           int
    -> iy2:                   Y coordinate of second atom                           int
    """
    # Get its neighbour based on the direction (d12)
    if np.logical_or(d12 == 1, d12 == 2):
        ix2 = ix1 + (-1)**(1 + d12)
        iy2 = iy1

    else:
        ix2 = ix1
        iy2 = iy1 + (-1)**(1 + d12)

    # Check whether the coordinates out of the boundary of the matrix
    # If out, change them as the periodic boundary conditions
    pair = periodic_boundary(ix2, iy2, size)
    ix2, iy2 = pair[0][0], pair[0][1]

    # Return the new coordinates
    return ix2, iy2


def periodic_boundary(arr, size):
    """
    Description:
    Change the position of the atom that runs out of the boundary.

    Positional arguments:
    -> arr:                    Array of coordinates                              array
    -> size:                   Dimension of the matrix                           int

    Return:
    -> x:                      Changed X coordinate                              int
    -> y:                      Changed Y coordinate                              int
    """
    # Check whether the X and Y coordinates out of the matrix dimension
    for pair in arr:
        if pair[0] > (size - 1):      # Larger than the upper bound
            pair[0] = 0               # Change to the lower bound
        
        elif pair[0] < 0:
            pair[0] = size - 1
        
        if pair[1] > (size - 1):
            pair[1] = 0
        
        elif pair[1] < 0:
            pair[1] = size - 1
        

    return arr

        