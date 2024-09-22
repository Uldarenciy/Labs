import matplotlib.pyplot as plt 
import numpy as np 

wave = np.array([7032, 6929, 6717, 6678, 6599, 6533, 6507, 6402, 6383, 6334, 6305, 6267, 6217, 6164, 6143, 6096, 6030, 5976, 5882, 5852, 5401, 5341, 5331])

deg  = np.array([2566, 2498, 2488, 2464, 2428, 2392, 2384, 2364, 2352, 2336, 2316, 2292, 2284, 2264, 2254, 2234, 2204, 2194, 2164, 2148, 2102, 1882, 1838])

t = np.polyfit(deg, wave, 2)
f = np.poly1d(t)
plt.plot(deg, f(deg))

plt.plot(deg, wave)
plt.ylabel('λ, Å') #Подпись для оси х
plt.xlabel('θ, °') #Подпись для оси y
plt.title('Градуировка монохроматора (зависимость длины волны от угла)')

plt.errorbar(deg, wave, xerr = deg * 0.01, fmt='o-', ecolor='red')
plt.show() 


