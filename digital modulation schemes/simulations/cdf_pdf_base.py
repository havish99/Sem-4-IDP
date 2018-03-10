from __future__ import division
import matplotlib.pyplot as plt 

import numpy as np 

x=np.arange(-5,5,1e-1)

n=np.random.normal(0,1,10000)

temp=0
prob=[]
pdf=[]
pdf.append(0)
for i in x:
	num=np.nonzero(n<i)
	k=np.size(num)
	prob.append(k/10000)
for i in range(0,len(prob)-1):
	y=(prob[i+1]-prob[i])/(x[i+1]-x[i])
	pdf.append(y)

plt.scatter(x,pdf)
plt.grid()
plt.show()
