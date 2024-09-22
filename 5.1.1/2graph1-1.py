import matplotlib.pyplot as plt 
import numpy as np 

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

ax.set_xlabel(r"V, В", fontsize=12.5)
ax.set_ylabel(r"V1, В", fontsize=12.5)
#teta=1380
v1_1380 = np.array([28,22,17,13,9,0,92,116,131,155,174,195,214]) / 1000
v_1380 = np.array([-147,-190,-228,-262,-295,-373,159,262,320,420,493,567,638]) / 1000 
        
#teta = 2200 
v1_2200 = np.array([191,105,58,33,17,5]) / 1000 
v_2200 = np.array([0,-138,-243,-322,-413,-669]) / 1000 

#teta = 2350 
v1_2350 = np.array([417,28,103,33,7,0]) / 1000
v_2350 = np.array([0,-113,-224,-316,-406,-460]) / 1000 

#teta = 2450 
v1_2450 = np.array([370,137,45,1,0]) / 1000 
v_2450 = np.array([0,-128,-212,-311,-409]) / 1000 

#teta = 2530 
v1_2530 = np.array([262,73,32,19,11,7,6,4]) / 1000
v_2530 = np.array([0,-109,-163,-200,-243,-301,-326,-494]) / 1000

# plt.plot(v_1380, v1_1380)
# plt.plot(v_2200, v1_2200)
# plt.plot(v_2350, v1_2350)
# plt.plot(v_2450, v1_2450)
# plt.plot(v_2530, v1_2530)

#plt.ylabel('V1') 
#plt.xlabel('V')
plt.title('Зависимость фототока от напряжения')

t1 = np.polyfit(v_1380, v1_1380, 2) #аппроксимация
f1 = np.poly1d(t1)
t2 = np.polyfit(v_2200, v1_2200, 2) #аппроксимация
f2 = np.poly1d(t2)
t3 = np.polyfit(v_2350, v1_2350, 2) #аппроксимация
f3 = np.poly1d(t3)
t4 = np.polyfit(v_2450, v1_2450, 2) #аппроксимация
f4 = np.poly1d(t4)
t5 = np.polyfit(v_2530, v1_2530, 2) #аппроксимация
f5 = np.poly1d(t1)


ax.xaxis.set_minor_locator(plt.MultipleLocator(40)) #ticks
#ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

ax.plot(v_1380, v1_1380, linestyle="None", marker='o', color="b", label = "эксперименты") #график
ax.plot(v_1380, f1(v_1380), linestyle="-", marker='None', color="r", label = "Аппроксимация") #график
ax.plot(v_2200, v1_2200, linestyle="None", marker='o', color="b", label = "эксперименты") #график
ax.plot(v_2200, f2(v_2200), linestyle="-", marker='None', color="r", label = "Аппроксимация") #график
ax.plot(v_2350, v1_2350, linestyle="None", marker='o', color="b", label = "эксперименты") #график
ax.plot(v_2350, f3(v_2350), linestyle="-", marker='None', color="r", label = "Аппроксимация") #график
ax.plot(v_2450, v1_2450, linestyle="None", marker='o', color="b", label = "эксперименты") #график
ax.plot(v_2450, f4(v_2450), linestyle="-", marker='None', color="r", label = "Аппроксимация") #график
ax.plot(v_2530, v1_2530, linestyle="None", marker='o', color="b", label = "эксперименты") #график
ax.plot(v_2530, f5(v_2530), linestyle="-", marker='None', color="r", label = "Аппроксимация") #график
print(f1)
print(f2)
print(f3)
print(f4)
print(f5)

# for i in range(len(x1)):
#     x_2[i]=x1[i]**2
# for i in range(len(x1)):
#     y_2[i]=y1[i]**2
# avgx2=mean(x_2)
# avgy2=mean(y_2)
# sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-(3.236)**2)/(len(x1)))**0.5
#t = np.polyfit(deg, wave, 2)
#f = np.poly1d(t)
#plt.plot(deg, f(deg))
#plt.errorbar(v_1380, v1_1380, xerr = v_1380 * 0.01, fmt='o-', ecolor='red')
#plt.errorbar(v_2200, v1_2200, xerr = v_2200 * 0.01, fmt='o-', ecolor='red')
#plt.errorbar(v_2350, v1_2350, xerr = v_2350 * 0.01, fmt='o-', ecolor='red')
#plt.errorbar(v_2450, v1_2450, xerr = v_2450 * 0.01, fmt='o-', ecolor='red')
#plt.errorbar(v_2530, v1_2530, xerr = v_2530 * 0.01, fmt='o-', ecolor='red')

plt.show() 

