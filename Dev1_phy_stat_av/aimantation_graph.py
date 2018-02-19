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
                                                                                                                                                     
    #On utilise Tc sur T                                                                                                                             
                                                                                                                                                     
    return np.tanh(m*tc_over_t)                                                                                                                      
                                                                                                                                                     
def magnetization_H(m, tc_over_t, muH_over_jq):                                                                                                      
                                                                                                                                                     
    return np.tanh(tc_over_t*(m+muH_over_jq))                                                                                                        
                                                                                                                                                     
def newton_f(m ,tc_over_t):                                                                                                                          
    return magnetization(m, tc_over_t) - m                                                                                                           
                                                                                                                                                     
def newton_fH(m, tc_over_t, muH_over_jq):                                                                                                            
    return magnetization_H(m, tc_over_t, muH_over_jq) - m                                                                                            
                                                                                                                                                     
def newton_df(m, tc_over_t):                                                                                                                         
    return tc_over_t*(1-np.tanh(m*tc_over_t)*np.tanh(m*tc_over_t)) - 1                                                                               
                                                                                                                                                     
def newton_dfH(m, tc_over_t, muH_over_jq):                                                                                                           
    return tc_over_t*(1-magnetization_H(m, tc_over_t, muH_over_jq)*magnetization_H(m, tc_over_t, muH_over_jq)) - 1                                   
                                                                                                                                                     
if __name__ == '__main__':                                                                                                                           
    #plt.rc('text', usetex=True)                                                                                                                     
                                                                                                                                                     
    for i in np.arange(0,10):                                                                                                                        
        print(sp.optimize.newton(newton_f,0.2*i*(-1)**i, newton_df, args=(1.3,)))                                                                    
                                                                                                                                                     
    pointlist = np.array([], dtype=np.float32)                                                                                                       
                                                                                                                                                     
    for tc_over_t in np.linspace(0,2, 1000):                                                                                                         
        point = sp.optimize.newton(newton_f,0.2, args=(tc_over_t,))                                                                                  
        if tc_over_t > 1 and abs(point) < 1e-8:                                                                                                      
            while abs(point) < 1e-8:                                                                                                                 
                point = sp.optimize.newton(newton_f, np.random.rand(), newton_df, args=(tc_over_t,))                                                 
        pointlist = np.append(pointlist, point)                                                                                                      
                                                                                                                                                     
    fig = plt.figure(figsize=(13, 9))                                                                                                                
    ax = fig.add_subplot(221)                                                                                                                        
    ax.plot(np.linspace(-1, 1), np.linspace(-1, 1), 'b-', label='$m = m$')                                                                           
    ax.set_title("$a) \:\: H = 0$", fontsize=25)                                                                                                     
    m = np.linspace(-2, 2, 100)                                                                                                                      
    color_list = ['y', 'orange', 'r', 'darkred', 'saddlebrown']                                                                                      
    i = 0                                                                                                                                            
    for tc_sur_t in [0.5, 1, 1.5, 2]:                                                                                                                
        ax.plot(m, magnetization(m, tc_sur_t), color=color_list[i], label='$T_c/T = {}$'.format(tc_sur_t))                                           
        i += 1                                                                                                                                       
    ax.legend(loc=2, fontsize=14)                                                                                                                    
    ax.set_xlabel('$m$', fontsize=25)                                                                                                                
    ax.set_ylabel('$\\tanh(m T_c/T)$', fontsize=25)                                                                                                  
                                                                                                                                                     
    ax2 = fig.add_subplot(222)                                                                                                                       
    ax2.set_title("$b)$", fontsize=25)                                                                                                               
    ax2.plot(np.linspace(0, 2, 1000)[499:], abs(pointlist[499:]), 'b')                                                                               
    ax2.plot(np.linspace(0, 2, 1000)[499:], -abs(pointlist[499:]), 'r')                                                                              
    ax2.plot([0, 2], [0, 0], 'purple')                                                                                                               
    ax2.set_xlabel('$T_c/T$', fontsize=25)                                                                                                           
    ax2.set_ylabel('$m$', fontsize=25)                                                                                                               
                                                                                                                                                     
                                                                                                                                                     
    ################# With magnetic field ########################                                                                                   
                                                                                                                                                     
    pointlist = np.array([], dtype=np.float32)                                                                                                       
                                                                                                                                                     
    for tc_over_t in np.linspace(0,2, 1000):                                                                                                         
        point = sp.optimize.newton(newton_fH,0.2, args=(tc_over_t, 1))                                                                               
        if tc_over_t > 1 and abs(point) < 1e-8:                                                                                                      
            while abs(point) < 1e-8:                                                                                                                 
                point = sp.optimize.newton(newton_fH, np.random.rand(), newton_dfH, args=(tc_over_t, 1))                                             
        pointlist = np.append(pointlist, point)                                                                                                      
                                                                                                                                                     
    #fig = plt.figure(figsize=(12, 4))                                                                                                               
                                                                                                                                                     
    ax3 = fig.add_subplot(223)                                                                                                                       
    ax3.set_title("$c)\:\: \mu H/Jq= 1$", fontsize=25)                                                                                               
    #ax3.plot([], [], ' ', label=r"$\frac{\mu H}{Jq} = 1$")                                                                                          
    ax3.plot(np.linspace(-1, 1), np.linspace(-1, 1), 'b-', label='$m = m$')                                                                          
    m = np.linspace(-2, 2, 100)                                                                                                                      
    color_list = ['y', 'orange', 'r', 'darkred', 'saddlebrown']                                                                                      
    i = 0                                                                                                                                            
    for tc_sur_t in [0.5, 1, 1.5, 2]:                                                                                                                
        ax3.plot(m, magnetization_H(m, tc_sur_t, 1), color=color_list[i], label='$T_c/T = {}$'.format(tc_sur_t))                                     
        i += 1                                                                                                                                       
                                                                                                                                                     
    ax3.legend(loc=0, fontsize=15)                                                                                                                   
    ax3.set_xlabel('$m$', fontsize=25)                                                                                                               
    ax3.set_ylabel(r'$\tanh\left[\frac{T_c}{T}\left(m + \frac{\mu H}{Jq}\right)\right]$', fontsize=25)                                               
                                                                                                                                                     
    ax4 = fig.add_subplot(224)                                                                                                                       
    ax4.set_title("$d)$", fontsize=25)                                                                                                               
    ax4.plot(np.linspace(0, 2, 1000), abs(pointlist), 'b')                                                                                           
    #ax4.plot(np.linspace(0, 2, 1000), -abs(pointlist), 'r')                                                                                         
    #ax4.plot([0, 2], [0, 0], 'purple')                                                                                                              
    ax4.set_xlabel('$T_c/T$', fontsize=25)                                                                                                           
    ax4.set_ylabel('$m$', fontsize=25)                                                                                                               
    plt.show()                                                                                                                                       
