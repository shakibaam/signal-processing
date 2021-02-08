import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import math
PI: 3.141592653589793
start = -20
stop = 20
step=1

n1=np.linspace(start, stop, int((stop-start)/step))

x1=np.heaviside(n1,1)-np.heaviside(n1-3,1)+np.heaviside(n1-5,1)

style.use("ggplot")
plt.stem(n1,x1,label='plot1')
plt.xlabel('N-axis')
plt.ylabel('X-axis')
plt.legend()
plt.show()

x2_1=2*np.cos(2*n1*math.pi)

style.use("ggplot")
plt.stem(n1,x2_1,label='plot2_1')
plt.xlabel('N-axis')
plt.ylabel('X-axis')
plt.legend()
plt.show()

x2_2=2*np.cos(4*n1*math.pi)

style.use("ggplot")
plt.stem(n1,x2_2,label='plot2_2')
plt.xlabel('N-axis')
plt.ylabel('X-axis')
plt.legend()
plt.show()



x2_3=2*np.cos(6*n1*math.pi)

style.use("ggplot")
plt.stem(n1,x2_3,label='plot2_3')
plt.xlabel('N-axis')
plt.ylabel('X-axis')
plt.legend()
plt.show()


x3_1=2*np.cos(2*n1)
style.use("ggplot")
plt.stem(n1,x3_1,label='plot3_1')
plt.xlabel('N-axis')
plt.ylabel('X-axis')
plt.legend()
plt.show()

x3_2=2*np.cos(4*n1)
style.use("ggplot")
plt.stem(n1,x3_2,label='plot3_2')
plt.xlabel('N-axis')
plt.ylabel('X-axis')
plt.legend()
plt.show()

x3_3=2*np.cos(6*n1)

style.use("ggplot")
plt.stem(n1,x3_3,label='plot3_3')
plt.xlabel('N-axis')
plt.ylabel('X-axis')
plt.legend()
plt.show()


