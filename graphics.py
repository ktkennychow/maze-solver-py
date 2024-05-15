from tkinter import Tk, Canvas


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_1, point_2):
        self.point_1: Point = point_1
        self.point_2: Point = point_2

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.point_1.x,
            self.point_1.y,
            self.point_2.x,
            self.point_2.y,
            fill=fill_color,
            width=2,
        )


class Window:
    def __init__(self, width: float, height: float):
        self.width: float = width
        self.height: float = height
        self.root = Tk()
        self.root.title("aMAZ(E)ing")
        self.canvas = Canvas(height=height, width=width)
        self.canvas.pack()
        self.is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running == True:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line: Line, fill_color: str = "black"):
        line.draw(self.canvas, fill_color)
