import numpy as np
#######################################################################################
import pandas as pd
import matplotlib.pylab as plb 
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import gc

params = {
    'figure.figsize': (10, 8),
    'axes.labelsize': 20,
    'axes.titlesize': 20,
    'xtick.labelsize': 'x-large',
    'ytick.labelsize': 'x-large',
    'legend.fontsize': 'x-large'
}
plb.rcParams.update(params)


def main():

    data = pd.read_csv('stats.csv')
    
    for i in range(10):
        name = data.iloc[i, 0]
        start = i * 51
        end = start + 51

        nbar = data.iloc[start: end, 6]
        temp = np.linspace(300, 5300, 51)

        nbar_max = nbar.idxmax()

        fig = plt.figure(dpi=300)
        ax1 = fig.add_subplot(111)
        ax1.scatter(temp, nbar, color='tab:red')
        poly1 = np.polyfit(temp[:nbar_max+1], nbar[: nbar_max+1], 2)
        poly_y_1 = np.poly1d(poly1)(temp[:nbar_max+1])
        ax1.plot(temp[:nbar_max+1], poly_y_1, 'r-')
        poly2 = np.polyfit(temp[nbar_max:], nbar[nbar_max:], 2)
        poly_y_2 = np.poly1d(poly2)(temp[nbar_max:])
        ax1.plot(temp[nbar_max:], poly_y_2, 'r-')
        ax1.set_xlabel('Temperature (K)')
        ax1.set_ylabel('Heat capacity (k_B)')

        """ax1.polyfit()

        ax2 = ax1.twinx()"""

        fig.savefig(r'E:\Coding\alloy_phase_transition\Order_C\{}.png'.format(name))
        plt.close(fig)
        gc.collect()


if __name__ == '__main__':
    main()
