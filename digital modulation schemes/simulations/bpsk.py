from __future__ import division
import numpy as np 
import matplotlib.pyplot as plt 
from scipy import special 
simlen=10000

def coin(x):
	return 2*np.random.randint(2,size=x)-1
x=np.arange(-10,10,1e-1)
X=coin(simlen)
N=np.random.normal(0,1,simlen)
A=4 # this can be changed
temp=0
Y=A*X+N
pdf=[]
prob=[]
pdf.append(0)
for i in x:
	num=np.nonzero(Y<i)
	k=np.size(num)
	prob.append(k/10000)
for i in range(0,len(prob)-1):
	y=(prob[i+1]-prob[i])/(x[i+1]-x[i])
	pdf.append(y)

plt.plot(pdf)
plt.grid()
plt.show()







