import matplotlib.pyplot as plt
import numpy as np

# Создание фигуры и осей
fig, ax = plt.subplots(figsize=(16, 10), dpi=400)

# Установка подписей осей
ax.set_xlabel(r"V, В", fontsize=12.5)
ax.set_ylabel(r"√I, А", fontsize=12.5)

# Данные для разных углов
v1_1380_0 = np.array([28, 22, 17, 13, 9, 0, 92, 116, 131, 155, 174, 195, 214]) / 1000
v_1380 = np.array([-147, -190, -228, -262, -295, -373, 159, 262, 320, 420, 493, 567, 638]) / 1000
v1_1380 = np.sqrt(v1_1380_0)

v1_2200_0 = np.array([191, 105, 58, 33, 17, 5]) / 1000
v_2200 = np.array([0, -138, -243, -322, -413, -669]) / 1000
v1_2200 = np.sqrt(v1_2200_0)

v1_2350_0 = np.array([417, 28, 103, 33, 7, 0]) / 1000
v_2350 = np.array([0, -113, -224, -316, -406, -460]) / 1000
v1_2350 = np.sqrt(v1_2350_0)

v1_2450_0 = np.array([370, 137, 45, 1, 0]) / 1000
v_2450 = np.array([0, -128, -212, -311, -409]) / 1000
v1_2450 = np.sqrt(v1_2450_0)

v1_2530_0 = np.array([262, 73, 32, 19, 11, 7, 6, 4]) / 1000
v_2530 = np.array([0, -109, -163, -200, -243, -301, -326, -494]) / 1000
v1_2530 = np.sqrt(v1_2530_0)

# Аппроксимации (полиномы 2-й степени)
t1 = np.polyfit(v_1380, v1_1380, 2)
f1 = np.poly1d(t1)

t2 = np.polyfit(v_2200, v1_2200, 2)
f2 = np.poly1d(t2)

t3 = np.polyfit(v_2350, v1_2350, 2)
f3 = np.poly1d(t3)

t4 = np.polyfit(v_2450, v1_2450, 2)
f4 = np.poly1d(t4)

t5 = np.polyfit(v_2530, v1_2530, 2)
f5 = np.poly1d(t5)

# Настройка осей и сетки
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.05))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-')
ax.grid(which='minor', linestyle='--')

# Построение графиков данных и аппроксимаций разными цветами
colors = ['r', 'g', 'b', 'c', 'm']  # Массив цветов для каждой аппроксимации

# Функция для добавления крестов
def add_crosses(x, y, x_err, y_err, color):
    ax.errorbar(x, y, xerr=x_err, yerr=y_err, fmt='None', color=color, capsize=5)

# Добавление данных с крестами
add_crosses(v_1380, v1_1380, 0.02 * np.abs(v_1380), 0.02 * np.abs(v1_1380), colors[0])
ax.plot(v_1380, v1_1380, linestyle="None", marker='o', color=colors[0], label="Эксперименты 1380 Ангстрем")
ax.plot(np.linspace(min(v_1380), max(v_1380), 500), f1(np.linspace(min(v_1380), max(v_1380), 500)), linestyle="-", color=colors[0], label="Аппроксимация 1380 Ангстрем")

add_crosses(v_2200, v1_2200, 0.02 * np.abs(v_2200), 0.02 * np.abs(v1_2200), colors[1])
ax.plot(v_2200, v1_2200, linestyle="None", marker='o', color=colors[1], label="Эксперименты 2200 Ангстрем")
ax.plot(np.linspace(min(v_2200), max(v_2200), 500), f2(np.linspace(min(v_2200), max(v_2200), 500)), linestyle="-", color=colors[1], label="Аппроксимация 2200 Ангстрем")

add_crosses(v_2350, v1_2350, 0.02 * np.abs(v_2350), 0.02 * np.abs(v1_2350), colors[2])
ax.plot(v_2350, v1_2350, linestyle="None", marker='o', color=colors[2], label="Эксперименты 2350 Ангстрем")
ax.plot(np.linspace(min(v_2350), max(v_2350), 500), f3(np.linspace(min(v_2350), max(v_2350), 500)), linestyle="-", color=colors[2], label="Аппроксимация 2350 Ангстрем")

add_crosses(v_2450, v1_2450, 0.02 * np.abs(v_2450), 0.02 * np.abs(v1_2450), colors[3])
ax.plot(v_2450, v1_2450, linestyle="None", marker='o', color=colors[3], label="Эксперименты 2450 Ангстрем")
ax.plot(np.linspace(min(v_2450), max(v_2450), 500), f4(np.linspace(min(v_2450), max(v_2450), 500)), linestyle="-", color=colors[3], label="Аппроксимация 2450 Ангстрем")

add_crosses(v_2530, v1_2530, 0.02 * np.abs(v_2530), 0.02 * np.abs(v1_2530), colors[4])
ax.plot(v_2530, v1_2530, linestyle="None", marker='o', color=colors[4], label="Эксперименты 2530 Ангстрем")
ax.plot(np.linspace(min(v_2530), max(v_2530), 500), f5(np.linspace(min(v_2530), max(v_2530), 500)), linestyle="-", color=colors[4], label="Аппроксимация 2530 Ангстрем")

# Добавление легенды с уменьшенным шрифтом, расположенной сверху справа
ax.legend(fontsize=3, loc='upper left', markerscale=0.1)

# Установка заголовка
plt.title('Фототок')

# Отображение графика
plt.show()
