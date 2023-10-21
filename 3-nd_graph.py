import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x2 = [0, 0.21, 0.4, 0.57, 0.89, 1.16, 1.3, 1.52, 1.71, 1.9, 2.06, 2.27, 2.54, 2.72, 2.95, 3.06, 2.92, 2.57, 2.19, 1.71, 1.49, 0.9, 0.6, 0.35, 0.14, 0.12]
x = []
y2 = [1, 2, 4, 7, 19, 29, 38, 47, 59, 72, 83, 99, 119, 134, 150, 159, 152, 129, 100, 64, 50, 21, 11, 5, -2, -2]
y = []
for a in x2:
    x.append(((a * 292.8 + 6.553) ** 2) / 10e6)
for a in y2:
    y.append(a)


yerr = [10, 21, 10, 9, 19, 15, 30, 9, 28, 9, 13, 13, 11, 9]
    

ax.set_xlabel(r"$ B^2,  Тл^2$", fontsize=12.5)
ax.set_ylabel(r"$ \Delta P , \mu Н$", fontsize=12.5)
#ax.set_title("$r^2=f(m)$", fontsize=15)#название графика

t= np.polyfit(x, y, 1) #аппроксимация
f = np.poly1d(t)

ax.xaxis.set_minor_locator(plt.MultipleLocator(25)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(50))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

ax.plot(x, y, linestyle="None", marker='o', color="b", label = "эксперименты") #график
ax.plot(x, f(x), linestyle="-", marker='None', color="r", label = "Аппроксимация") #график

#plt.errorbar(x, y, yerr=yerr, fmt='None', ecolor='b')#кресты погрешностей на графике

#plt.xlim(0.8, 5.2)
#plt.ylim(7, 44)

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
sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-(2027)**2)/(len(x1)))**0.5
print(sigma)#абсолютная погрешность
print(sigma/(2027))#относительная погрешность


fig.savefig("3-rd_graph(for Wolfram).png") #сохранение