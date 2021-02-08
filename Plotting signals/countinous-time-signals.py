import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

start = -3
stop = 3
step = 0.001
t1 = np.linspace(start, stop, int((stop - start) / step))
x1 = np.exp(-3 * t1)
x2 = np.exp(-3 * t1) * np.heaviside(t1, 1)
x3 = (np.exp(-3 * t1) * np.heaviside(t1, 1)) + 2 * np.sin(t1 + 2)
temp = (np.exp(-1 * t1)) * (np.sin(t1) + np.cos(t1)) * np.heaviside(t1, 1)
x4 = np.where(t1 > 1, temp,
              (np.where(t1 < -1, 0, 1)))

# style.use("ggplot")
# plt.plot(t1,x1,color='red',label='plot1')
# plt.xlabel('T-axis')
# plt.ylabel('X-axis')
# plt.legend()
# plt.show()

style.use("ggplot")
f, plt_arr = plt.subplots(4, sharex='col')
plt_arr[0].plot(t1, x1, color='red')
plt_arr[0].set_title('plot1')
plt_arr[1].plot(t1, x2, color='blue')
plt_arr[1].set_title('plot2')
plt_arr[2].plot(t1, x3, color='green')
plt_arr[2].set_title('plot3')
plt_arr[3].plot(t1, x4, color='purple')
plt_arr[3].set_title('plot4')
plt.show()
