import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import lorenz as ts
import math

def perturbation(n,e):
	A=np.array([[-a,a,0],[b-z[n],-1,-x[n]],[y[n],x[n],-c]])
	x_tilda_vector=e
	B=A.dot(x_tilda_vector)
	x_tilda_hat=e[0]+delta_t*B[0]
	y_tilda_hat=e[1]+delta_t*B[1]
	z_tilda_hat=e[2]+delta_t*B[2]
	x_tilda_vector_hat=np.array([x_tilda_hat,y_tilda_hat,z_tilda_hat])
	C=A.dot(x_tilda_vector_hat)
	D=B+C
	x_tilda=e[0]+delta_t*(D[0])/2.0
	y_tilda=e[1]+delta_t*(D[1])/2.0
	z_tilda=e[2]+delta_t*(D[2])/2.0
	x_tilda_vector=np.array([x_tilda,y_tilda,z_tilda])
	
	return x_tilda_vector


def gram_schmidt(p,e_hat):
	k=0
	e_bar=[]
	e=[]
	while(k<p):
		i=0
		sum=np.array([0,0,0])
		while(i<k):
			sum=sum+np.dot(e_hat[k],e[i])*e[i]
			i=i+1

		e_bar.append(e_hat[k]-sum)
		e.append((e_bar[k]*1.0)/np.linalg.norm(e_bar[k]))
		k=k+1
	

	return e

def volume(p,e_hat):
	if(p==1):
		return np.linalg.norm(e_hat[0])
	if(p==2):
		c=np.cross(e_hat[0],e_hat[1])
		return np.linalg.norm(c)
	if(p==3):
		c=np.cross(e_hat[1],e_hat[2])
		d=np.dot(e_hat[0],c)
		return np.linalg.norm(d)
			


x=ts.x
y=ts.y
z=ts.z
a=ts.a
b=ts.b
c=ts.c
delta_t=ts.delta_t
p=1
lyapunov=[]


while(p<4):
	n=0
	N=0
	v=[1]
	e=[[1,0,0],[0,1,0],[0,0,1]]
	sigma=[0]

	while(n<41000):
		k=0
		e_hat=[]
		while(k<p):
			e_hat.append(perturbation(n,e[k]))
			#print("Hello")
			#print(p)
			k=k+1
		v.append(volume(p,e_hat))	
		e=gram_schmidt(p,e_hat)	
		n=n+1
	
	while(N+1<41000):
		a_1=(N*1.0/(N+1))*sigma[N]
		b_1=(1.0/(delta_t*(N+1)))*(math.log(v[N+1]))
		sigma.append(a_1+b_1)
		N=N+1
	j=0
	sum=0
	while(j<p-1):
		sum=sum+lyapunov[j]
		j=j+1

	lyapunov.append(sigma[N]-sum)	

	p=p+1	


print(lyapunov)
