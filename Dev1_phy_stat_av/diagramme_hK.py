import numpy as np
import scipy as sp
import time
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

def h_prime(h, k):
    return h +(1/2)*np.log(np.cosh(2*k+h)/np.cosh(-2*k +h))

def k_prime(h, k):
    return (1/4)*(np.log(np.cosh(2*k+h))+np.log(np.cosh(-2*k+h)) - np.log((np.cosh(h)*np.cosh(h))))


if __name__ == '__main__':

    h = 200
    k = np.linspace(0, 1000)
    k = np.arange(0, 1000)
    i = 0
    x = 200

    #for h in np.linspace(0,10, 20):
    #    hinit = h
    #    for x  in np.arange(1,10):
    #        h = hinit

    #        i = 0
    #        while i < 100:
    #            x_prim = k_prime(h, x)
    #            b_prim = h_prime(h , x)
    #            print(x_prim, b_prim)


    #            #plt.plot([x , x_prim], [x_prim, x_prim], 'b')
    #            #plt.plot([x_prim, x_prim],[x_prim, k_prime(h, x_prim)], 'b')
    #            #plt.plot([h, b_prim], [x, x_prim])

    #            plt.quiver([h],[x],[( b_prim - h)], [( x_prim- x)], angles='xy', scale_units='xy', scale=1, width=0.005 )

    #            x = x_prim
    #            h = b_prim
    #            if abs(x) < 0.0001 :
    #                break
    #            i += 1

    #plt.xlim(0, 20)
    ##plt.ylim(0, 10)
    #plt.show()

    hvalues = np.linspace(0, 3, 15)
    kvalues = np.linspace(0, 2, 10)
    for h in hvalues:
        for k in kvalues:
            k_prim = k_prime(h, k)
            h_prim = h_prime(h, k)

            plt.quiver([h], [k], [(h_prim - h)], [(k_prim - k)], angles='xy', scale_units='xy', scale=3.5, width=0.005)
            #plt.quiver([h], [k], [(h_prim - h)], [(k_prim - k)], units = 'width')

    plt.xlim(0, 2)
    # plt.ylim(0, 10)
    plt.show()
