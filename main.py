from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_1: Point, point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2

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
        self.width = width
        self.height = height
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


class Cell:
    def __init__(self, x1, y1, x2, y2, window: Window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._window = window

    def draw(self):
        if self.has_left_wall:
            self._window.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            )
        if self.has_right_wall:
            self._window.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            )
        if self.has_top_wall:
            self._window.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            )
        if self.has_bottom_wall:
            self._window.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            )

    def draw_move(self, to_cell, undo=False):
        fill_color = "gray"
        if undo == None:
            fill_color = "red"
        center_x1 = (self._x1 + self._x2) / 2
        center_y1 = (self._y1 + self._y2) / 2
        center_x2 = (to_cell._x1 + to_cell._x2) / 2
        center_y2 = (to_cell._y1 + to_cell._y2) / 2
        self._window.draw_line(
            Line(Point(center_x1, center_y1), Point(center_x2, center_y2)), fill_color
        )


def main():
    window = Window(800, 600)
    point_1 = Point(10, 50)
    point_2 = Point(100, 350)
    line_1 = Line(point_1, point_2)
    point_3 = Point(510, 150)
    point_4 = Point(123, 321)
    line_2 = Line(point_3, point_4)
    cell_1 = Cell(100, 100, 200, 200, window)
    cell_2 = Cell(350, 350, 550, 550, window)
    window.draw_line(line_1, "blue")
    window.draw_line(line_2, "red")
    cell_1.draw()
    cell_2.draw()
    cell_1.draw_move(cell_2)
    window.wait_for_close()


if __name__ == "__main__":
    main()
