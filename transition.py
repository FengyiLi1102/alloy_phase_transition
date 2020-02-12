import matplotlib.pylab as plb
import matplotlib.pyplot as plt
import numpy as np
import gc
import pandas as pd

params = {
    'legend.fontsize': 'x-large',
    'figure.figsize': (10, 8),
    'axes.labelsize': 18,
    'axes.titlesize': 'x-large',
    'xtick.labelsize': 'x-large',
    'ytick.labelsize': 'x-large',
}
plb.rcParams.update(params)


def main():

    # size = 100; J = 0.1
    T_list_01 = [1230, 1250, 1400, 1480, 1500]

    # J = -0.1
    T_list_n01 = [550, 750, 950, 1150, 1250]

    # Fraction
    f_list = np.linspace(0.1, 0.5, 5)

    fig = plt.figure(dpi=300)
    ax1 = fig.add_subplot(121)
    ax1.plot(f_list, np.poly1d(np.polyfit(f_list, T_list_01, 1))(f_list), 'r', label='J = 0.1 eV')
    ax1.scatter(f_list, T_list_01, c='r', marker='*')
    fig.suptitle('Alloy fraction', y=0.05, fontsize=18)
    ax1.set_ylabel('Transition temperature (K)')
    ax2 = fig.add_subplot(122)
    ax2.plot(f_list, np.poly1d(np.polyfit(f_list, T_list_n01, 1))(f_list), label='J = -0.1 eV')
    ax2.scatter(f_list, T_list_n01, c='b', marker='x')
    fig.legend(loc=0)
    fig.savefig('xxxxx.png')
    plt.close(fig)
    gc.collect()


def draw():
    myfile = pd.read_csv(r'E:\Coding\Data_100_4000\stats.csv')
    

if __name__ == '__main__':
    main()