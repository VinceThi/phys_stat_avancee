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

def inverse(h,kprim):
    return (1/4) * np.arccosh(2*np.cosh(h)*np.cosh(h)*np.exp(4*kprim)-np.cosh(2*h))


if __name__ == '__main__':

    h = 200
    k = np.linspace(0, 1000)
    k = np.arange(0, 1000)
    i = 0
    x = 200
    plt.rc('text', usetex=True)

    print(k_prime(1, 0.574910879829))
    print(k_prime(1, 0))
    print(inverse(1 , 0.153444140922))
    for h in [1]:#np.linspace(0,10, 20):
        hinit = h
        for x  in np.arange(2,3):
            h = hinit

            i = 0
            while i < 100:
                x_prim = k_prime(h, x)
                #b_prim = h_prime(h , x)
                #print(x_prim, b_prim)

                if i == 0 :
                    plt.plot([x , x_prim], [x_prim, x_prim], 'b', label='$Cobweb$')
                else:
                    plt.plot([x, x_prim], [x_prim, x_prim], 'b')
                plt.plot([x_prim, x_prim],[x_prim, k_prime(h, x_prim)], 'b')
                #plt.plot([h, b_prim], [x, x_prim])

                x = x_prim
                #h = b_prim
                if abs(x) < 0.0001 :
                    break
                i += 1
    #plt.xlim(0, 20)
    ##plt.ylim(0, 10)
    z = np.linspace(0, 2, 1000)
    plt.plot(z, z, 'k', label=r'$K^\prime = K$')
    plt.plot(z, k_prime(1, z), 'r', label='$K^\prime = K^\prime(1,K)$')
    plt.legend(loc=0, fontsize=16)
    plt.ylabel('$K^\prime$', fontsize=25)
    plt.xlabel('$K$', fontsize=25)
    plt.xlim(0, 2)
    plt.ylim(0, 2)
    plt.show()


    ########### FLOW DIAGRAM ###############
    hvalues = np.linspace(0, 3, 15)
    kvalues = np.linspace(0, 2, 10)
    for h in hvalues:
        for k in kvalues:
            k_prim = k_prime(h, k)
            h_prim = h_prime(h, k)

            plt.quiver([h], [k], [(h_prim - h)], [(k_prim - k)], angles='xy', scale_units='xy', scale=3.5, width=0.005)
            #plt.quiver([h], [k], [(h_prim - h)], [(k_prim - k)], units = 'width')


    plt.xlabel('$h$', fontsize=25)
    plt.ylabel('$K$', fontsize=25)


    plt.show()



    ################################


    fig = plt.figure()
    ax = fig.gca(projection='3d')

    h = np.linspace(0,10)
    k = np.linspace(0,10)
    h ,k = np.meshgrid(h, k)
    z = k_prime(h,k)
    z2 = k

    surf = ax.plot_surface(h, k, z, cmap=cm.YlOrRd_r)

    ax.set_zlim(0, 10)
    #ax.zaxis.set_major_locator(LinearLocator(10))
    #ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    #surf = ax.plot_surface(h, k, z2, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    # Add a color bar which maps values to colors.
    #fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.set_xlabel('$h$', fontsize=25)
    ax.set_ylabel('$K$', fontsize=25)
    ax.set_zlabel('$K^\prime$', fontsize=25)
    plt.show()

    #plt.plot(k, k_prime(h, k))
    #plt.plot(k,k)
    #print(k_prime(h,k) - k)
    #plt.show()

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