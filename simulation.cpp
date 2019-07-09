//Wilberforce Pendulum Simulation by Verlat Method
	//Alejandra Torres Manotas (julio/2019)
#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <fstream>
using namespace std;

double x, px, y, py,x2, px2, y2, py2, k, epsilon, iterations;
string name;
//This functions are the method functions which represent the x-momentum derivative and the y-momentum derivative
double F1(double a, double b, double e)
{
	return -(a+(2.0*e*a*pow(b,2.0)));
};

double F2(double a, double b, double e)
{
	return -((4.0*b)+(2.0*e*b*pow(x,2.0)));
};

int main()
{
	//Varietion of epsilon value from 0 to 1 in 0.1 steps size
	for(double epsilon=0.5;epsilon<=1.0;epsilon=epsilon+0.1)
	{
		//Archive where we will save the solutions of the method
		name="Sperturbation3"+to_string(epsilon)+".txt";
		ofstream archivo;
		archivo.open(name,ios::out);
		if(archivo.fail())
		{
			cout<<"No se pudo abrir el archivo."<<"\n";
			exit(1);
		}
		/*Method inicialization:
			k is the step size of the method
			(x,px,y,py) are the initial conditions
			Iterations is the number of method iterations
			*/
		k= 0.005;
		x=1.0;
		px=1.0;
		y=1.0;
		py=1.0;
		iterations=0.0;
		cout<<"Epsilon: "<<epsilon<<"\n";
		do{	//Method implementation	
			x2=x+(k*px)+((pow(k,2.0)/2.0)*F1(x,y,epsilon));
			y2=y+(k*py)+((pow(k,2.0)/2.0)*F2(x,y,epsilon));
			px2=px+((k/2.0)*(F1(x2,y2,epsilon)+F1(x,y,epsilon)));
			py2=py+((k/2.0)*(F2(x2,y2,epsilon)+F2(x,y,epsilon)));
			archivo<<iterations<<";"<<x<<";"<<px<<";"<<y<<";"<<py<<"\n";
			iterations=iterations+k;
			x=x2;y=y2;px=px2;py=py2;
		}while(iterations<=5000);
		archivo.close();
	}
}

/* Runnig instructions:
	$ g++ simulation.cpp  -o sm
	$ ./sm
*/

