import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x = [25, 23.073, 19.125, 15.966, 11.914, 9.922, 7.906, 6, 4.0883, 2.03, 0.5, -25, -23.07, -19.12, -15.98, -11.92, -9.89, -7.9, -6, -4.08]

y = [22, 21.26, 19.76, 18.5, 16.53, 15.27, 13.66, 11.64, 9.16, 5.76, 2.85, -23, -21.5, -20.57, -19.7, -17.1, -15.7, -13.79, -11.6, -9.35]

#yerr = [10, 21, 10, 9, 19, 15, 30, 9, 28, 9, 13, 13, 11, 9]
    

ax.set_xlabel(r"U, В", fontsize=12.5)
ax.set_ylabel(r"I, $\mu$А", fontsize=12.5)
ax.set_title("3 мА", fontsize=15)#название графика

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


fig.savefig("graph(3mA).png") #сохранение