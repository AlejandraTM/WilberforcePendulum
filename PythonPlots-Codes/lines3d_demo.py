import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math as m

fig = plt.figure()
ax = fig.gca(projection='3d')
#Surface
theta = np.linspace(-300 * np.pi, 300 * np.pi, 365)
h=3.
z = np.linspace(-h, 2*h, 365)
#print z
r = z*((2*h)-z)**(1./2.)
y = r * np.sin(theta)
x = r * np.cos(theta)
#ax.plot(Y, Z, X)
ax.plot(a4, a1,a3,'.',label="P3")
ax.plot(a4, a1,-1*a3,'.',label="P3")
ax.plot(b3, b4,b1,'.',label="P1")
ax.plot(-1*b3, b4,b1,'.',label="P2")
ax.grid(True)
plt.legend( ('Singular surface', 'Critical Points of $N_1$', 'Critical Points of $N_2$'), loc = 'upper right')
ax.set_xlabel('$\\alpha_3$',fontsize=18)
ax.set_ylabel('$\\alpha_4$',fontsize=18)
ax.set_zlabel('$\\alpha_1$',fontsize=18)
#ax.set_zlim(-10,20)

plt.show()
