import numpy as np
import pandas as pd
from alloy2D import alloy2D
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from scipy.interpolate import make_interp_spline, BSpline


#######################################################################################
#                                  GLOBAL VALUES                                      #
#######################################################################################
cellA = 0       # Matrix atom
cellB = 1       # Alloy atom

# Globle setting for the figure drawing
figure(figsize=(7, 6), dpi=300)

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
    size = 30                                      
    nEquil = 100000
    nSweeps = 150000
    fAlloy_list = [0.1, 0.2, 0.3, 0.4, 0.5]
    T_downlim = 300
    T_uplim = 5300
    T_interval = 100
    Eam_list = [-0.1, 0.0, 0.1]
    step_interval = 10

    nT = int((T_uplim - T_downlim)/ T_interval) + 1
    T_list = np.linspace(T_downlim, T_uplim, nT)

    
    # Open file to save the statistics
    file = open ("stats.csv", "w")
    file.write('Job number, Alloy fraction, Temperature (K), Unlike bond energy (eV), Average number of unlike neighbours, Average energy (eV), Heat capacity (kB)\n')
    
    # Loop over values
    for fAlloy in fAlloy_list:

        for Eam in Eam_list:
            orders = list()
            E_assemble = list()

            for T in T_list:
                job = '{}f_{}eV_{:4.2f}K'.format(fAlloy, Eam, T)
                
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
                nBar, Ebar, C, Etable = alloy2D(size, fAlloy, nSweeps, nEquil, T, Eam, job)
                E_assemble.append(Etable)
                
                # For plotting
                orders.append(nBar)

                # Write out the statistics
                file.write('{0}, {1:6.4f}, {2:8.2f}, {3:5.2f}, {4:6.4f}, {5:14.7g}, {6:14.7g}\n'.format(job, fAlloy, T, Eam, nBar, Ebar, C))


            # Find the phase transition temperature for the alloy with the given fraction and bond energy
            name = '{0}_{1}'.format(fAlloy, Eam)
            plt.figure(1)

            # Smooth the curve to ease the inspection of the temperature
            Tnew = np.linspace(T_list.min(), T_list.max(), 5001)
            spl = make_interp_spline(T_list, orders, k=3)     # k=3 default as the cubic interpolate
            power_smooth = spl(Tnew)
            plt.plot(Tnew, power_smooth)
            plt.title("Smoothed curve of temperature aganist to the order parameter")
            plt.xlabel("Temperature (K)")
            plt.ylabel("Order parameter (unit)")
            plt.savefig(r'E:\Coding\alloy_phase_transition\T_order\{}---T_order.png'.format(name))
            plt.close(1)

            # Plot several energy curve under different temperature for general trends
            plt.figure(2)
            for i in range(0, len(E_assemble), 15):
                plt.plot(E_assemble[i][0:int(nSweeps/step_interval)], label='{:.2f}K'.format(300 + T_interval*i))

               
            plt.legend()
            plt.title ("Energy change following the number of steps under several temperature")
            plt.xlabel("Time step / 10")
            plt.ylabel("Energy (eV)")
            plt.savefig(r'E:\Coding\alloy_phase_transition\Energy\{}---energy.png'.format(name))
            plt.close(2)


    # Close the file
    file.close()
    
    # Sign off
    print('')
    print ("Simulations completed.")


if __name__ == "__main__":
    main()
