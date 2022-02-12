import tkinter
from tkinter import Tk, BOTH, X, LEFT, RIGHT, Listbox, Canvas, Y, CENTER, TOP
from tkinter.ttk import Frame, Label, Entry, Button

PI = 3.14
width_frame = 500
height_frame = 500
center_x_frame = width_frame/2
center_y_frame = height_frame/2


class Figure:

    def square(self):
        pass

    def perimeter(self):
        pass

    def volume(self):
        pass

    def draw_figure(self):
        frame_draw_figure = Frame()

        frame_draw_figure.pack(fill=Y)

        canvas = Canvas(frame_draw_figure, bg='red', width=width_frame, height=2*height_frame/3)
        return canvas


class Circle(Figure):
    title = "Круг"

    def __init__(self, r):
        super().__init__()
        self.r = r
        print("I am borning")

    def area(self):
        return PI*self.r**2

    def perimeter(self):
        return 2*PI*self.r

    def draw_figure(self):
        canvas = super().draw_figure()
        canvas.create_oval(0.1*width_frame, 0.1*height_frame, 0.9*width_frame, 0.9*height_frame, outline="#000000", width=1)
        canvas.pack()


class Square(Figure):
    title = "Квадрат"

    def __init__(self, x):
        super().__init__()
        self.x = x

    def area(self):
        return self.x ** 2

    def perimeter(self):
        return 4 * self.x

    def draw_figure(self):
        canvas = super().draw_figure()
        canvas.create_rectangle(0.1 * width_frame, 0.1 * height_frame, 0.9 * width_frame, 0.9 * height_frame,
                           outline="#000000", width=1)
        canvas.pack()


class Rectangle(Square):
    title = "Прямоугольник"

    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2*(self.x + self.y)


class Triangle(Rectangle):
    title = "Треугольник"

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def perimeter(self):
        return self.x + self.y + self.z

    def area(self):
        p = self.perimeter()
        return (p*(p-self.x)*(p-self.y)*(p-self.z))**0.5
#
#
class Trapezoid:
    title = "Трапеция"


    @staticmethod
    def draw_figure():

        return 'Draw trap'
#
#
class Rhombus(Rectangle, Figure):
    title = "Ромб"

    def __init__(self, x, y):
        super().__init__(x, y)

    def area(self):
        return self.x*self.y

    def perimeter(self):
        return 4*self.x

    def draw_figure(self):
        canvas = Figure.draw_figure(self)
        canvas.create_rectangle(0.3 * width_frame, 0.3 * height_frame, 0.7 * width_frame, 0.7 * height_frame,
                                outline="#000000", width=1)
        canvas.create_line(0.5 * width_frame, 0.1 * height_frame, 0.2 * width_frame, 0.5 * height_frame,
                           0.5 * width_frame, 0.9 * height_frame, 0.9 * width_frame, 0.5 * height_frame,
                           0.5 * width_frame, 0.1 * height_frame)
        canvas.pack()


class Sphere(Circle):

    def __init__(self, r):
        super().__init__(r)

    def area(self):
        return 4*PI*self.r

    def volume(self):
        return (4/3)*self.r**3

    def draw_figure(self):
        canvas = super().draw_figure()
        canvas.create_oval(0.1*width_frame, 0.1*height_frame, 0.9*width_frame, 0.9*height_frame, outline="#000000", width=1)
        canvas.pack()

    title = "Сфера"


class Cube(Square, Figure):
    title = "Куб"

    def __init__(self, x):
        super().__init__(x)

    def area(self):
        return 6*self.x


    def perimeter(self):
        return 12*self.x

    def volume(self):
        return self.x**3

    def draw_figure(self):
        canvas = Figure.draw_figure(self)
        canvas.create_rectangle(0.3 * width_frame, 0.3 * height_frame, 0.7 * width_frame, 0.7 * height_frame,
                           outline="#000000", width=1)
        canvas.create_line(0.7 * width_frame, 0.7 * height_frame, 0.8 * width_frame, 0.5 * height_frame,
                           0.8 * width_frame, 0.1 * height_frame, 0.7 * width_frame, 0.3 * height_frame)
        canvas.create_line(0.3 * width_frame, 0.3 * height_frame, 0.4 * width_frame, 0.1 * height_frame,
                           0.8 * width_frame, 0.1 * height_frame)
        canvas.create_line(0.3 * width_frame, 0.7 * height_frame, 0.4 * width_frame, 0.5 * height_frame,
                           0.8 * width_frame, 0.5 * height_frame, dash=(10, 10))
        canvas.create_line(0.4 * width_frame, 0.5 * height_frame,
                           0.4 * width_frame, 0.1 * height_frame, dash=(10, 10))

        canvas.pack()
#
#
# class Parallelepiped(Rectangle):
#     title = "Параллелепипед"
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#     def area(self):
#         return 2*(self.x*self.y + self.x*self.z + self.y*self.z)
#
#     def volume(self):
#         return self.x*self.y*self.z
#
#     def perimeter(self):
#         return 4*(self.x+self.y+self.z)
#
#
# class Pyramid(Parallelepiped):
#     title = "Пирамида"
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#     def volume(self):
#         return (1/3)*self.x*self.y*self.z
#
#     def area(self):
#         return self.x*self.y + self.x * self.z + self.y*self.z


class Cylinder (Rectangle, Figure):
    title = "Цилиндр"

    def __init__(self, x, y):
        super().__init__(x, y)

    def area(self):
        return 2*PI*self.x*self.y

    def draw_figure(self):
        canvas = Figure.draw_figure(self)
        if self.x >= self.y:
            x = 0.8*width_frame
            y = self.y/self.x * (0.8*height_frame)
        else:
            y = 0.8 * height_frame
            x = self.x/self.y*(0.8 * width_frame)

        center_x_frame = width_frame/2
        center_y_frame = height_frame/2

        canvas.create_oval(
            center_x_frame - x//2, center_y_frame - y//2, center_x_frame + x//2, (center_y_frame - y//2) + 100,
        )
        canvas.create_oval(
            center_x_frame - x // 2, center_y_frame + y // 2, center_x_frame + x // 2, (center_y_frame + y//2) + 100,
        )
        canvas.create_line(center_x_frame - x//2, center_y_frame - y//2+50, center_x_frame - x//2, center_y_frame + y//2 + 50)
        canvas.create_line(center_x_frame + x//2, center_y_frame - y//2+50, center_x_frame + x//2, center_y_frame + y//2 + 50)

        canvas.pack()


class Cone(Cylinder, Figure):
    title = "Конус"

    def __init__(self, x, y):
        super().__init__(x, y)

    def area(self):
        return PI*self.x*(self.y**2+self.x**2)**0.5

    def volume(self):
        return (1/3)*PI*(self.x**2) * self.y

    def draw_figure(self):
        canvas = Figure.draw_figure(self)

        canvas = Figure.draw_figure(self)
        if self.x >= self.y:
            x = 0.8 * width_frame
            y = self.y / self.x * (0.8 * height_frame)
        else:
            y = 0.8 * height_frame
            x = self.x / self.y * (0.8 * width_frame)
        canvas.create_oval(
            center_x_frame - x // 2, center_y_frame + y // 2, center_x_frame + x // 2, (center_y_frame + y // 2) + 100,
        )
        canvas.create_line(center_x_frame - x // 2, center_y_frame + y // 2 + 50, center_x_frame,
                           center_y_frame - y // 2)
        canvas.create_line(center_x_frame + x // 2, center_y_frame + y // 2 + 50, center_x_frame,
                           center_y_frame - y // 2)

        canvas. pack()
        return 'draw Cone'


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        figures_with1_params = {"Круг": 'Circle.draw_figure()',
                   "Квадрат": 'Square.draw_figure()',
                   "Прямоугольник": 'Rectangle.draw_figure()',
                   "Треугольник": 'Triangle.draw_figure()',
                   "Трапеция": 'Trapezoid.draw_figure()',
                   "Ромб": 'Rhombus.draw_figure()',
                   "Сфера": 'Sphere.draw_figure()',
                   "Куб": 'Cube.draw_figure()',
                   "Параллелепипед": 'Parallelepiped.draw_figure()',
                   "Пирамида": 'Pyramid.draw_figure()',
                   "Цилиндр": 'Cylinder.draw_figure()',
                   "Конус": 'Cone.draw_figure()'}


        self.master.title("Геометрический калькулятор")
        self.pack(fill=BOTH, expand=1)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Выберите фигуру", width=20)
        lbl1.pack(side=LEFT, padx=5, pady=5)


        list_figures = Listbox(frame1)
        list_figures.pack(fill=X, pady=5, padx=5,)
        i = 0
        for figure in figures_with1_params.keys():
            list_figures.insert(i, figure)
            i += 1


        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Размеры фигуры", width=20)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2, width=20)
        entry2.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        def proverka():
            """!!!!!!!!!!!!!!!Переименовать"""

            # print(type(entry2.get()))
            # print('click', entry2.get())
            #
            # figure = Circle(int(entry2.get()))
            # square = figure.area()
            # perimetr = figure.perimeter()
            # lbl_answer = Label(text=f"{square}, {perimetr}", width=20)
            # lbl_answer.pack(side=LEFT, padx=5, pady=5)
            # figure.draw_figure()
            # parametrs = entry2.get()
            # # print(parametrs)
            # print(type(parametrs))


            # print(type(parametrs_list))
            # print(parametrs_list)
            parametrs_list = entry2.get().split()

            figure_number = int(list_figures.curselection()[0])
            print(figure_number)
            parametrs_list = tuple(map(int, parametrs_list))
            name_figure = list_figures.get(figure_number)


            if len(parametrs_list) == 1:

                print(figure_number)



                figures_with1_params = {"Круг": Circle(*parametrs_list),
                                        "Квадрат": Square(*parametrs_list),
                                        "Сфера": Sphere(*parametrs_list),
                                        "Куб": Cube(*parametrs_list),
                                        }

                figure = figures_with1_params[name_figure]
                square = figure.area()
                perimetr = figure.perimeter()
                lbl_answer = Label(text=f"Площадь фигуры - {square}, периметр фигуры - {perimetr}", width=200)
                lbl_answer.pack(side=TOP, padx=5, pady=5)
                figure.draw_figure()

            elif len(parametrs_list)==2:

                figures_with2_params = {"Прямоугольник": Rectangle(*parametrs_list),
                                        """"Трапеция": Trapezoid(*parametrs_list),"""
                                        "Ромб": Rhombus(*parametrs_list),
                                        "Цилиндр": Cylinder(*parametrs_list),
                                        "Конус": Cone(*parametrs_list)
                                        }


                figure = figures_with2_params[name_figure]
                square = figure.area()
                perimetr = figure.perimeter()
                lbl_answer = Label(text=f"Площадь фигуры - {square}, периметр фигуры - {perimetr}", width=200)
                lbl_answer.pack(side=TOP, padx=5, pady=5)
                figure.draw_figure()

            """
            
            ,
            ,
            "Параллелепипед": Parallelepiped(),
            "Пирамида": Pyramid(),
            "Цилиндр": Cylinder(),
            "Конус": Cone()"""

            # print(list_figures.get(int(list_figures.curselection()[0])))
            # a = list_figures.get(int(list_figures.curselection()[0]))
            # figure = figures_with1_params[a]
            # print(figure.draw_figure())



        calculate_button = Button(frame3, text="Посчитать")
        calculate_button.pack(side=RIGHT, padx=5, pady=5)
        calculate_button.config(command=proverka)
        # clear_button = Button(frame3, text="Очистить")
        # calculate_button.pack(side=RIGHT, padx=5, pady=5)
        # calculate_button.config(command=clear)




def main():
    root = Tk()
    root.geometry("1000x700+50+50")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
