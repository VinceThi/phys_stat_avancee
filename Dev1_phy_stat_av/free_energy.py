import numpy as np
import matplotlib.pyplot as plt
def h_prime(h, k):
    return h +(1/2)*np.log(np.cosh(2*k+h)/np.cosh(-2*k +h))

def k_prime(h, k):
    return (1/4)*(np.log(np.cosh(2*k+h))+np.log(np.cosh(-2*k+h)) - np.log((np.cosh(h)*np.cosh(h))))

def inverse_kprime(h,kprim):
    return (1/4) * np.arccosh(2*np.cosh(h)*np.cosh(h)*np.exp(4*kprim)-np.cosh(2*h))

def free_g(previous_k,h, previous_g):
    return (1/2) *( np.log(2) + np.log(np.cosh(h))+ previous_k + previous_g)

def g_init(h):
    return np.log(2*np.cosh(h))

if __name__ == '__main__':

    hlist = np.arange(0, 2.5, 0.5)
    #hlist = [0, 100]
    hlist = [1]
    k_init = 0.01


    for h in hlist:
        i = 0
        kprim = 0.01
        previous_g = g_init(h)
        karr = np.array([],dtype=float)
        garr = np.array([], dtype=float)
        karr = np.append(karr, kprim)
        garr = np.append(garr, previous_g)
        print(previous_g)
        while i < 20:
            k = inverse_kprime(h, kprim)
            g = free_g(kprim,h, previous_g)
            #print(h, '    :     ', k, "   &   ", g)
            print(g)
            #plt.plot([kprim, k], [previous_g, g])
            karr = np.append(karr, k)
            garr = np.append(garr, g)


            kprim = k
            previous_g = g
            i += 1
        print('___________________________')
        plt.plot(karr, garr, label='$h = '+str(h) + '$')
    plt.xlim([0,5])
    plt.ylim([0, 5])
    plt.legend(loc=0)
    plt.xlabel('$K$', fontsize=20)
    plt.ylabel('$g(K, h)$', fontsize=20)
    plt.show()

