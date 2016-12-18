import numpy as np 	
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import lorenz as ts
from operator import itemgetter
import math


""" Parameters for FNN algorithm (lorenz system)
intial conditions=[1,2,3]  parameters=[16,45.92,4] deta_t=.02 No. of data points 41000
Tau=5*delta_t  R_tol=15 A_tol=2
"""

class node:
	def __init__(self,value):
		self.right=None
		self.left=None
		self.value=value	

# Creates axis kd tree where dimension is the dimension of the points
def kd_tree(point_list,depth,dimension):
	if(len(point_list)==0):
		return None
	axis=depth%dimension

	#sort point_list according to axis component
	#find the median of the sorted list
	
	point_list=sorted(point_list,key=lambda y:y[axis])
	
	median=len(point_list)/2
	
	
	tree=node(point_list[median])
	point_list_right=point_list[median+1::]
	point_list_left=point_list[0:median:]	
	tree.right=kd_tree(point_list_right,depth+1,dimension)
	tree.left=kd_tree(point_list_left,depth+1,dimension)	
	return tree

# Finds the nearest neighbour of the query in kd tree where head is the head of the tree
def nearest_neib(query,head,depth,dimension):
	axis=depth%dimension

	if(head.right==None and head.left==None):
		
		return head


	if(head.right==None):
		nearest_left=nearest_neib(query,head.left,depth+1,dimension)
		
		
		radius=np.linalg.norm(np.asarray(query[:d:])-np.asarray(nearest_left.value[:d:]))

		distance=np.linalg.norm(np.asarray(query[:d:])-np.asarray(head.value[:d:]))
		if(distance!=0 and radius!=0):
			minimum=min(distance,radius)
		if(distance==0):
			return nearest_left
		if(radius==0):
			return head	
		if(minimum==radius):
			return nearest_left
		if(minimum==distance):
			return head				

	if(head.left==None):
		nearest_right=nearest_neib(query,head.right,depth+1,dimension)
		radius=np.linalg.norm(np.asarray(query[:d:])-np.asarray(nearest_right.value[:d:]))
		distance=np.linalg.norm(np.asarray(query[:d:])-np.asarray(head.value[:d:]))
		if(distance!=0 and radius!=0):
			minimum=min(distance,radius)
		if(distance==0):
			return nearest_right	
		if(radius==0):
			return head
		if(minimum==radius):
			return nearest_right
		if(minimum==distance):
			return head	

	if(query[axis]>=head.value[axis]):
		nearest_right=nearest_neib(query,head.right,depth+1,dimension)
		radius=np.linalg.norm(np.asarray(query[:d:])-np.asarray(nearest_right.value[:d:]))
		if(abs(head.value[axis]-query[axis])<radius):
			nearest_left=nearest_neib(query,head.left,depth+1,dimension)
			distance=np.linalg.norm(np.asarray(query[:d:])-np.asarray(head.value[:d:]))
			distance_=np.linalg.norm(np.asarray(query[:d:])-np.asarray(nearest_left.value[:d:]))
			if(distance!=0 and distance!=0 and distance_!=0):
				minimum=min(radius,distance_,distance)
			if(distance==0):
				minimum=min(radius,distance_)
			if(radius==0):
				minimum=min(distance,distance_)		
			if(distance_==0):
				minimum=min(radius,distance)
			if(minimum==radius):
				return nearest_right
			if(minimum==distance_):
				return nearest_left
			if(minimum==distance):
				return head		
		
		if(abs(head.value[axis]-query[axis])>radius):
			distance=np.linalg.norm(np.asarray(query[:d:])-np.asarray(head.value[:d:]))
			if(distance!=0 and radius!=0):
				minimum=min(distance,radius)
			if(distance==0):
				return nearest_right
			if(radius==0):
				return head		
			if(minimum==radius):
				return nearest_right
			if(minimum==distance):
				return head	

	if(query[axis]<head.value[axis]):
		
		nearest_left=nearest_neib(query,head.left,depth+1,dimension)
		
		radius=np.linalg.norm(np.asarray(query[:d:])-np.asarray(nearest_left.value[:d:]))
		if(abs(head.value[axis]-query[axis])<radius):

			nearest_right=nearest_neib(query,head.right,depth+1,dimension)
			distance=np.linalg.norm(np.asarray(query[:d:])-np.asarray(head.value[:d:]))
			distance_=np.linalg.norm(np.asarray(query[:d:])-np.asarray(nearest_right.value[:d:]))
			if(distance!=0 and radius!=0 and distance_!=0):
				minimum=min(radius,distance_,distance)
			if(distance==0):
				minimum=min(radius,distance_)
			if(distance_==0):
				minimum=min(radius,distance)
			if(radius==0):
				minimum=min(distance_,distance)		
			if(minimum==distance_):
				return nearest_right
			if(minimum==radius):
				return nearest_left
			if(minimum==distance):
				return head		
		
		if(abs(head.value[axis]-query[axis])>radius):
			distance=np.linalg.norm(np.asarray(query[:d:])-np.asarray(head.value[:d:]))

			if(distance!=0 and radius!=0):
				minimum=min(distance,radius)
			if(distance==0):
				return nearest_left
			if(radius==0):
				return head	
			if(minimum==radius):
				return nearest_left
			if(minimum==distance):
				return head				
			

x=ts.x
N_hat=20000 #number of data points of the time series
delta_t=ts.delta_t
tau=5*delta_t
ratio=int(tau/delta_t)

embedding_dimension=np.linspace(1,12,12)
FNN=[] # percentage of false nearest neighbours

R_tol=15.0
A_tol=2.0
mean=0.0
variance=0.0
d=1 #Embedding Dimension

j=0	
#Mean of the time series
while(j<N_hat):
	mean=mean+x[j]
	j=j+1
mean=(mean*1.0)/N_hat

j=0
#variance of the time series
while(j<N_hat):
	variance=variance+(x[j]-mean)*(x[j]-mean)
	j=j+1
variance=(variance*1.0)/N_hat	
R_A=math.sqrt(variance) #Standard deviation of the data

while(d<13):
	
	i=0
	sum=0
	N_bar=0
	N=N_hat-(d-1)*ratio #number of points in embedded space
	x_bar=[] #list of all points in embedded space
	
	#Filling points in x_bar
	while(i<N):
		j=0
		x_1=[]
		while(j<d):
			x_1.append(x[i+j*ratio])
			j=j+1
		x_1.append(i)	
		x_bar.append(x_1) 	
		i=i+1
	
	# creates a k_d tree from points in x_bar
	#tree is the head of the k_d tree

	tree=kd_tree(x_bar[:],0,d)
	#Nearsest neighbhour of each element
	
	i=0
	while(i<N):

		nearest=nearest_neib(x_bar[i],tree,0,d)
		nearest_index=nearest.value[d]
		test_point_index=i
		if(test_point_index+ratio*d<N_hat and nearest_index+ratio*d<N_hat):
			p_1=x[test_point_index+ratio*d]
			p_2=x[nearest_index+ratio*d]
			x_1=x_bar[i][:d:]
			x_2=nearest.value[:d:]
			x_1.append(p_1)
			x_2.append(p_2)
			distance_1=abs(p_1-p_2)
			distance_2=np.linalg.norm(np.asarray(x_bar[i][:d:])-np.asarray(nearest.value[:d:])) # R_d(n)
			distance_3=np.linalg.norm(np.asarray(x_1)-np.asarray(x_2)) # R_(d+1)(n)
			first_test=(distance_1*1.0/(distance_2))>R_tol
			second_test=(distance_3*1.0/(R_A))>A_tol
			if(second_test or first_test):
				sum=sum+1
			N_bar=N_bar+1

		i=i+1	
	percentage=(sum*1.0/N_bar)*100
	FNN.append(percentage)	
	print(N_bar)	
	d=d+1

print(FNN)	
plt.plot(embedding_dimension,FNN,'ro')
plt.show()