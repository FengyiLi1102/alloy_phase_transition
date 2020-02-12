import numpy as np


def getNeighbour (size, x, y):
    """
    Description:
    GETNEIGHBOUR returns the position of a neighbouring atom.

    Input arguments:
    -> size:                  The size of the simulation box                        int
    -> x:                     X coordinate of first atom                            int
    -> y:                     Y coordinate of first atom                            int

    Output arguments:
    -> Array:                 Contains all nearest four neighbours of the atom
    """
    # Get all four nearest neighbours around the chosen atom
    neighbours = np.array([
        [x, y - 1],     # Left
        [x, y + 1],     # Rright
        [x - 1, y],     # Top
        [x + 1, y]      # Bottom
    ])

    # Check whether the coordinates out of the boundary of the matrix
    # If out, change them as the periodic boundary condition
    # Return the new coordinates
    return periodic_boundary(neighbours, size)


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


###############################################################################
################################TEST ONLY######################################
###############################################################################
if __name__ == '__main__':
    size, x, y = 10, 8, 0
    print(getNeighbour(size, x, y))       