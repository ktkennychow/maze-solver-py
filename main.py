from tkinter import Tk, Canvas

from cell import Cell
from graphics import Line, Point, Window
from maze import Maze


def main():
    start_x = 50
    start_y = 50
    win_size_x = 800
    win_size_y = 600
    cell_size_x = 50
    cell_size_y = 50
    # uniform paddings in all 4 sides
    num_rows = (600 - start_x * 2) // cell_size_y
    num_cols = (800 - start_y * 2) // cell_size_x
    window = Window(win_size_x, win_size_y)
    maze_1 = Maze(
        start_x, start_y, num_rows, num_cols, cell_size_x, cell_size_y, window
    )
    maze_1.solve()
    window.wait_for_close()


if __name__ == "__main__":
    main()
