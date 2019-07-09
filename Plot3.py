import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math as m
mpl.rcParams['text.usetex'] = True
fig = plt.figure()
ax = fig.gca(projection='3d')
#Surface
theta = np.linspace(0.0, 300 * np.pi, 10000)
h=1.
x = np.linspace(0.0, 2*h, 10000)
#print z
r = x*((2.*h)-x)**(1./2.)
z = r * np.sin(theta)
y = r * np.cos(theta)
#Points 3 and 4
p3a1=2.*h*(((21.)**(1./2.)-1.)/((21.)**(1./2.)+3.))
py3=(((2.*h-p3a1)*p3a1**2.)**(3./2.))*np.sin(theta)
pz3=(((2.*h-p3a1)*p3a1**2.)**(3./2.))*np.cos(theta)
p3a3=(2./3.)*((h)**(3./2.))*(62*(21)**(1./2.)-282)**(1./2.)
p3a4=0.0
#ax.plot(Y, Z, X)
ax.grid(True)
plt.plot(x,y,z,label='Singular Surface')
plt.plot(p3a1+x*0,p3a3+py3*0,p3a4+pz3*0,'.',label=r'$P_3$')
plt.plot(p3a1+x*0,-p3a3+py3*0,p3a4+pz3*0,'.',label=r'$P_4$')
plt.plot(x*0,y*0,z*0,'.',label=r'$(0,0,0)$')
plt.plot(x*0+2*h,y*0,z*0,'.',label=r'$(2h,0,0)$')
plt.title(R'Critical Points of the Hamiltonian Normal Form'  )

#label and axes
plt.xticks(np.linspace(0.,2,5, endpoint=False),label=r'$\alpha_1$')
plt.yticks(np.linspace(-1.2,1.2,5, endpoint=True))
#box=ax.get_position()
#ax.get_position([box.x0,box.y0,box.width,box.height])
#ax.legend(loc='best', bbox_to_anchor=(1,1.05,0.,0.),shadow=True, fontsize='medium')
#Show plot
plt.show()
