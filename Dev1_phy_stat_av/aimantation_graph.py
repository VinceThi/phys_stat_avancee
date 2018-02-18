import numpy as np
import scipy as sp
import scipy.optimize
import time
import matplotlib.pyplot as plt
plt.style.use('classic')

def magnetization(m, tc_over_t):
    """
    Fonction qui renvoit tanh(m * tc/t)
    :param m: (float) Valeur de l'aimantation
    :param tc_over_t: (float) Rapport Tc/T
    :return: (float) m
    """
    return np.tanh(m*tc_over_t)

def newton_f(m ,tc_over_t):
    return magnetization(m, tc_over_t) - m

def newton_df(m, tc_over_t):
    return tc_over_t*(1-np.tanh(m*tc_over_t)*np.tanh(m*tc_over_t)) - 1

if __name__ == '__main__':
    for i in np.arange(0,10):
        print(sp.optimize.newton(newton_f,0.2*i*(-1)**i, args=(1.3,)))

    pointlist = np.array([], dtype=np.float32)

    for tc_over_t in np.linspace(0, 2, 1000):
        point = sp.optimize.newton(newton_f,0.2, args=(tc_over_t,))
        if tc_over_t > 1 and abs(point) < 1e-8:
            while abs(point) < 1e-8:
                point = sp.optimize.newton(newton_f, np.random.rand(), args=(tc_over_t,))
        pointlist = np.append(pointlist, point)

    fig = plt.figure(figsize=(12,4))
    ax = fig.add_subplot(121)
    ax.plot(np.linspace(-1, 1), np.linspace(-1, 1), 'b-')
    m = np.linspace(-1, 1, 100)
    color_list = ['y','orange', 'r', 'darkred', 'saddlebrown']
    i = 0
    for tc_sur_t in [1, 1.3, 1.6, 1.9]:
        ax.plot(m, magnetization(m, tc_sur_t), color=color_list[i], label='$T_c/T = {}$'.format(tc_sur_t))
        i += 1
    ax.legend(loc=2, fontsize=15)
    ax.set_xlabel('$m$', fontsize=25)
    ax.set_ylabel('$\\tanh(m T_c/T)$', fontsize=25)

    ax2 = fig.add_subplot(122)
    ax2.plot(np.linspace(0, 2, 1000), abs(pointlist), 'b')
    ax2.plot(np.linspace(0, 2, 1000), -abs(pointlist), 'r')
    ax2.plot([1,2],[0,0], 'purple')
    ax2.set_xlabel('$T_c/T$', fontsize=25)
    ax2.set_ylabel('$m$', fontsize=25)
    plt.show()
