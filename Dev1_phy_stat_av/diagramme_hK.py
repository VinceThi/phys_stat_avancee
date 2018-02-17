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
    h = np.arange(0,5)
    j = 0
    for h in np.arange(0,20):
        h_init = h
        for x in [5,10]:
            h = h_init
            i = 0
            while i < 100:
                x_prim = k_prime(h, x)
                b_prim = h_prime(h , x)
                print(x_prim, b_prim)
            
                #plt.plot([x , x_prim], [x_prim, x_prim], 'b')
                #plt.plot([x_prim, x_prim],[x_prim, k_prime(h, x_prim)], 'b')
                plt.plot([h, b_prim], [x, x_prim])
            
                x = x_prim
                h = b_prim
                i += 1
    plt.show()
    z = np.linspace(0, 20,1000)
    plt.plot(z, z)
    plt.plot(z, k_prime(0, z))
    plt.show()
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    h = np.linspace(0,10)
    k = np.linspace(0,10)
    h ,k = np.meshgrid(h, k)
    z = k_prime(h,k)
    z2 = k

    surf = ax.plot_surface(h, k, z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    ax.set_zlim(0, 10)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    surf = ax.plot_surface(h, k, z2, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.set_xlabel('h Label')
    ax.set_ylabel('K Label')
    ax.set_zlabel('k_prime Label')

    plt.show()

    plt.plot(k, k_prime(h, k))
    plt.plot(k,k)
    print(k_prime(h,k) - k)
    plt.show()

    ##h = np.linspace(0,1)
    #k = 0.5

    #i = 0
    #x = .5
    #for k in np.arange(0,10):
    #    i = 0
    #    x = 0.0001
    #    while i < 50:
    #        x_prim = h_prime(x, k)
    #        print(x_prim)

    #        #plt.plot([x, x_prim], [x_prim, x_prim], 'b')
    #        #plt.plot([x_prim, x_prim], [x_prim, h_prime(x_prim, k)], 'b')
    #        plt.plot([x, x_prim], [k, k])

    #        x = x_prim
    #        i += 1

    ##plt.plot(h, h_prime(h, k))
    ##plt.plot(h, h)
    #plt.show()