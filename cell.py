from graphics import Line, Point, Window


class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._window: Window = window
        self.visited: bool = False

    def draw(self, x1, y1, x2, y2):
        if self._window == None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall == True:
            self._window.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        if self.has_right_wall == True:
            self._window.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        if self.has_top_wall == True:
            self._window.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        if self.has_bottom_wall == True:
            self._window.draw_line(Line(Point(x1, y2), Point(x2, y2)))

    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo == True:
            fill_color = "#444"
        center_x1 = (self._x1 + self._x2) / 2
        center_y1 = (self._y1 + self._y2) / 2
        center_x2 = (to_cell._x1 + to_cell._x2) / 2
        center_y2 = (to_cell._y1 + to_cell._y2) / 2
        self._window.draw_line(
            Line(Point(center_x1, center_y1), Point(center_x2, center_y2)), fill_color
        )
