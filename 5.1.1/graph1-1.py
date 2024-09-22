import matplotlib.pyplot as plt 
import numpy as np 

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

wave = np.array([7032, 6929, 6717, 6678, 6599, 6533, 6507, 6402, 6383, 6334, 6305, 6267, 6217, 6164, 6143, 6096, 6030, 5976, 5882, 5852, 5401, 5341, 5331])

deg  = np.array([2566, 2498, 2488, 2464, 2428, 2392, 2384, 2364, 2352, 2336, 2316, 2292, 2284, 2264, 2254, 2234, 2204, 2194, 2164, 2148, 2102, 1882, 1838])

t = np.polyfit(deg, wave, 2)
f = np.poly1d(t)
ax.set_xlabel(r'λ, Å', fontsize=12.5)
ax.set_ylabel(r"θ, °", fontsize=12.5)
#plt.plot(deg, f(deg))
ax.xaxis.set_minor_locator(plt.MultipleLocator(400)) #ticks
#ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
plt.tick_params(axis='both', which='major', direction='inout', length=100)
plt.tick_params(axis='both', which='minor', direction='inout', length=150)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

ax.plot(wave, deg, linestyle="None", marker='o', color="b", label = "эксперименты") #график
ax.plot(wave, f(wave), linestyle="-", marker='None', color="r", label = "Аппроксимация") #график

#plt.plot(deg, wave)
#plt.ylabel('λ, Å') #Подпись для оси х
#plt.xlabel('θ, °') #Подпись для оси y
#plt.title('Градуировка монохроматора (зависимость длины волны от угла)')
ax.set_title('Градуировка монохроматора (зависимость длины волны от угла)', fontsize=7)#название графика
ax.plot(wave, deg, linestyle="None", marker='o', color="b", label = "эксперименты") #график
ax.plot(wave, f(wave), linestyle="-", marker='None', color="r", label = "Аппроксимация") #график

#plt.errorbar(deg, wave, xerr = deg * 0.01, fmt='o-', ecolor='red')
plt.show() 

fig.savefig("Градуировка монохроматора") #сохранение