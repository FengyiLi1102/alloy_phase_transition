import matplotlib.pylab as plb
import matplotlib.pyplot as plt
import numpy as np
import gc
import pandas as pd
from scipy import constants
import math as ma

k = constants.value(u'Boltzmann constant in eV/K')

params = {
    'legend.fontsize': 'x-large',
    'figure.figsize': (10, 8),
    'axes.labelsize': 20,
    'axes.titlesize': 20,
    'xtick.labelsize': 'x-large',
    'ytick.labelsize': 'x-large',
}
plb.rcParams.update(params)


def main():

    natom = 1600
    s = 4
    U = 0.2

    # J = -0.1
    T_list_n01 = np.array([1100, 1150, 1300, 1250, 1400])
    C_list = np.array([22, 131, 285, 550, 1040]) * k

    # Fraction
    f_list = np.linspace(0.1, 0.5, 5)

    # T_ps
    T_ps = s * U * (1-2*f_list) / 2 / k / np.log((1-f_list)/f_list)
    C = natom * k * (f_list*(1-f_list)*(1-2*f_list)*(np.log((1-f_list)/f_list))**2) / (1-2*f_list-2*(1-f_list)*f_list*np.log((1-f_list)/f_list))
    T = (s*U*(1-2*f_list)) / (2*k*np.log((1-f_list)/f_list))

    fig = plt.figure(dpi=300)
    ax1 = fig.add_subplot(111)
    #ax1.plot(f_list, np.poly1d(np.polyfit(f_list, T_list_n01, 1))(f_list), 'r', label='J = -0.1 eV')
    #ax1.scatter(f_list, T_list_n01, c='r', marker='*', label='Simulation')
    ax1.scatter(f_list, T_ps, c='b', marker='o', label='Theory')
    #ax1.plot(T, C, 'b', label='Literature')
    ax1.scatter(f_list, T_list_n01, c='r', marker='*', label='Simulation')
    #ax1.plot(T_list_n01, np.poly1d(np.polyfit(T_list_n01, C_list, 1))(T_list_n01), 'r', label='Simulation')
    fig.legend(loc=1, bbox_to_anchor=(0.905, 0.88))
    ax1.set_xlabel('Alloy fraction')
    ax1.set_ylabel('Transition temperature (K)')
    fig.savefig('xxxxx.png')
    plt.close(fig)
    gc.collect()
    

if __name__ == '__main__':
    main()