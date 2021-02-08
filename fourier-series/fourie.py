import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

def fouriye (T ,  x_t):
    start = 0
    end = T
    step = 0.001
    w=((np.pi)*2)/T
    a=[]
    b=[]

    t = np.arange(start, end, step)
    for i in range(0,11):


        x1 = x_t * np.sin(t*w*i)
        x2 = x_t * np.cos(t*w*i)
        integral_sin = np.sum(x1) * step
        integral_cos = np.sum(x2) * step
        # print(integral_sin)  # = 2
        # print(integral_cos)
        a.insert(i,(2 / T) * integral_cos)
        b.insert(i,2 / T * integral_sin)

    a_numpy=np.array(a)
    b_numpy=np.array(b)
    sum1=a[0]/2

    for k in range(0,11):


         sum1 +=  (a[k] * np.cos(k * ((np.pi * 2) / T) * t)) + (b[k] * np.sin(k * ((np.pi * 2) / T) * t))
         plt.plot(t, sum1)
         plt.show()









N=np.arange(-3,3,0.001)
t=np.arange(-3,3,0.001)
choices=[1,-1]
conditions=[N<0 , N>=0]
X=np.select(conditions,choices)

plt.plot(N, X, 'b', label="X1")
plt.xlabel('t-axis')
plt.ylabel('X-axis')
plt.legend()
plt.show()
# fouriye (6 ,  X)


conditions2=[ (t>-3) & (t<-2) , (t>-2) & (t<=-1) , (t>-1) & (t<=1) , (t>1) & (t<=2) , (t>2) & (t<=3) ]
choices2=[0 ,t+2 , -1*t , t-2 ,0]

X2=np.select(conditions2,choices2)
plt.plot(N, X2, 'b', label="X2")
plt.xlabel('t-axis')
plt.ylabel('X-axis')
plt.legend()
plt.show()
fouriye (6 ,  X2)





