
from scipy.io import wavfile
import scipy.io
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from scipy.fftpack import fftfreq

#sample_1
sr, data = wavfile.read('sample_1.wav')
plt.plot(data , label='1 in t')
plt.legend()
plt.show()
FFT = fft(data)
plt.plot(FFT , label='sample_1' , color='red')
plt.legend()
plt.show()

code=[]

for i in range(300000, 300641, 10):
    if FFT[i]<0:
        code.append('0')

    if FFT[i]>=0:
        code.append('1')


new1 = ''.join(code[0:8])
new2 = ''.join(code[8:16])
new3 = ''.join(code[16:24])
new4 = ''.join(code[24:32])
new5 = ''.join(code[32:40])
new6 = ''.join(code[40:48])
new7 = ''.join(code[48:56])
new8 = ''.join(code[56:64])



print("sample1:")
print(chr(int(new1, 2)), end='')
print(chr(int(new2, 2)), end='')
print(chr(int(new3, 2)), end='')
print(chr(int(new4, 2)), end='')
print(chr(int(new5, 2)), end='')
print(chr(int(new6, 2)), end='')
print(chr(int(new7, 2)), end='')
print(chr(int(new8, 2)), end='')



#sample_2
sr, data = wavfile.read('sample_2.wav')
plt.plot(data , label='2 in t')
plt.legend()
plt.show()
FFT = fft(data)
plt.plot(FFT , label='sample_2' )
plt.legend()
plt.show()

code=[]

for i in range(300000, 300641, 10):
    if FFT[i]<0:
        code.append('0')

    if FFT[i]>=0:
        code.append('1')


new1 = ''.join(code[0:8])
new2 = ''.join(code[8:16])
new3 = ''.join(code[16:24])
new4 = ''.join(code[24:32])
new5 = ''.join(code[32:40])
new6 = ''.join(code[40:48])
new7 = ''.join(code[48:56])
new8 = ''.join(code[56:64])



print("sample2:")
print(chr(int(new1, 2)), end='')
print(chr(int(new2, 2)), end='')
print(chr(int(new3, 2)), end='')
print(chr(int(new4, 2)), end='')
print(chr(int(new5, 2)), end='')
print(chr(int(new6, 2)), end='')
print(chr(int(new7, 2)), end='')
print(chr(int(new8, 2)), end='')



#sample_3
sr, data = wavfile.read('sample_3.wav')
plt.plot(data , label='3 in t')
plt.legend()
plt.show()
FFT = fft(data)
plt.plot(FFT , label='sample_3' , color='red')
plt.legend()
plt.show()

code=[]

for i in range(300000, 300641, 10):
    if FFT[i]<0:
        code.append('0')

    if FFT[i]>=0:
        code.append('1')


new1 = ''.join(code[0:8])
new2 = ''.join(code[8:16])
new3 = ''.join(code[16:24])
new4 = ''.join(code[24:32])
new5 = ''.join(code[32:40])
new6 = ''.join(code[40:48])
new7 = ''.join(code[48:56])
new8 = ''.join(code[56:64])



print("sample3:")
print(chr(int(new1, 2)), end='')
print(chr(int(new2, 2)), end='')
print(chr(int(new3, 2)), end='')
print(chr(int(new4, 2)), end='')
print(chr(int(new5, 2)), end='')
print(chr(int(new6, 2)), end='')
print(chr(int(new7, 2)), end='')
print(chr(int(new8, 2)), end='')


#sample_4
sr, data = wavfile.read('sample_4.wav')
plt.plot(data , label='4 in t')
plt.legend()
plt.show()
FFT = fft(data)

plt.plot(FFT , label='sample_4' , color='red')
plt.legend()
plt.show()

code=[]

for i in range(300000, 300641, 10):
    if FFT[i]<0:
        code.append('0')

    if FFT[i]>=0:
        code.append('1')


new1 = ''.join(code[0:8])
new2 = ''.join(code[8:16])
new3 = ''.join(code[16:24])
new4 = ''.join(code[24:32])
new5 = ''.join(code[32:40])
new6 = ''.join(code[40:48])
new7 = ''.join(code[48:56])
new8 = ''.join(code[56:64])



print("sample4:")
print(chr(int(new1, 2)), end='')
print(chr(int(new2, 2)), end='')
print(chr(int(new3, 2)), end='')
print(chr(int(new4, 2)), end='')
print(chr(int(new5, 2)), end='')
print(chr(int(new6, 2)), end='')
print(chr(int(new7, 2)), end='')
print(chr(int(new8, 2)), end='')

#sample_5
sr, data = wavfile.read('sample_5.wav')
plt.plot(data , label='5 in t')
plt.legend()
plt.show()
FFT = fft(data)
plt.plot(FFT , label='sample_5' , color='red')
plt.legend()
plt.show()

code=[]

for i in range(300000, 300641, 10):
    if FFT[i]<0:
        code.append('0')

    if FFT[i]>=0:
        code.append('1')


new1 = ''.join(code[0:8])
new2 = ''.join(code[8:16])
new3 = ''.join(code[16:24])
new4 = ''.join(code[24:32])
new5 = ''.join(code[32:40])
new6 = ''.join(code[40:48])
new7 = ''.join(code[48:56])
new8 = ''.join(code[56:64])



print("sample5:")
print(chr(int(new1, 2)), end='')
print(chr(int(new2, 2)), end='')
print(chr(int(new3, 2)), end='')
print(chr(int(new4, 2)), end='')
print(chr(int(new5, 2)), end='')
print(chr(int(new6, 2)), end='')
print(chr(int(new7, 2)), end='')
print(chr(int(new8, 2)), end='')