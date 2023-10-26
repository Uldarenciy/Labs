import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x = [25.082, 22.106, 19.075, 16.08, 13.142, 10.196, 8.119, 5.914, 4.2476, 1.9656, 0.52, -25, -22.105, -19.34, -16.12, -13.25, -10.25, -8.123, -5.85]
y = [16, 15.37, 14.53, 13.47, 12.2, 10.59, 9.16, 7.19, 5.34, 2.37, 0.34, -16.7, -15.7, -14.83, -13.8, -12.37, -11.05, -9.36, -7.02] 

#yerr = [10, 21, 10, 9, 19, 15, 30, 9, 28, 9, 13, 13, 11, 9]
    

ax.set_xlabel(r"U, В", fontsize=12.5)
ax.set_ylabel(r"I, $\mu$А", fontsize=12.5)
ax.set_title("2 мА", fontsize=15)#название графика

t = np.polyfit(x, y, 1) #аппроксимация
f = np.poly1d(t)

ax.xaxis.set_minor_locator(plt.MultipleLocator(40)) #ticks
#ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

ax.scatter(x, y, linestyle="None", marker='o', color="b", label = "эксперименты") #график
ax.scatter(x, f(x), linestyle="-", marker='None', color="r", label = "Аппроксимация") #график

#plt.errorbar(x, y, yerr=yerr, fmt='None', ecolor='b')#кресты погрешностей на графике

plt.xlim(-26, 26) #пределы графика
plt.ylim(-26, 26)

ax.legend()
print(f)

x1 = x[2:]
y1 = y[2:]
avgx= mean(x1)
avgy=mean(y1)
x_2 =[0] * len(x1)
y_2=[0] * len(y1)
for i in range(len(x1)):
    x_2[i]=x1[i]**2
for i in range(len(x1)):
    y_2[i]=y1[i]**2
avgx2=mean(x_2)
avgy2=mean(y_2)
sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-(3.236)**2)/(len(x1)))**0.5
# print(sigma)#абсолютная погрешность
# print(sigma/(3.236))#относительная погрешность


fig.savefig("graph(2mA).png") #сохранение