from tkinter import ARC

width_frame = 300
height_frame = 300
center_x_frame = width_frame / 2
center_y_frame = height_frame / 2
width_line = 2
PI = 3.14


class Paint:
    @staticmethod
    def change_x_y_z_for_draw(x, y, z):
        if x > y and x > z:
            x = 0.7 * width_frame
            y = (y / x) * (0.7 * height_frame)
            z = (z / x) * (0.2 * height_frame)
        elif y > z and y > x:
            y = 0.7 * height_frame
            x = (x / y) * (0.7 * width_frame)
            z = (z / y) * (0.2 * height_frame)
        elif z > x and z > y:
            z = 0.2 * width_frame
            y = (y / z) * 0.7 * height_frame
            x = (x / z) * 0.7 * width_frame
        return x, y, z

        pass

    @staticmethod
    def change_x_y_for_draw(x, y):
        if x >= y:
            x = 0.6 * width_frame
            y = y / x * (0.6 * height_frame)
        else:
            y = 0.6 * height_frame
            x = x / y * (0.6 * width_frame)
        return x, y

    @staticmethod
    def change_x_for_draw():
        return 0.6 * width_frame

    def draw_figure(self, canvas_for_figure):
        pass


class Figure:

    def get_square(self):
        return "Отсутствует"

    def get_perimeter(self):
        return "Отсутствует"

    def get_volume(self):
        return "Отсутствует"

    @classmethod
    def cls_method(cls):
        return 'cls Method'


class Square(Figure, Paint):

    def __init__(self, x):
        super().__init__()
        self.x = x

    @staticmethod
    def get_name_figure():
        return "Квадрат"

    def get_area(self):
        return self.x ** 2

    def get_perimeter(self):
        return 4 * self.x

    def draw_figure(self, canvas_for_figure):
        Paint.draw_figure(self, canvas_for_figure)

        canvas_for_figure.create_rectangle(
            0.3 * width_frame, 0.3 * height_frame,
            0.7 * width_frame, 0.7 * height_frame,
            width=width_line
        )


class Circle(Square, Figure, Paint):

    def __init__(self, x):
        super().__init__(x)

    @staticmethod
    def name_figure():
        return "Круг"

    def get_area(self):
        return PI * self.x ** 2

    def get_perimeter(self):
        return 2 * PI * self.x

    def draw_figure(self, canvas_for_figure):
        Paint.draw_figure(self, canvas_for_figure)

        x = Paint.change_x_for_draw()
        canvas_for_figure.create_oval(center_x_frame - x / 2, center_y_frame - x / 2,
                                      center_x_frame + x / 2, center_y_frame + x / 2,
                                      width=width_line)


class Rectangle(Square, Figure):

    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    @staticmethod
    def get_name_figure():
        return "Прямоугольник"

    def get_area(self):
        return self.x * self.y

    def get_perimeter(self):
        return 2 * (self.x + self.y)

    def draw_figure(self, canvas_for_figure):
        Paint.draw_figure(self, canvas_for_figure)

        x, y = Paint.change_x_y_for_draw(self.x, self.y)

        canvas_for_figure.create_rectangle(
            center_x_frame - x / 2, center_y_frame - y / 2,
            center_x_frame + x / 2, center_y_frame + y / 2,
            width=width_line
        )


class Triangle(Rectangle):

    def __init__(self, x, y):
        super().__init__(x, y)

    @staticmethod
    def get_name_figure():
        return "Треугольник"

    def get_perimeter(self):
        return self.x + self.y + (self.x ** 2 + self.y ** 2) ** 0.5

    def get_area(self):
        return 0.5 * self.x * self.y

    def draw_figure(self, canvas_for_figure):
        Paint.draw_figure(self, canvas_for_figure)

        x, y = Paint.change_x_y_for_draw(self.x, self.y)

        canvas_for_figure.create_line(
            center_x_frame - x / 2, center_y_frame + y / 2,
            center_x_frame - x / 2, center_y_frame - y / 2,
            center_x_frame + x / 2, center_y_frame + y / 2,
            center_x_frame - x / 2, center_y_frame + y / 2,
            width=width_line
        )


class Trapezoid(Rectangle, Figure, Paint):
    """ x - нижняя грань трапеции
        y - высота
        z - верхняя грань трапеции"""

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    @staticmethod
    def get_name_figure():
        return "Трапеция"

    def get_area(self):
        return self.y * (self.x + self.z) / 2

    def get_perimetr(self):
        return self.x + self.z + 2 * ((((self.x - self.z) / 2) ** 2 + self.y ** 2) ** 0.5)

    def draw_figure(self, canvas_for_figure):
        Paint.draw_figure(self, canvas_for_figure)
        x, y, z = Paint.change_x_y_z_for_draw(self.x, self.y, self.z)

        canvas_for_figure.create_line(
            center_x_frame - x / 2, center_y_frame + y / 2,
            center_x_frame + x / 2, center_y_frame + y / 2,
            center_x_frame + x / 2 - z / 2, center_y_frame - y / 2,
            center_x_frame - x / 2 + z / 2, center_y_frame - y / 2,
            center_x_frame - x / 2, center_y_frame + y / 2,
            width=width_line
        )


class Rhombus(Rectangle, Figure, Paint):

    def __init__(self, x, y):
        super().__init__(x, y)

    @staticmethod
    def get_name_figure():
        return "Ромб"

    def get_area(self):
        return self.x * self.y

    def get_perimeter(self):
        return 4 * self.x

    def draw_figure(self, canvas_for_figure):
        Paint.draw_figure(self, canvas_for_figure)

        x, y = Paint.change_x_y_for_draw(self.x, self.y)

        canvas_for_figure.create_line(
            center_x_frame, center_y_frame - y / 2,
                            center_x_frame - x / 2, center_y_frame,
            center_x_frame, center_y_frame + y / 2,
                            center_x_frame + x / 2, center_y_frame,
            center_x_frame, center_y_frame - y / 2,
            width=width_line
        )


class Sphere(Circle, Figure, Paint):

    def __init__(self, x):
        super().__init__(x)

    @staticmethod
    def get_name_figure():
        return "Сфера"

    def get_perimeter(self):
        return Figure.get_perimeter(self)

    def get_area(self):
        return 4 * PI * self.x

    def get_volume(self):
        return (4 / 3) * self.x ** 3

    def draw_figure(self, canvas_for_figure):
        Paint.draw_figure(self, canvas_for_figure)
        Circle.draw_figure(self, canvas_for_figure)

        x = Paint.change_x_for_draw()

        canvas_for_figure.create_arc(
            center_x_frame - x / 2, center_y_frame - 20,
            center_x_frame + x / 2, center_y_frame + 20,
            start=180,
            extent=180, style=ARC,
            width=width_line
        )

        canvas_for_figure.create_arc(
            center_x_frame - x / 2, center_y_frame - 20,
            center_x_frame + x / 2, center_y_frame + 20,
            start=0,
            extent=180, style=ARC, dash=(10, 10)
        )


class Cube(Square, Figure, Paint):

    def __init__(self, x):
        super().__init__(x)

    @staticmethod
    def get_name_figure():
        return "Куб"

    def get_area(self):
        return 6 * self.x

    def get_perimeter(self):
        return 12 * self.x

    def get_volume(self):
        return self.x ** 3

    def draw_figure(self, canvas_for_figure):
        Paint.draw_figure(self, canvas_for_figure)
        Square.draw_figure(self, canvas_for_figure)

        canvas_for_figure.create_line(
            0.7 * width_frame, 0.7 * height_frame,
            0.8 * width_frame, 0.5 * height_frame,
            0.8 * width_frame, 0.1 * height_frame,
            0.7 * width_frame, 0.3 * height_frame,
            width=width_line
        )
        canvas_for_figure.create_line(
            0.3 * width_frame, 0.3 * height_frame,
            0.4 * width_frame, 0.1 * height_frame,
            0.8 * width_frame, 0.1 * height_frame,
            width=width_line
        )
        canvas_for_figure.create_line(
            0.3 * width_frame, 0.7 * height_frame,
            0.4 * width_frame, 0.5 * height_frame,
            0.8 * width_frame, 0.5 * height_frame,
            dash=(10, 10)
        )
        canvas_for_figure.create_line(
            0.4 * width_frame, 0.5 * height_frame,
            0.4 * width_frame, 0.1 * height_frame,
            dash=(10, 10)
        )


class Parallelepiped(Trapezoid, Figure, Paint):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def get_name_figure():
        return "Параллелепипед"

    def get_area(self):
        return 2 * (self.x * self.y + self.x * self.z + self.y * self.z)

    def get_volume(self):
        return self.x * self.y * self.z

    def get_perimeter(self):
        return 4 * (self.x + self.y + self.z)

    def draw_figure(self, canvas_for_figure):
        Paint.draw_figure(self, canvas_for_figure)
        x, y, z = Paint.change_x_y_z_for_draw(self.x, self.y, self.z)

        canvas_for_figure.create_line(
            center_x_frame - x / 2, center_y_frame - y / 2,
            center_x_frame + x / 2, center_y_frame - y / 2,
            center_x_frame + x / 2, center_y_frame + y / 2,
            center_x_frame - x / 2, center_y_frame + y / 2,
            center_x_frame - x / 2, center_y_frame - y / 2,
            width=width_line
        )
        canvas_for_figure.create_line(
            center_x_frame + x / 2, center_y_frame + y / 2,
            center_x_frame + x / 2 + z, center_y_frame + y / 2 - z,
            center_x_frame + x / 2 + z, center_y_frame - y / 2 - z,
            center_x_frame + x / 2, center_y_frame - y / 2,
            width=width_line
        )
        canvas_for_figure.create_line(
            center_x_frame - x / 2, center_y_frame - y / 2,
            center_x_frame - x / 2 + z, center_y_frame - y / 2 - z,
            center_x_frame + x / 2 + z, center_y_frame - y / 2 - z,
            width=width_line
        )
        canvas_for_figure.create_line(
            center_x_frame - x / 2, center_y_frame + y / 2,
            center_x_frame - x / 2 + z, center_y_frame + y / 2 - z,
            center_x_frame - x / 2 + z, center_y_frame - y / 2 - z,
            dash=(10, 10)
        )
        canvas_for_figure.create_line(
            center_x_frame - x / 2 + z, center_y_frame + y / 2 - z,
            center_x_frame + x / 2 + z, center_y_frame + y / 2 - z,
            dash=(10, 10),
        )


class Pyramid(Trapezoid, Figure, Paint):
    ''' x - сторона основания пирамиды
        y - сторона основания пирамиды
        z - высота пирамиды'''

    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    @staticmethod
    def get_name_figure():
        return "Пирамида"

    def get_volume(self):
        return (1 / 3) * self.x * self.y * self.z

    def get_area(self):
        return self.x * self.y + self.x * self.z + self.y * self.z

    def draw_figure(self, canvas_for_figure):
        Paint.draw_figure(self, canvas_for_figure)
        x, y, z = Paint.change_x_y_z_for_draw(self.x, self.y, self.z)

        canvas_for_figure.create_line(
            center_x_frame, center_y_frame - y / 2,
                            center_x_frame - x / 2, center_y_frame + y / 2,
                            center_x_frame + x / 2, center_y_frame + y / 2,
            center_x_frame, center_y_frame - y / 2,
            width=width_line
        )
        canvas_for_figure.create_line(
            center_x_frame + x / 2, center_y_frame + y / 2,
            center_x_frame + x / 2 + z, center_y_frame + y / 2 - z,
            center_x_frame, center_y_frame - y / 2,
            width=width_line
        )
        canvas_for_figure.create_line(
            center_x_frame - x / 2, center_y_frame + y / 2,
            center_x_frame - x / 2 + z, center_y_frame + y / 2 - z,
            center_x_frame, center_y_frame - y / 2, dash=(10, 10),
        )

        canvas_for_figure.create_line(
            center_x_frame - x / 2 + z, center_y_frame + y / 2 - z,
            center_x_frame + x / 2 + z, center_y_frame + y / 2 - z,
            dash=(10, 10)
        )


class Cylinder(Rectangle, Figure, Paint):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def get_name_figure():
        return "Цилиндр"

    def get_perimeter(self):
        return Figure.get_perimeter(self)

    def get_area(self):
        return 2 * PI * self.x * self.y

    def get_volume(self):
        return PI * self.x ** 2 * self.y

    def draw_figure(self, canvas_for_figure):
        Paint.draw_figure(self, canvas_for_figure)
        x, y = Paint.change_x_y_for_draw(self.x, self.y)

        canvas_for_figure.create_oval(
            center_x_frame - x // 2, center_y_frame - y // 2,
            center_x_frame + x // 2, (center_y_frame - y // 2) + 24,
            width=width_line
        )

        canvas_for_figure.create_arc(
            center_x_frame - x // 2, center_y_frame + y // 2,
            center_x_frame + x // 2, (center_y_frame + y // 2) + 24, start=180,
            extent=180, style=ARC,
            width=width_line
        )

        canvas_for_figure.create_line(
            center_x_frame - x // 2, center_y_frame - y // 2 + 12,
            center_x_frame - x // 2, center_y_frame + y // 2 + 12,
            width=width_line
        )
        canvas_for_figure.create_line(
            center_x_frame + x // 2, center_y_frame - y // 2 + 15,
            center_x_frame + x // 2, center_y_frame + y // 2 + 15,
            width=width_line
        )


class Cone(Rectangle, Figure, Paint):

    def __init__(self, x, y):
        super().__init__(x, y)

    @staticmethod
    def get_name_figure():
        return "Конус"

    def get_perimeter(self):
        return Figure.get_perimeter(self)

    def get_area(self):
        return PI * self.x * (self.y ** 2 + self.x ** 2) ** 0.5

    def get_volume(self):
        return (1 / 3) * PI * (self.x ** 2) * self.y

    def draw_figure(self, canvas_for_figure):
        Paint.draw_figure(self, canvas_for_figure)
        x, y = Paint.change_x_y_for_draw(self.x, self.y)

        canvas_for_figure.create_arc(
            center_x_frame - x // 2, center_y_frame + y // 2,
            center_x_frame + x // 2, (center_y_frame + y // 2) + 24,
            start=180,
            extent=180, style=ARC, width=width_line
        )

        canvas_for_figure.create_line(
            center_x_frame - x // 2, center_y_frame + y // 2 + 12,
            center_x_frame, center_y_frame - y // 2,
            width=width_line
        )
        canvas_for_figure.create_line(
            center_x_frame + x // 2, center_y_frame + y // 2 + 12,
            center_x_frame, center_y_frame - y // 2,
            width=width_line
        )
