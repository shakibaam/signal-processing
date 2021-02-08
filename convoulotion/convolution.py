import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np


def convolution (x, h):
    x_size = len(x)
    h_size = len(h)
    y = [0 for i in range(x_size+h_size-1)]
    for i in range(x_size+h_size-1):
        if (i<=x_size-1):
            for j in range (i+1):
                y[i]=x[j]*h[i-j]+y[i]

        elif(i>=x_size):
            z=i-(x_size-1)
            for j in range(z,x_size):
                y[i] = x[j] * h[i - j] + y[i]


    print(y)
    return y




start_a = -10
stop_a = 10
step_a = 0.1
n1 = np.linspace(start_a, stop_a+1, int((stop_a - start_a) / step_a))
x1=0.5*np.exp(-2*n1)*np.heaviside(n1,1)
h1=np.heaviside(n1,1)-np.heaviside(n1-5,1)


temp1_a=np.convolve(x1,h1)
temp_a=convolution(x1,h1)
start_a_c = -20
stop1_a_c = 20

n1_c = np.linspace(start_a_c, stop1_a_c, (int((stop1_a_c - start_a_c) / step_a))-1)
plt.plot(n1_c,temp_a,'r',label='plot1_function')
plt.plot(n1_c,temp1_a,'b',label='plot1_library')
plt.xlabel('N-axis')
plt.ylabel('X-axis')
plt.legend()
plt.show()



start_b = -5
stop_b= 10
step_b = 1
# n2 = np.linspace(start_b, stop_b, int((stop_b - start_b) / step_b))
n2=np.arange(-5,10)
x2=np.power(1/3,-1*n2)*np.heaviside(-1*n2-1,1)
h2=np.heaviside(n2-1,1)




temp1_b=np.convolve(x2,h2)
temp_b=convolution(x2,h2)
start_b_c = -10
stop1_b_c = 20

n2_c = np.linspace(start_b_c, stop1_b_c, (int((stop1_b_c - start_b_c) / step_b))-1)
plt.stem(n2_c,temp1_b,'b',label='plot2_library')
plt.stem(n2_c,temp_b,'r',label='plot2_function')
plt.xlabel('N-axis')
plt.ylabel('X-axis')
plt.legend()
plt.show()



start_3 = -5
stop_3= 10
step_3 = 1
n3=np.arange(-5,10)
x3=np.heaviside(n3,1)-np.heaviside(n3-3,1)+np.heaviside(n3-5,1)-np.heaviside(n3-8,1)
h3=np.heaviside(n3,1)*np.power(1/3,n3)


temp1_c=np.convolve(x3,h3)
temp_c=convolution(x3,h3)
start_b_c = -10
stop1_b_c = 20
step_3=1

n3_c = np.linspace(start_b_c, stop1_b_c, (int((stop1_b_c - start_b_c) / step_3))-1)

plt.stem(n3_c,temp1_c,'b',label='plot3_library')
plt.stem(n3_c,temp_c,'r',label='plot3_function')
plt.xlabel('N-axis')
plt.ylabel('X-axis')
plt.legend()
plt.show()