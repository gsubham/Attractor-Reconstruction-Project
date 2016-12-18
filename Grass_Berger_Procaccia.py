import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import logistic_map as ts
import math



#ts
N_hat=1001
L=128
m=1
delta_t=1
tau=5*delta_t
k_1=tau/delta_t
epsi_max=math.exp(6)


def gradient_descent():

	theta_not=2
	theta_one=1.8
	sum=1
	sum_1=1
	alpha=.001
	nop=1
	J=[]
	NOI=[]

	#nod=200
	while(sum!=0 or sum_1!=0):
		print(theta_one)
		#nod=search.nod

		i=0
		sum=0
		sum_1=0
		sum_2=0
		while(i<nod):
			sum=sum+(theta_not+theta_one*ln_r[i]-ln_c[i])
			sum_1=sum_1+(theta_not+theta_one*ln_r[i]-ln_c[i])*ln_r[i]
			sum_2=sum_2+(theta_not+theta_one*ln_r[i]-ln_c[i])*(theta_not+theta_one*ln_r[i]-ln_c[i])
			i=i+1
		sum_2=sum_2/(2.0*nod)	
		J.append(sum_2)	
		theta_not=theta_not-(alpha*sum*1.0)/nod
		theta_one=theta_one-(alpha*sum_1*1.0)/nod
	
	
		nop=nop+1
		NOI.append(nop)
		if(nop==100000):
			#plt.plot(NOI,J)
			break

	print(theta_one)
	return theta_one

def dist(m):
	i=0	
	j=1
	k=1
	N=N_hat-(m-1)*int(k_1)
	for w in range(N+1) :
		l.append([0])
	while(i<N):	
		p=0
		x_1=[]
		while(p<m):

			x_1.append(ts.x[i+p*int(k_1)])
			p=p+1
		d.append(x_1)
		i=i+1
	while(j<N+1):
		n_1=(int(d[j][0]/epsi_max))%L
		n_2=(int(d[j][1]/epsi_max))%L
		if(BOX[n_1][n_2]==0.0):
			BOX[n_1][n_2]=j
			l[int(BOX[n_1][n_2])].append(j)
		if(BOX[n_1][n_2]!=0.0):
			l[int(BOX[n_1][n_2])].append(j)	
		j=j+1
	while(k<N+1):
		print(k)
		n_1=(int(d[k][0]/epsi_max))%L
		n_2=(int(d[k][1]/epsi_max))%L
		neib=[int(BOX[n_1][n_2]),int(BOX[(n_1+1)%L][n_2%L]),int(BOX[(n_1+1)%L][(n_2-1)%L]),int(BOX[n_1%L][(n_2-1)%L]),int(BOX[(n_1-1)%L][(n_2-1)%L]),int(BOX[(n_1-1)%L][n_2%L]),int(BOX[(n_1-1)%L][(n_2+1)%L]),int(BOX[n_1%L][(n_2+1)%L]),int(BOX[(n_1+1)%L][(n_2+1)%L])]
		for n in neib:
			if(n!=0):
				len_=len(l[n])
				q=1
				while(q<len_):
					n_1=l[n][q]
					dis_1=np.linalg.norm(np.asarray(d[n_1])-np.asarray(d[k]))
					if(0<dis_1<=epsi_max):
						dis.append(dis_1)
					q=q+1
						
		k=k+1	
	dis.sort()
	

def binary_search(r):
	#print(r)
	
	len_1=len(dis)
	#print(len_1)
	start=0
	i=0
	while(len_1>0):
		#print(i)
		m_1=start+len_1/2
		if(dis[m_1]<r):
			len_1=len_1-(m_1+1-start)
			start=m_1+1
			i=i+1
			continue
		if(start<m_1 and dis[m_1-1]>=r):
			len_1=m_1-start
			i=i+1
			continue

		return m_1


dimension=[]			
while(m<5):
	N=N_hat-m+2
	dis=[]
	l=[]
	d=[1]
	BOX=np.zeros((L,L))
	dist(m)
	ln_c=[]
	ln_r=[]
	s_1=math.exp(-1)
	s_2=math.exp(3)	
	R=np.linspace(s_1,s_2,1000,endpoint="true")
	nod=0
	nop=0
	sum_3=[]
	#print(R)
	for r in R:
		#print(r)
		#print(binary_search(r))
		if(binary_search(r)==None):
			sum=len(dis)
		else:
			if(dis[binary_search(r)]==r):
				sum=binary_search(r)+1
			else:
				sum=binary_search(r)
		sum_1=(1.0*sum)/(N*N)
		sum_3.append(sum)
		if(sum!=0):
			sum_2=math.log(sum_1)
			ln_c.append(sum_2)
			ln_r.append(math.log(r))
			nod=nod+1
		#print("hello")



		nop=nop+1		
	plt.plot(ln_r,ln_c,'ro')
	slope=gradient_descent()
	dimension.append(slope)
	
	m=m+1

print(dimension)
#print(dis)
#print(len(dis))
plt.show()



