from models import *
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

            figure.draw_figure(canvas_for_figure)

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
