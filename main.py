
from tkinter import *
from tkinter.ttk import Frame, Label, Entry, Button

PI = 3.14


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        figures = ("Круг", "Квадрат", "Прямоугольник", "Треугольник", "Трапеция", "Ромб", "Сфера", "Куб",
                   "Параллелепипед", "Пирамида", "Цилиндр", "Конус"
                   )

        self.master.title("Геометрический калькулятор")
        self.pack(fill=BOTH, expand=1)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Выберите фигуру", width=20)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        list_figures = Listbox(frame1)
        list_figures.pack(fill=X, pady=5, padx=5)
        i = 0
        for figure in figures:
            list_figures.insert(i, figure)
            i += 1

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Размеры фигуры", width=20)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        size_figure = Entry(frame2, width=20)
        size_figure.pack(fill=X, side=LEFT, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        frame4 = Frame(self)
        frame4.pack(fill=X)

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

        lbl_description = Label(frame4, text=description, width=90)
        lbl_description.pack(side=LEFT)

        frame5 = Frame(self)
        frame5.pack(fill=X, expand=1)

        canvas_for_figure = Canvas(frame5)
        canvas_for_figure.pack()

        answer = StringVar()

        lbl_answer = Label(frame4,
                           textvariable=answer,
                           width=200)
        lbl_answer.config(font=("Courier", 16, "italic"))
        lbl_answer.pack()

        def perform_calculations():

            width_frame = 300
            height_frame = 300
            center_x_frame = width_frame / 2
            center_y_frame = height_frame / 2

            width_line = 2

            class Figure:

                def square(self):
                    return "Отсутствует"

                def perimeter(self):
                    return "Отсутствует"

                def volume(self):
                    return "Отсутствует"

                def draw_figure(self):
                    pass

            class Square(Figure):

                def __init__(self, x):
                    super().__init__()
                    self.x = x

                @staticmethod
                def name_figure():
                    return "Квадрат"

                def area(self):
                    return self.x ** 2

                def perimeter(self):
                    return 4 * self.x

                def draw_figure(self):
                    canvas_for_figure.create_rectangle(
                        0.3 * width_frame, 0.3 * height_frame,
                        0.7 * width_frame, 0.7 * height_frame,
                        width=width_line
                    )

            class Circle(Figure):

                def __init__(self, r):
                    super().__init__()
                    self.r = r

                @staticmethod
                def name_figure():
                    return "Круг"

                def area(self):
                    return PI * self.r ** 2

                def perimeter(self):
                    return 2 * PI * self.r

                def draw_figure(self):
                    x = 0.6 * width_frame
                    canvas_for_figure.create_oval(center_x_frame - x/2, center_y_frame - x/2,
                                                  center_x_frame + x/2, center_y_frame + x/2,
                                                  width=width_line)

            class Rectangle(Square, Figure):

                def __init__(self, x, y):
                    super().__init__(x)
                    self.y = y

                @staticmethod
                def name_figure():
                    return "Прямоугольник"

                def area(self):
                    return self.x * self.y

                def perimeter(self):
                    return 2 * (self.x + self.y)

                def draw_figure(self):
                    canvas = Figure.draw_figure(self)
                    if self.x >= self.y:
                        x = 0.6 * width_frame
                        y = self.y / self.x * (0.6 * height_frame)
                    else:
                        y = 0.6 * height_frame
                        x = self.x / self.y * (0.6 * width_frame)
                    canvas_for_figure.create_rectangle(
                        center_x_frame - x / 2, center_y_frame - y / 2,
                        center_x_frame + x / 2, center_y_frame + y / 2,
                        width=width_line
                    )


            class Triangle(Rectangle):

                def __init__(self, x, y):
                    super().__init__(x, y)

                @staticmethod
                def name_figure():
                    return "Треугольник"

                def perimeter(self):
                    return self.x + self.y + (self.x ** 2 + self.y ** 2) ** 0.5

                def area(self):
                    return 0.5 * self.x * self.y

                def draw_figure(self):
                    if self.x >= self.y:
                        x = 0.7 * width_frame
                        y = self.y / self.x * (0.7 * height_frame)
                    else:
                        y = 0.7 * height_frame
                        x = self.x / self.y * (0.7 * width_frame)

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
                def name_figure():
                    return "Трапеция"

                def area(self):
                    return self.y*(self.x+self.z)/2

                def perimetr(self):
                    return self.x + self.z + 2*((((self.x - self.z)/2)**2 + self.y**2)**0.5)


                def draw_figure(self):
                    if self.x > self.y and self.x > self.z:
                        x = 0.7 * width_frame
                        y = (self.y / self.x) * (0.7 * height_frame)
                        z = (self.z / self.x) * (0.7 * height_frame)
                    elif self.y > self.z and self.y > self.x:
                        y = 0.7 * height_frame
                        x = (self.x / self.y) * (0.7 * width_frame)
                        z = (self.z / self.y) * (0.7 * height_frame)
                    elif self.z > self.x and self.z > self.y:
                        z = 0.7 * width_frame
                        y = (self.y / self.z) * 0.7 * height_frame
                        x = (self.x / self.z) * 0.7 * width_frame

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
                def name_figure():
                    return "Ромб"

                def area(self):
                    return self.x * self.y

                def perimeter(self):
                    return 4 * self.x

                def draw_figure(self):
                    if self.x >= self.y:
                        x = 0.7 * width_frame
                        y = self.y / self.x * (0.7 * height_frame)
                    else:
                        y = 0.7 * height_frame
                        x = self.x / self.y * (0.7 * width_frame)
                    canvas_for_figure.create_line(
                        center_x_frame, center_y_frame - y / 2,
                                        center_x_frame - x / 2, center_y_frame,
                        center_x_frame, center_y_frame + y / 2,
                                        center_x_frame + x / 2, center_y_frame,
                        center_x_frame, center_y_frame - y / 2,
                        width=width_line
                    )

            class Sphere(Circle, Figure):

                def __init__(self, r):
                    super().__init__(r)

                @staticmethod
                def name_figure():
                    return "Сфера"

                def perimeter(self):
                    return Figure.perimeter(self)

                def area(self):
                    return 4 * PI * self.r

                def volume(self):
                    return (4 / 3) * self.r ** 3

                def draw_figure(self):
                    Circle.draw_figure(self)
                    x = 0.6 * width_frame

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
                def name_figure():
                    return "Куб"

                def area(self):
                    return 6 * self.x

                def perimeter(self):
                    return 12 * self.x

                def volume(self):
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

            class Parallelepiped(Rectangle, Figure):

                def __init__(self, x, y, z):
                    self.x = x
                    self.y = y
                    self.z = z

                @staticmethod
                def name_figure():
                    return "Параллелепипед"

                def area(self):
                    return 2 * (self.x * self.y + self.x * self.z + self.y * self.z)

                def volume(self):
                    return self.x * self.y * self.z

                def perimeter(self):
                    return 4 * (self.x + self.y + self.z)

                def draw_figure(self):
                    if self.x > self.y and self.x > self.z:
                        x = 0.7 * width_frame - self.z
                        y = (self.y / self.x) * (0.8 * height_frame) - self.z
                        z = (self.z / self.x) * (0.2 * (height_frame ** 2 + width_frame ** 2) ** 0.5)
                    elif self.y > self.z and self.y > self.x:
                        y = 0.7 * height_frame - self.z
                        x = (self.x / self.y) * (0.8 * width_frame) - self.z
                        z = (self.z / self.y) * (0.2 * (height_frame ** 2 + width_frame ** 2) ** 0.5)
                    elif self.z > self.x and self.z > self.y:
                        z = (0.2 * (height_frame ** 2 + width_frame ** 2) ** 0.5) - self.z
                        y = (self.y / self.z) * 0.8 * height_frame - self.z
                        x = (self.x / self.z) * (0.8 * width_frame)


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

            class Pyramid(Parallelepiped, Figure):
                ''' x - сторона основания пирамиды
                    y - сторона основания пирамиды
                    z - высота пирамиды'''

                def __init__(self, x, y, z):
                    super().__init__(x, y, z)

                @staticmethod
                def name_figure():
                    return "Пирамида"

                def volume(self):
                    return (1 / 3) * self.x * self.y * self.z

                def area(self):
                    return self.x * self.y + self.x * self.z + self.y * self.z

                def draw_figure(self):
                    if self.x > self.y and self.x > self.z:
                        x = 0.7 * width_frame - self.z
                        y = (self.y / self.x) * (0.8 * height_frame) - self.z
                        z = (self.z / self.x) * (0.2 * (height_frame ** 2 + width_frame ** 2) ** 0.5)
                    elif self.y > self.z and self.y > self.x:
                        y = 0.7 * height_frame - self.z
                        x = (self.x / self.y) * (0.8 * width_frame) - self.z
                        z = (self.z / self.y) * (0.2 * (height_frame ** 2 + width_frame ** 2) ** 0.5)
                    elif self.z > self.x and self.z > self.y:
                        z = (0.2 * (height_frame ** 2 + width_frame ** 2) ** 0.5) - self.z
                        y = (self.y / self.z) * 0.8 * height_frame - self.z
                        x = (self.x / self.z) * (0.8 * width_frame)


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
                def name_figure():
                    return "Цилиндр"

                def perimeter(self):
                    return Figure.perimeter(self)

                def area(self):
                    return 2 * PI * self.x * self.y

                def volume(self):
                    return PI*self.x**2 * self.y

                def draw_figure(self):
                    if self.x >= self.y:
                        x = 0.5 * width_frame
                        y = self.y / self.x * (0.6 * height_frame)
                    else:
                        y = 0.5 * height_frame
                        x = self.x / self.y * (0.6 * width_frame)

                    canvas_for_figure.create_oval(
                        center_x_frame - x // 2, center_y_frame - y // 2,
                        center_x_frame + x // 2, (center_y_frame - y // 2) + 30,
                        width=width_line
                    )

                    canvas_for_figure.create_arc(
                        center_x_frame - x // 2, center_y_frame + y // 2,
                        center_x_frame + x // 2, (center_y_frame + y // 2) + 30, start=180,
                        extent=180, style=ARC,
                        width=width_line
                    )

                    canvas_for_figure.create_line(
                          center_x_frame - x // 2, center_y_frame - y // 2 + 15,
                          center_x_frame - x // 2, center_y_frame + y // 2 + 15,
                        width=width_line
                                                  )
                    canvas_for_figure.create_line(
                          center_x_frame + x // 2, center_y_frame - y // 2 + 15,
                          center_x_frame + x // 2, center_y_frame + y // 2 + 15,
                        width=width_line
                                                  )

            class Cone(Cylinder, Figure):

                def __init__(self, x, y):
                    super().__init__(x, y)

                @staticmethod
                def name_figure():
                    return "Конус"

                def perimeter(self):
                    return Figure.perimeter(self)

                def area(self):
                    return PI * self.x * (self.y ** 2 + self.x ** 2) ** 0.5

                def volume(self):
                    return (1 / 3) * PI * (self.x ** 2) * self.y

                def draw_figure(self):
                    if self.x >= self.y:
                        x = 0.4 * width_frame
                        y = self.y / self.x * (0.5 * height_frame)
                    else:
                        y = 0.4 * height_frame
                        x = self.x / self.y * (0.5 * width_frame)
                    canvas_for_figure.create_arc(
                        center_x_frame - x // 2, center_y_frame + y // 2,
                        center_x_frame + x // 2, (center_y_frame + y // 2) + 50,
                        start=180,
                        extent=180, style=ARC, width=width_line
                    )

                    canvas_for_figure.create_line(
                        center_x_frame - x // 2, center_y_frame + y // 2 + 25,
                        center_x_frame, center_y_frame - y // 2,
                        width=width_line
                    )
                    canvas_for_figure.create_line(
                        center_x_frame + x // 2, center_y_frame + y // 2 + 25,
                        center_x_frame, center_y_frame - y // 2,
                        width=width_line
                    )

            canvas_for_figure.delete("all")

            parametrs_list = size_figure.get().split()
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

            square = figure.area()
            perimetr = figure.perimeter()
            volume = figure.volume()

            answer.set(f"Площадь фигуры - {square}\nПериметр фигуры - {perimetr}\nОбъем фигуры - {volume}")

            figure.draw_figure()

            lbl_answer.pack(side=BOTTOM)

        calculate_button = Button(frame3, text="Посчитать")
        calculate_button.pack(side=RIGHT, padx=5, pady=5)
        calculate_button.config(command=perform_calculations)


def main():
    root = Tk()
    # root.geometry("1000x1000+50+50")
    app = Example()
    root.update_idletasks()
    root.mainloop()


if __name__ == '__main__':
    main()
