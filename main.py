
from tkinter import *
from tkinter.ttk import Frame, Label, Entry, Button

PI = 3.14


class GraphicInterface(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        figures = ("Круг", "Квадрат", "Прямоугольник", "Треугольник", "Трапеция", "Ромб", "Сфера", "Куб",
                   "Параллелепипед", "Пирамида", "Цилиндр", "Конус"
                   )

        self.master.title("Геометрический калькулятор")
        self.pack(fill=BOTH, expand=1)

        frame_row_1 = Frame(self)
        frame_row_1.pack(fill=X)

        text_row_1 = Label(frame_row_1, text="Выберите фигуру", width=20)
        text_row_1.pack(side=LEFT, padx=5, pady=5)

        list_figures = Listbox(frame_row_1)
        list_figures.pack(fill=X, pady=5, padx=5)
        i = 0
        for figure in figures:
            list_figures.insert(i, figure)
            i += 1

        frame_row_2 = Frame(self)
        frame_row_2.pack(fill=X)

        text_row_2 = Label(frame_row_2, text="Размеры фигуры", width=20)
        text_row_2.pack(side=LEFT, padx=5, pady=5)

        figure_sizes = Entry(frame_row_2, width=20)
        figure_sizes.pack(fill=X, side=LEFT, padx=5, expand=True)

        frame_row_3 = Frame(self)
        frame_row_3.pack(fill=X)

        frame_row_4 = Frame(self)
        frame_row_4.pack(fill=X)

        description = """ Выберите фигуру и далее введите через пробел параметры фигуры
                     Круг - 1 параметр (радиус)
                     Квадрат - 1 параметр (сторона)
                     Куб - 1 параметр (сторона)
                     Сфера - 1 параметр (радиус)
                     Прямоугольник - 2 параметра (стороны)
                     Конус - 2 параметра (радиус и высота)
                     Цилиндр - 2 параметра (радиус и высота
                     Ромб - 2 параметра (стороны диагоналей)
                     Треугольник - 2 параметра (длины катетов)
                     Трапеция - 3 параметра (нижнее верхнее основание, высота)
                     Параллелепипед - 3 параметра (длины сторон)
                     Пирамида - 3 параметра (длины основания и высота)
                     """

        text_description = Label(frame_row_4, text=description, width=90)
        text_description.pack(side=LEFT)

        frame_for_draw_figure = Frame(self)
        frame_for_draw_figure.pack(fill=X, expand=1)

        canvas_for_figure = Canvas(frame_for_draw_figure)
        canvas_for_figure.pack()

        p_s_v_figure = StringVar()

        text_psv_figure = Label(frame_row_4,
                           textvariable=p_s_v_figure,
                           width=200)
        text_psv_figure.config(font=("Courier", 16, "italic"))
        text_psv_figure.pack()

        def perform_calculations():

            width_frame = 300
            height_frame = 300
            center_x_frame = width_frame / 2
            center_y_frame = height_frame / 2
            width_line = 2

            class Figure:
                
                def get_square(self):
                    return "Отсутствует"

                def get_perimeter(self):
                    return "Отсутствует"

                def get_volume(self):
                    return "Отсутствует"

                def draw_figure(self):
                    pass

                @classmethod
                def cls_method(cls):
                    return 'cls Method'

            class Square(Figure):

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

                def change_x_for_draw(self):
                    return 0.6 * width_frame

                def draw_figure(self):
                    canvas_for_figure.create_rectangle(
                        0.3 * width_frame, 0.3 * height_frame,
                        0.7 * width_frame, 0.7 * height_frame,
                        width=width_line
                    )

            class Circle(Square, Figure):

                def __init__(self, x):
                    super().__init__(x)
                    # self.x = x

                @staticmethod
                def name_figure():
                    return "Круг"

                def get_area(self):
                    return PI * self.x ** 2

                def get_perimeter(self):
                    return 2 * PI * self.x




                def draw_figure(self):
                    x = Square.change_x_for_draw(self)
                    canvas_for_figure.create_oval(center_x_frame - x/2, center_y_frame - x/2,
                                                  center_x_frame + x/2, center_y_frame + x/2,
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

                def change_x_y_for_draw(self):
                    if self.x >= self.y:
                        x = 0.6 * width_frame
                        y = self.y / self.x * (0.6 * height_frame)
                    else:
                        y = 0.6 * height_frame
                        x = self.x / self.y * (0.6 * width_frame)
                    return x, y


                def draw_figure(self):
                    x, y = Rectangle.change_x_y_for_draw(self)

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

                def draw_figure(self):
                    x, y = Rectangle.change_x_y_for_draw(self)

                    canvas_for_figure.create_line(
                                       center_x_frame - x / 2, center_y_frame + y / 2,
                                       center_x_frame - x / 2, center_y_frame - y / 2,
                                       center_x_frame + x / 2, center_y_frame + y / 2,
                                       center_x_frame - x / 2, center_y_frame + y / 2,
                                       width=width_line
                                       )

            class Trapezoid(Rectangle, Figure):

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
                    return self.y*(self.x+self.z)/2

                def get_perimetr(self):
                    return self.x + self.z + 2*((((self.x - self.z)/2)**2 + self.y**2)**0.5)

                def change_x_y_z_for_draw(self):
                    if self.x > self.y and self.x > self.z:
                        x = 0.7 * width_frame
                        y = (self.y / self.x) * (0.7 * height_frame)
                        z = (self.z / self.x) * (0.2 * height_frame)
                    elif self.y > self.z and self.y > self.x:
                        y = 0.7 * height_frame
                        x = (self.x / self.y) * (0.7 * width_frame)
                        z = (self.z / self.y) * (0.2 * height_frame)
                    elif self.z > self.x and self.z > self.y:
                        z = 0.2 * width_frame
                        y = (self.y / self.z) * 0.7 * height_frame
                        x = (self.x / self.z) * 0.7 * width_frame
                    return x, y, z

                def draw_figure(self):
                    x, y, z = Trapezoid.change_x_y_z_for_draw(self)

                    canvas_for_figure.create_line(
                        center_x_frame - x / 2, center_y_frame + y / 2,
                        center_x_frame + x / 2, center_y_frame + y / 2,
                        center_x_frame + x / 2 - z / 2, center_y_frame - y / 2,
                        center_x_frame - x / 2 + z / 2, center_y_frame - y / 2,
                        center_x_frame - x / 2, center_y_frame + y / 2,
                        width=width_line
                    )

            class Rhombus(Rectangle, Figure):

                def __init__(self, x, y):
                    super().__init__(x, y)

                @staticmethod
                def get_name_figure():
                    return "Ромб"

                def get_area(self):
                    return self.x * self.y

                def get_perimeter(self):
                    return 4 * self.x

                def draw_figure(self):
                    x, y = Rectangle.change_x_y_for_draw(self)

                    canvas_for_figure.create_line(
                        center_x_frame, center_y_frame - y / 2,
                                        center_x_frame - x / 2, center_y_frame,
                        center_x_frame, center_y_frame + y / 2,
                                        center_x_frame + x / 2, center_y_frame,
                        center_x_frame, center_y_frame - y / 2,
                        width=width_line
                    )

            class Sphere(Circle, Figure):

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

                def draw_figure(self):
                    Circle.draw_figure(self)
                    x = Square.change_x_for_draw(self)

                    canvas_for_figure.create_arc(
                        center_x_frame - x/2, center_y_frame - 20,
                        center_x_frame + x/2, center_y_frame + 20,
                        start=180,
                        extent=180, style=ARC,
                        width=width_line
                    )

                    canvas_for_figure.create_arc(
                        center_x_frame - x / 2, center_y_frame - 20,
                        center_x_frame + x / 2, center_y_frame + 20,
                        start=0,
                        extent=180, style=ARC, dash=(10,10)
                    )

            class Cube(Square, Figure):

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

                def draw_figure(self):
                    Square.draw_figure(self)

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

            class Parallelepiped(Trapezoid, Figure):

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

                def draw_figure(self):
                    x, y, z = Trapezoid.change_x_y_z_for_draw(self)

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

            class Pyramid(Trapezoid, Figure):
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

                def draw_figure(self):
                    x, y, z = Trapezoid.change_x_y_z_for_draw(self)


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

            class Cylinder(Rectangle, Figure):

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
                    return PI*self.x**2 * self.y

                def draw_figure(self):
                    x, y = Rectangle.change_x_y_for_draw(self)

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

            class Cone(Rectangle, Figure):

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

                def draw_figure(self):
                    x, y = Rectangle.change_x_y_for_draw(self)

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

            canvas_for_figure.delete("all")

            parametrs_list = figure_sizes.get().split()
            parametrs_list = tuple(map(int, parametrs_list))

            for a in parametrs_list:
                if a <= 0:
                    raise Exception("Значения должны быть больше 0")

            figure_number = int(list_figures.curselection()[0])

            name_figure = list_figures.get(figure_number)

            if len(parametrs_list) == 1:
                figures_with1_params = {"Круг": Circle(*parametrs_list),
                                        "Квадрат": Square(*parametrs_list),
                                        "Сфера": Sphere(*parametrs_list),
                                        "Куб": Cube(*parametrs_list),
                                        }
                figure = figures_with1_params[name_figure]

            elif len(parametrs_list) == 2:
                figures_with2_params = {"Прямоугольник": Rectangle(*parametrs_list),
                                        "Ромб": Rhombus(*parametrs_list),
                                        "Цилиндр": Cylinder(*parametrs_list),
                                        "Конус": Cone(*parametrs_list),
                                        "Треугольник": Triangle(*parametrs_list)
                                        }
                figure = figures_with2_params[name_figure]
            elif len(parametrs_list) == 3:
                figures_with3_params = {"Параллелепипед": Parallelepiped(*parametrs_list),
                                        "Трапеция": Trapezoid(*parametrs_list),
                                        "Пирамида": Pyramid(*parametrs_list)
                                        }
                figure = figures_with3_params[name_figure]

            square = figure.get_area()
            perimetr = figure.get_perimeter()
            volume = figure.get_volume()

            p_s_v_figure.set(f"Площадь фигуры - {square}\nПериметр фигуры - {perimetr}\nОбъем фигуры - {volume}")

            figure.draw_figure()

            text_psv_figure.pack(side=BOTTOM)

        calculate_button = Button(frame_row_3, text="Посчитать")
        calculate_button.pack(side=RIGHT, padx=5, pady=5)
        calculate_button.config(command=perform_calculations)


def main():
    root = Tk()
    app = GraphicInterface()
    root.update_idletasks()
    root.mainloop()


if __name__ == '__main__':
    main()
