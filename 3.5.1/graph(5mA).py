import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x = [25, 22.044, 19.004, 16.021, 13.128, 10.108, 8.16, 6.043, 4.16, 1.9887, 0.005, -25, -22.053, -19.02, -15.993, -13.028, -10.052, -8.074, -5.996, -4.1765, -2.0376, -0.5]

y = [0.036, 0.035, 0.033, 0.031, 0.029, 0.026, 0.024, 0.02, 0.016, 0.01, 0.4852, -0.043, -0.041, -0.038, -0.035, -0.032, -0.028, -0.024, -0.019, -0.013, -0.006, -0.00029]

#yerr = [10, 21, 10, 9, 19, 15, 30, 9, 28, 9, 13, 13, 11, 9]
    

ax.set_xlabel(r"U, В", fontsize=12.5)
ax.set_ylabel(r"I, мА", fontsize=12.5)
ax.set_title("5 мА", fontsize=15)#название графика

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

plt.xlim(-26, 26)
plt.ylim(-0.06, 0.06)

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


fig.savefig("graph(5mA).png") #сохранение