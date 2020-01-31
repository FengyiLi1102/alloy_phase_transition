import numpy as np
#######################################################################################


def findTT():
    """
    
    """
    #
    derivates = abs((orders[1:] - orders[:-1])) / (T_list[1:] - T_list[:-1])

    param = 0.8
    threshold = param * derivates.max()

    Xs = [i if derivates[i] >= threshold else pass for i in len(derivates)]
    


    if 