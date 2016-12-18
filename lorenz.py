#runge-kutta method

import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt


def func(x,y,z):
	x_dot=[-a*x+a*y,b*x-y-x*z,-c*z+x*y]
	return x_dot
def phase():
	fig = plt.figure()
	ax = Axes3D(fig)
	ax.plot(x,y,z)
	ax.set_xlabel("x")
	ax.set_ylabel("y")
	ax.set_zlabel("z")
	plt.show()
def xtime_series():
	plt.plot(t,x)	
	plt.show()

def ytime_series():
	plt.plot(t,y)
	plt.show()
def ztime_series():
	plt.plot(t,z)
	plt.show()


xnot=input()
ynot=input()
znot=input()
a=input()
b=input()
c=input()	
x=[xnot]
y=[ynot]
z=[znot]
xhat=[]
yhat=[]
zhat=[]
t=np.linspace(0,1000,100001,endpoint="True")
n=0
delta_t=.01  

while(n+1<100001):
	x_hat=func(x[n],y[n],z[n])	#f(x[n])
	xhat.append(x_hat[0]*delta_t+x[n])
	yhat.append(x_hat[1]*delta_t+y[n])
	zhat.append(x_hat[2]*delta_t+z[n])
	y_hat=func(xhat[n],yhat[n],zhat[n]) # f(xhat[n])
	x.append(x[n]+(delta_t/2)*(x_hat[0]+y_hat[0]))
	y.append(y[n]+(delta_t/2)*(x_hat[1]+y_hat[1]))
	z.append(z[n]+(delta_t/2)*(x_hat[2]+y_hat[2]))
	n=n+1

xtime_series()
phase()




