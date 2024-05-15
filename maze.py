import random
from cell import Cell
from graphics import Window
import time


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window, seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._cells: list[list[Cell]] = []
        self._window: Window = window
        self._seed = seed
        if self._seed != None:
            self._seed = random.seed(seed)
        self._create_cells()

    def _create_cells(self):
        self._cells = [
            [Cell(self._window) for _ in range(self._num_rows)]
            for _ in range(self._num_cols)
        ]
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        for col in range(len(self._cells)):
            for row in range(len(self._cells[0])):
                self._draw_cell(col, row)

    def _draw_cell(self, i: int, j: int):
        cell_x1 = self._x1 + self._cell_size_x * i
        cell_y1 = self._y1 + self._cell_size_y * j
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_y
        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        self._window.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[len(self._cells) - 1][
            len(self._cells[0]) - 1
        ].has_bottom_wall = False

    def _break_walls_r(self, i: int, j: int):
        self._cells[i][j].visited = True
        #  i i i
        # j[][][]
        # j[][][]
        # j[][][]
        while True:
            possible_directions = []
            if 0 <= (i - 1):
                if self._cells[i - 1][j].visited == False:
                    possible_directions.append("left")
            if i + 1 <= self._num_cols - 1:
                if self._cells[i + 1][j].visited == False:
                    possible_directions.append("right")
            if 0 <= (j - 1):
                if self._cells[i][j - 1].visited == False:
                    possible_directions.append("up")
            if j + 1 <= self._num_rows - 1:
                if self._cells[i][j + 1].visited == False:
                    possible_directions.append("down")
            if len(possible_directions) == 0:
                return
            direction = random.choice(possible_directions)
            if direction == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
                self._break_walls_r(i - 1, j)
            if direction == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
                self._break_walls_r(i + 1, j)
            if direction == "up":
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
                self._break_walls_r(i, j - 1)
            if direction == "down":
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
                self._break_walls_r(i, j + 1)

    def _reset_cells_visited(self):
        for col in range(len(self._cells)):
            for row in range(len(self._cells[0])):
                self._cells[col][row].visited = False

    def solve(self):
        return self._solve_r(i=0, j=0)

    def _solve_r(self, i: int, j: int):
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[-1][-1]:
            return True
        # check left cell
        if 0 <= (i - 1):
            if self._cells[i][j].has_left_wall == False:
                if self._cells[i - 1][j].visited == False:
                    self._cells[i][j].draw_move(self._cells[i - 1][j])
                    next_move = self._solve_r(i=i - 1, j=j)
                    if next_move == True:
                        return True
                    else:
                        self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)
        # check right cell
        if i + 1 <= self._num_cols - 1:
            if self._cells[i][j].has_right_wall == False:
                if self._cells[i + 1][j].visited == False:
                    self._cells[i][j].draw_move(self._cells[i + 1][j])
                    next_move = self._solve_r(i=i + 1, j=j)
                    if next_move == True:
                        return True
                    else:
                        self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)
        # check up cell
        if 0 <= (j - 1):
            if self._cells[i][j].has_top_wall == False:
                if self._cells[i][j - 1].visited == False:
                    self._cells[i][j].draw_move(self._cells[i][j - 1])
                    next_move = self._solve_r(i=i, j=j - 1)
                    if next_move == True:
                        return True
                    else:
                        self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)
        # check down cell
        if j + 1 <= self._num_rows - 1:
            if self._cells[i][j].has_bottom_wall == False:
                if self._cells[i][j + 1].visited == False:
                    self._cells[i][j].draw_move(self._cells[i][j + 1])
                    next_move = self._solve_r(i=i, j=j + 1)
                    if next_move == True:
                        return True
                    else:
                        self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)
        return False
