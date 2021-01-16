#Plot of Wilberforce Pendulum
import numpy as np
import matplotlib.pyplot as plt

#Read File Method Solution
#p1,v1=np.loadtxt("PoincareMAp30.000000.txt",delimiter=';', usecols=(0,1),unpack=True)
#p,v=np.loadtxt("PoincareMAp320.000000.txt",delimiter=';', usecols=(0,1),unpack=True)
t3,p13,v13,p23,v23=np.loadtxt("Sperturbation1.000000.txt",delimiter=';', usecols=(0,1,2,3,4),unpack=True)
#pi,vi,pj,vj=np.loadtxt("PMInit1.000000.txt",delimiter=';', usecols=(0,1,2,3),unpack=True)
#Poincare Map Plots
option =0

while(option!=4):
	option=int(input(" 0. Movement \n 1. Poincare Map \n 2. Init Conditions \n 3. Exit \n"))
	if(option==0):
		fig, ax=plt.subplots()
		ax.plot(p13,p23,'b.', markersize=0.05,label="Pendulum")
		ax.set_xlabel('x')
		ax.set_ylabel('y')
		#plt.xlim(-0.5,0.5)
		#plt.ylim(-3.0,3.0)
		ax.grid(True)
		ax.set_title("Wilberforce Pendulum for $\epsilon=1$")
		#plt.title("First Particle Phase Space with $\epsilon=0.0$")
		plt.savefig('Mov(1)')
		plt.show()
	if(option==1):
		fig, ax=plt.subplots()
		ax.plot(p1,v1,'r.', markersize=1)
		ax.plot(p,v,'b.', markersize=1)
		ax.set_xlabel('Position')
		ax.set_ylabel('Momentum')
		#plt.xlim(-.2,.2)
		#plt.ylim(-1.8,-2.2)
		ax.grid(True)
		ax.set_title("Poincare Map with $\epsilon=1$")
		plt.savefig('PM(1)')
		plt.show()
	elif(option==2):
		fig, ax=plt.subplots()
		ax.plot(pi,vi,'r.', markersize=0.5)
		ax.set_xlabel('Position')
		ax.set_ylabel('Momentum')
		#plt.xlim(-.2,.2)
		#plt.ylim(-1.8,-2.2)
		ax.grid(True)
		ax.set_title("Condiciones Iniciales")
		plt.savefig('initPM1(1)')
		plt.show()
		fig, ax=plt.subplots()
		ax.plot(pj,vj,'b.', markersize=0.5)
		ax.set_xlabel('Position')
		ax.set_ylabel('Momentum')
		#plt.xlim(-.2,.2)
		#plt.ylim(-1.8,-2.2)
		ax.grid(True)
		ax.set_title("Condiciones Iniciales")
		plt.savefig('initPM2(1)')
		plt.show()
	elif(option==3):
		break;

	
