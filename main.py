from tkinter import Tk, Text, BOTH, X, N, LEFT, RIGHT, Listbox
from tkinter.ttk import Frame, Label, Entry, Button

PI = 3,14

class Figure:
    def __init__(self):
        pass

    def square(self):
        pass

    def perimeter(self):
        pass

    def volume(self):
        pass

    def draw_figure(self):
        pass

class Circle(Figure):
    title = "Круг"

    def __init__(self, radius):
        super().__init__()
        print("I am borning")
        self.radius = radius

    def area(self):
        return PI*self.radius**2

    def perimeter(self):
        return 2*PI*self.radius

    @staticmethod
    def draw_figure():
        return 'Draw Circle'


class Square(Figure):
    title = "Квадрат"

    def __init__(self, x):
        super().__init__()
        self.x = x

    def area(self):
        return self.x**2

    def perimeter(self):
        return 4*self.x

    @staticmethod
    def draw_figure():

        pass


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



class Trapezoid:
    title = "Трапеция"
    pass


class Rhombus(Rectangle):
    title = "Ромб"

    def __init__(self, x, y):
        super().__init__(x, y)

    def area(self):
        return self.x*self.y

    def perimeter(self):
        return 4*self.x

class Sphere(Circle):

    def __init__(self, radius):
        super().__init__(radius)

    def area(self):
        return 4*PI*self.radius

    def volume(self):
        return (4/3)*self.radius**3

    title = "Сфера"
    pass


class Cube(Square):
    title = "Куб"

    def __init__(self):
        super().__init__(x)

    def area(self):
        return 6*self.x


    def perimeter(self):
        return 12*self.x

    def volume(self):
        return self.x**3

class Parallelepiped(Rectangle):
    title = "Параллелепипед"

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def area(self):
        return 2*(self.x*self.y + self.x*self.z + self.y*self.z)

    def volume(self):
        return self.x*self.y*self.z

    def perimeter(self):
        return 4*(self.x+self.y+self.z)


class Pyramid(Parallelepiped):
    title = "Пирамида"
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def volume(self):
        return (1/3)*self.x*self.y*self.z

    def area(self):
        return self.x*self.y + self.x * self.z + self.y*self.z


class Cylinder (Rectangle):
    title = "Цилиндр"

    def __init__(self, x, y):
        super().__init__(x, y)

    def area(self):
        return 2*PI*self.x*self.y + 2*


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

        figures = {"Круг": Circle(),
                              "Квадрат": Square(),
                              "Прямоугольник": Rectangle(),
                              "Треугольник": Triangle(),
                              "Трапеция": Trapezoid(),
                              "Ромб": Rhombus(),
                              "Сфера": Sphere(),
                              "Куб": Cube(),
                              "Параллелепипед": Parallelepiped(),
                              "Пирамида": Pyramid(),
                              "Цилиндр": Cylinder(),
                              "Конус": Cone()}

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
            figure = figures[a]
            print(figure.draw_figure())

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


