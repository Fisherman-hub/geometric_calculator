from tkinter import Tk, Text, BOTH, X, N, LEFT, RIGHT, Listbox
from tkinter.ttk import Frame, Label, Entry, Button


class Figure:
    pass


class Circle(Figure):
    title = "Круг"

    @staticmethod
    def draw_figure():
        return 'Draw Circle'


class Square:
    title = "Квадрат"

    @staticmethod
    def draw_figure():

        pass


class Rectangle:
    title = "Прямоугольник"
    pass


class Triangle:
    title = "Треугольник"
    pass


class Trapezoid:
    title = "Трапеция"
    pass


class Rhombus:
    title = "Ромб"
    pass


class Sphere:
    title = "Сфера"
    pass


class Cube:
    title = "Куб"
    pass


class Parallelepiped:
    title = "Параллелепипед"
    pass


class Pyramid:
    title = "Пирамида"
    pass


class Cylinder:
    title = "Цилиндр"
    pass


class Cone:
    title = "Конус"
    pass


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Геометрический калькулятор")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        figures = {"Круг": Circle.draw_figure(),
                              "Квадрат": "",
                              "Прямоугольник": "",
                              "Треугольник": "",
                              "Трапеция": "",
                              "Ромб": "",
                              "Сфера": "",
                              "Куб": "",
                              "Параллелепипед": "",
                              "Пирамида": "",
                              "Цилиндр": "",
                              "Конус": ""}

        lbl1 = Label(frame1, text="Выберите фигуру", width=20)
        lbl1.pack(side=LEFT, padx=5, pady=5)


        list_figures = Listbox(frame1)
        list_figures.pack(fill=X, pady=5, padx=5,)
        i = 0
        for figure in figures.keys():
            list_figures.insert(i, figure)
            i += 1


        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Автор", width=20)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, expand=True)


        calculate_button = Button(self, text="Посчитать")
        calculate_button.pack(side=RIGHT, padx=5, pady=5)

        def proverka():
            print(list_figures.get(int(list_figures.curselection()[0])))
            a = list_figures.get(int(list_figures.curselection()[0]))
            print(figures[a])

        calculate_button.config(command=proverka)



def main():
    root = Tk()
    root.geometry("1000x700+50+50")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()




def set_difficulty(value, difficulty):
    # Do the job here !
    pass


