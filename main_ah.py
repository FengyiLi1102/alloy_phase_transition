import numpy as np
import math as m
import matplotlib.pyplot as plt
from scipy.stats import binom


#######################################################################################
# GLOBAL VALUES
#######################################################################################
cellA = 0 # Matrix atom
cellB = 1 # Alloy atom






def swapInfo(ixa, iya, dab, nBox, config, Ematrix):
"""
SWAPINFO Returns the position of the neighbour and the energy change following a swap
Input arguments
ixa X coordinate of first atom
iya Y coordinate of first atom
dab Direction of second atom relative to first. There are four
possible directions, so this takes values between 1 and
4. Together with ixa and ixb, this allows the position
of the second atom to be computed. This calculation is
done by getNeighbour
config The configuration of alloy atoms
nBox System size
Ematrix The 2x2 matrix of bond energies
Output arguments
ixb X coordinate of second atom
iyb Y coordinate of second atom
dE Energy change following swap
""" ADD CODE HERE
return ixb, iyb, dE

##########################################
# MAIN FUNCTION
##########################################
#
# This invokes the operations in the required order
