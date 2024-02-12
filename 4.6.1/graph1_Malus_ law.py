import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
from math import cos

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

#I - интенсивность
x_0 = [0, 20, 40, 60, 80, 100]
y = [56, 55, 45, 27, 6, 15]
#угол
x = []
#cos^2(угол)
for i in range(0, len(x_0)):
    x.append(cos(x_0[i]) * cos(x_0[i]))


xerr = []
yerr = []

#Нахожденике погрешности в x и y {xerr и yerr}
for i in range(0, len(x)):
    xerr.append(1 / 100)    

for i in range(0, len(y)):
    yerr.append(1)
               
#yerr = [0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0000010, 0.0000010, 0.000001013]
#xerr = [10, 23, 23, 45, 12, 12, 11, 34, 56, 76, 12]
    

ax.set_xlabel(r"$cos^2(\alpha$)", fontsize=12.5)
ax.set_ylabel(r"$I$, мкВ", fontsize=12.5)
ax.set_title(r"I = f($cos^2$($\alpha$)) зависимость уровня сигнала I от угла поворота $\alpha$ приёмной антенны относительно луча", fontsize=15)#название графика

t = np.polyfit(x, y, 1) #аппроксимация (3-ий параметр - степень полинома подгонки)
f = np.poly1d(t)

ax.xaxis.set_minor_locator(plt.MultipleLocator(40)) #ticks
#ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

ax.plot(x, y, linestyle="None", marker='o', color="b", label = "эксперименты") #график
ax.plot(x, f(x), linestyle="-", marker='None', color="r", label = "Аппроксимация") #график

plt.errorbar(x, y, yerr=yerr, xerr=xerr, fmt='None', ecolor='b')#кресты погрешностей на графике

#plt.xlim(0.8, 5.2) #пределы графика
#plt.ylim(7, 44)

ax.legend()
print(f)

x1 = x
y1 = y
avgx= mean(x1)
avgy=mean(y1)
x_2 = [0] * len(x1)
y_2 = [0] * len(y1)
for i in range(len(x1)):
    x_2[i]=x1[i]**2

for i in range(len(x1)):
    y_2[i]=y1[i]**2

avgx2=mean(x_2)
avgy2=mean(y_2)                           #значение углового коэффициента
sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-(11.75)**2)/(len(x1)))**0.5
#print(sigma) #абсолютная погрешность
#print(sigma / (11.75)) #относительная погрешность (делим на значение углового коэффициента)


fig.savefig("graph1_Malus_ law.png") #сохранение
