import numpy as np
import pandas as pd
from alloy2D import alloy2D


#######################################################################################
#                                  GLOBAL VALUES                                      #
#######################################################################################
cellA = 0       # Matrix atom
cellB = 1       # Alloy atom


def main():
    """
    Description:
    Main function to simulate the phase transition of the alloy with several parameters.

    Positional arguments:
    -> natoms:            Total number of total atoms
    -> nEquil:            Total number of Monte Carlo moves to reach the equilibrium
    -> nSweeps:           Total number of Monte Carlo moves
    -> fAlly_list:        Compositions of alloy atoms in the matrix
    -> T_list:            Temperature lists
    -> Eam_List:          Interacton energy between alloy and host atoms

    Return:

    """
    # Define the simulation parameters
    size = 10                                       
    nEquil = 50000
    nSweeps = 100000
    fAlloy_list = [0.1, 0.2, 0.3, 0.4, 0.5]
    T_list = [300, 1000, 2000]
    Eam_list = [-0.1, 0.0, 0.1]
    
    # Open file to save the statistics
    file = open ("stats.csv", "w")
    file.write('Job number, Alloy fraction, Temperature (K), Unlike bond energy (eV), Average number of unlike neighbours, Average energy (eV), Heat capacity (kB)\n')
    
    # Loop over values
    count = 0
    for fAlloy in fAlloy_list:

        for Eam in Eam_list:
            orders = list()

            for T in T_list:
                count = count + 1
                job = '{:04d}'.format(count)
                
                # Echo the parameters back to the user
                print ("")
                print ("Simulation ", job)
                print ("----------------")
                print ("Cell size = ", size)
                print ("Alloy fraction = ", fAlloy)
                print ("Total number of moves = ", nSweeps)
                print ("Number of equilibration moves = ", nEquil)
                print ("Temperature = ", T, "K")
                print ("Bond energy = ", Eam, "eV")
                
                # Run the simulation
                nBar, Ebar, C, ORDERbar = alloy2D(size, fAlloy, nSweeps, nEquil, T, Eam, job)
                
                #
                orders.append(ORDERbar)

                # Write out the statistics
                file.write('{0:4d}, {1:6.4f}, {2:8.2f}, {3:5.2f}, {4:6.4f}, {5:14.7g}, {6:14.7g}\n'.format(count, fAlloy, T, Eam, nBar, Ebar, C))

            # Find the phase transition temperature for the alloy with the given fraction and bond energy


    # Close the file
    file.close()
    
    # Sign off
    print('')
    print ("Simulations completed.")


if __name__ == "__main__":
    main()
