import numpy as np
import pandas as pd
from alloy2D import alloy2D
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib.pylab as pylab
import seaborn as sns
import gc


#######################################################################################
#                                  GLOBAL VALUES                                      #
#######################################################################################
cellA = 0       # Matrix atom
cellB = 1       # Alloy atom

# Globle setting for the figure drawing
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (10, 8),
          'axes.labelsize': 20,
          'axes.titlesize': 20,
          'xtick.labelsize':'x-large',
          'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)


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
    -> Eam_List:          Interact on energy between alloy and host atoms

    Return:

    """
    # Define the simulation parameters
    size = 40                                
    nEquil = 2000000
    nSweeps = 3000000
    fAlloy_list = [0.5, 0.4, 0.3, 0.2, 0.1]
    T_downlim = 300
    T_uplim = 5300
    T_interval = 100
    Eam_list = [-0.1, 0.1]
    step_interval = 10

    nT = int((T_uplim - T_downlim)/ T_interval) + 1
    T_list = np.linspace(T_downlim, T_uplim, nT)

    
    # Open file to save the statistics
    file = open("stats.csv", "w")
    file.write('Job number, Alloy fraction, Temperature (K), Unlike bond energy (eV), Average number of unlike neighbours, Average energy (eV), Heat capacity (kB)\n')
    
    # Loop over values
    for fAlloy in fAlloy_list:

        for Eam in Eam_list:
            orders = list()
            C_list= list()
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
                nBar, Ebar, C, Etable = alloy2D(size, fAlloy, nSweeps, nEquil, T, Eam, job, T_list)
                E_assemble.append(Etable)
                C_list.append(C)
                
                # For plotting
                orders.append(nBar)

                # Write out the statistics
                file.write('{0}, {1:6.4f}, {2:8.2f}, {3:5.2f}, {4:6.4f}, {5:14.7g}, {6:14.7g}\n'.format(job, fAlloy, T, Eam, nBar, Ebar, C))


            # Find the phase transition temperature for the alloy with the given fraction and bond energy
            name = '{0}_{1}'.format(fAlloy, Eam)

            fig = plt.figure(dpi=300)
            ax = fig.add_subplot(111)
            ax.scatter(T_list, C_list)
            ax.set_title("Effect of temperature change to\n the heat capacity per atom")
            ax.set_xlabel("Temperature (K)")
            ax.set_ylabel("Heat capacity (/k_B)")
            ax.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
            ax.yaxis.major.formatter._useMathText = True
            ax.yaxis.get_offset_text().set_fontsize(15)
            ax.get_yaxis().get_major_formatter().set_useOffset(True)
            fig.savefig(r'E:\Coding\alloy_phase_transition\C\{}---T_C.png'.format(name))
            plt.close(fig)
            gc.collect()

            fig = plt.figure(dpi=300)
            ax = fig.add_subplot(111)
            ax.scatter(T_list, orders)
            ax.set_title("Variation of the average order parameter against to the temperature")
            ax.set_xlabel("Temperature (K)")
            ax.set_ylabel("Order parameter (unit)")
            fig.savefig(r'E:\Coding\alloy_phase_transition\T_order\{}---T_order.png'.format(name))
            plt.close(fig)
            gc.collect()

            # Plot several energy curve under different temperature for general trends
            fig = plt.figure(dpi=300)
            ax = fig.add_subplot(111)
            diff = nSweeps - nEquil
            for i in range(0, len(E_assemble), 10):
                ax.plot(E_assemble[i][0:int(diff/step_interval)], label='{:.2f}K'.format(300 + T_interval*i), linewidth=1.5)

               
            ax.legend(loc=0) 
            ax.set_title ("Energy change under different temperatures")
            ax.set_xlabel("Time step / 10")
            ax.set_ylabel("Energy (eV)")
            ax.ticklabel_format(axis='x', style='sci', scilimits=(0,0))
            ax.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
            ax.xaxis.get_offset_text().set_fontsize(15)
            ax.yaxis.get_offset_text().set_fontsize(15)
            ax.xaxis.major.formatter._useMathText = True
            ax.yaxis.major.formatter._useMathText = True
            ax.get_xaxis().get_major_formatter().set_useOffset(True)
            ax.get_yaxis().get_major_formatter().set_useOffset(True)
            fig.savefig(r'E:\Coding\alloy_phase_transition\Energy\{}---energy.png'.format(name))
            plt.close(fig)
            gc.collect()

            # Plot C and n on the same figure for convenience
            fig, ax1 = plt.subplots()

            # Plot C
            color = 'tab:red'
            ax1.set_xlabel('Temperature (K)')
            ax1.set_ylabel('Heat capacity (k_B)')
            ax1.scatter(T_list, C_list, color=color, marker='*')

            ax2 = ax1.twinx()  # For plotting n

            color = 'tab:blue'
            ax2.set_ylabel('Average order parameter')  # we already handled the x-label with ax1
            ax2.scatter(T_list, orders, color=color, marker='x')

            fig.tight_layout()  # otherwise the right y-label is slightly clipped
            fig.savefig(r'E:\Coding\alloy_phase_transition\Order_C\{}_{}---Order_C.png'.format(fAlloy, Eam))
            plt.close(fig)
            gc.collect()


            


    # Close the file
    file.close()
    
    # Sign off
    print('')
    print ("Simulations completed.")


if __name__ == "__main__":
    main()
