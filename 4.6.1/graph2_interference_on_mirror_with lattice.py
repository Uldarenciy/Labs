import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x = [0, 0.25, 0.5, 1, 1.4, 1.69, 1.89, 2.15, 2.35, 2.69, 2.95, 3.20, 3.40, 3.70, 4, 4.3, 4.62, 4.89, 5.15, 5.40, 5.64, 5.84, 6, 6.29, 6.48, 6.74, 7, 7.25, 7.40, 7.57, 7.71, 7.83, 7.99]


y = [76, 76, 76, 64, 58, 42, 36, 31, 30, 31, 30, 44, 49, 59, 74, 80, 76, 71, 67, 60, 50, 50, 44, 39, 39, 36, 40, 48, 54, 60, 77, 82, 87]
xerr = []
yerr = []
#Нахожденике погрешности в x и y {xerr и yerr}
for i in range(0, len(x)):
    xerr.append(0.01)         
for i in range(0, len(y)):
    yerr.append(1)
print(len(x), " ", len(y))
#yerr = [0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0010, 0.0000010, 0.0000010, 0.000001013]
#xerr = [10, 23, 23, 45, 12, 12, 11, 34, 56, 76, 12]
    

ax.set_xlabel(r"x, мм", fontsize=12.5)
ax.set_ylabel(r"I, мкВ", fontsize = 12.5)
ax.set_title("Интерференция на зеркале с решёткой", fontsize=15)#название графика

#t = np.polyfit(x, y, 2) #аппроксимация (3-ий параметр - степень полинома подгонки)
#f = np.poly1d(t)

ax.xaxis.set_minor_locator(plt.MultipleLocator(40)) #ticks
#ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

#ax.plot(x, y, linestyle="None", marker='o', color="b", label = "эксперименты") #график
#ax.plot(x, f(x), linestyle="-", marker='None', color="r", label = "Аппроксимация") #график

plt.errorbar(x, y, yerr=yerr, xerr=xerr, fmt='None', ecolor='b')#кресты погрешностей на графике

#plt.xlim(0.8, 5.2) #пределы графика
#plt.ylim(7, 44)

ax.legend()
#print(f)

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
sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-(7.117e-06)**2)/(len(x1)))**0.5
#print(sigma) #абсолютная погрешность
#print(sigma / (7.117e-06)) #относительная погрешность (делим на значение углового коэффициента)


fig.savefig("graph2_interference_on_mirror_with lattice.png") #сохранение
