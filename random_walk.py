from random import choice

class RandomWalk():
    """Класс для случайных блужданий."""
    def __init__(self, num_points=5000):
        """Инициализирует атрибуты блуждания."""
        self.num_points = num_points
        # Все блуждания начинаются с точки (0,0).
        self.x_values = [0]
        self.y_values = [0]
        self.get_step()


    def get_step(self):
        while len(self.y_values) < self.num_points:
            # Определение направления и длины перемещения
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_distance * x_direction

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_distance * y_direction

            if x_step == 0 and y_step == 0:
                continue
            # Выяесление следующих значений x и y.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.y_values.append(next_y)
            self.x_values.append(next_x)

    def fill_walk(self):
        # Определение направления и длины перемещения
        x_step = self.get_step()
        y_step = self.get_step()



