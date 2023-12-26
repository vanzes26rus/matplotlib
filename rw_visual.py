import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_nambers = list(range(rw.num_points))
    plt.figure(figsize=(10, 6))
    # Удаление осей с диаграммы
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    plt.scatter(rw.x_values, rw.y_values, c=point_nambers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    # Выделение первой и последней точки.
    plt.scatter(0,0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)
    # Изменение размера диаграммы
    plt.show()
    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break