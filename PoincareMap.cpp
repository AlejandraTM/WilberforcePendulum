#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <fstream>
#include<time.h>
using namespace std;

double x, px, y, py, k, epsilon, pi, section,x0, signo, i;
string name, name2;

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
	pi=4.0*atan(1.0);
	k=0.005;
	section=0.0;
	//Varietion of epsilon value from 0 to 1 in 0.1 steps size
	for(double epsilon=0.0;epsilon<=1.0;epsilon=epsilon+0.1)
	{
		//Archive where we will save the solutions of the method
		name="PoincareMAp2"+to_string(epsilon)+".txt";
		ofstream archivo, archivo2;
		archivo.open(name,ios::out);
		if(archivo.fail())
		{
			cout<<"No se pudo abrir el archivo."<<"\n";
			exit(1);
		}
		name2="PMInit"+to_string(epsilon)+".txt";
		archivo2.open(name2,ios::out);
		if(archivo.fail())
		{
			cout<<"No se pudo abrir el archivo."<<"\n";
			exit(1);
		}
		i=0.0;
		do{	
		/*Method inicialization:
			k is the step size of the method
			(x,px,y,py) are the initial conditions
			t is the number of method iterations
			*/
			double x2, px2, y2, py2,t;
			srand(i);
			t=0.0;
			x=1.5; 
			px=(-100.0+rand()%(201))/100.0;
			y=0.01;
			py=-pow(2.0*(3.0-epsilon*pow(x*y,2.0))-(pow(px,2.0)+pow(x,2.0)+4.0*pow(y,2.0)),0.5);
			archivo2<<x<<";"<<px<<";"<<y<<";"<<py<<"\n";
			archivo<<x<<";"<<px<<"\n";
			do{
				//Method implementation	
				x2=x+(k*px)+((pow(k,2.0)/2.0)*F1(x,y,epsilon));
				y2=y+(k*py)+((pow(k,2.0)/2.0)*F2(x,y,epsilon));
				px2=px+((k/2.0)*(F1(x2,y2,epsilon)+F1(x,y,epsilon)));
				py2=py+((k/2.0)*(F2(x2,y2,epsilon)+F2(x,y,epsilon)));
				if(y*y2<section)//Poincare Section y=0
				{
					t=t+1.0;
					if(abs(y)<abs(y2))//Data condition. The minimun distance to zero.
					{
						archivo<<x<<";"<<px<<"\n";
					}
					else
					{
						archivo<<x2<<";"<<px2<<"\n";
					}
				}
				x=x2;y=y2;px=px2;py=py2;
			}while(t<=200.0);
			i=i+1.0;
		}while(i<=100.0);
		archivo.close();
		cout<<"epsilon= "<<epsilon<<"\n";
	}
}

/* Runnig instructions:
	$ g++ -O3 PoincareMap.cpp  -o pm
	$ ./pm
*/
