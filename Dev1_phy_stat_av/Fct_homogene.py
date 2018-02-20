import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
plt.style.use('classic')

#x = np.linspace(0,1,10000)
#x2 = np.linspace(0,1,10)
#def f(x): return np.sqrt(x)
#
#fig=plt.figure()
#ax=fig.add_subplot(111, label="1")
#ax2=fig.add_subplot(111, label="2", frame_on=False)
#ax3=fig.add_subplot(111, label="3", frame_on=False)
#
#ax.plot(x, f(x), 'k')
#ax.set_ylabel('$f(x)$', fontsize=25)
#ax.set_xlabel('$x$', fontsize=25, x=1.0, y=0.1)
#ax.tick_params(axis='x', colors="k")
#ax.tick_params(axis='y', colors="k")
#
#ax2.plot(4*x2, 2*f(x2), 'ro')
#ax2.xaxis.tick_top()
#ax2.yaxis.tick_right()
#ax2.set_ylabel('$2f(x)$', fontsize=25, color='r')
#ax2.set_xlabel('$2^2x$', fontsize=25, x=1.0, y=0.1, color='r')
#ax2.xaxis.set_label_position('top')
#ax2.yaxis.set_label_position('right')
#ax2.tick_params(axis='x', colors="r")
#ax2.tick_params(axis='y', colors="r")
#
#ax3.set_xticks([])
#ax3.set_yticks([])
#plt.show()


def g(x, y): return y/np.abs(x)








fig = plt.figure()
ax = fig.add_subplot(1, 2, 1, projection='3d')
#ax = fig.gca(projection='3d')
# Make data.
X = np.linspace(1, 5, 100)
Y = np.linspace(1, 5, 100)
X, Y = np.meshgrid(X, Y)

# Plot the surface.
surf = ax.plot_surface(X, Y, g(X,Y), cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
#fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_ylabel('$y$', fontsize=25)
ax.set_xlabel('$x$', fontsize=25)
ax.set_zlabel('$f(x,y)$', fontsize=25)

plt.subplot(122)
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
#ax2 = fig.gca(projection='3d')

# Plot the surface.
surf = ax2.plot_surface(4*X, 8*Y, 2*g(X,Y), cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
#ax2.zaxis.set_major_locator(LinearLocator(10))
#ax2.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
#fig.colorbar(surf, shrink=0.5, aspect=5)

ax2.set_ylabel('$2^3y$', fontsize=20, linespacing=3.2)
ax2.set_xlabel('$2^2x$', fontsize=20, linespacing=3.2)
ax2.set_zlabel('$2f(x,y)$', fontsize=25, linespacing=3.2)

plt.show()