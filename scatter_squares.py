import matplotlib.pyplot as plt

# построение линии на граффике
import_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# Изменение ширины линии диаграммы
plt.plot(import_values, squares, linewidth=5)
# Назначение имени диаграммы, и размера ширифта
plt.title("Square Numbers", fontsize=24)
# название по оси X
plt.xlabel("Value", fontsize=14)
# название по оси Y
plt.ylabel("Square of Value", fontsize=14)
# оформление дилений на граффике
plt.tick_params(axis='both', labelsize=14)
# вывод изображения граффика
plt.show()

# Построение точек на граффике
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=200)
# s задает размер точкек
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# назнаечение размера ширифта делений на осях
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()

# Автоматическое вычесление данных

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values,cmap=plt.cm.Reds, edgecolors='none', s=40)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)


plt.show()

x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]

plt.plot(x_values, y_values, linewidth=7)
plt.title("Cubic Numbers", fontsize=30)
plt.xlabel("Nambers", fontsize=15)
plt.ylabel("Cubic", fontsize=20)
plt.tick_params(labelsize=14)
plt.show()

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
print(y_values)

plt.scatter(x_values, y_values, linewidth=7, c=y_values, cmap=plt.cm.Reds, edgecolors='none', s=40 )
plt.title("Cubic Numbers", fontsize=30)
plt.xlabel("Nambers", fontsize=15)
plt.ylabel("Cubic", fontsize=20)
plt.tick_params(labelsize=14)
plt.axis([0, 5000, 0, 135000000000])
plt.show()

