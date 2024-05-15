import unittest

from main import Window
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        window = Window(800, 600)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, window)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[-1][-1].has_bottom_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols // 2][num_rows // 2].visited,
            False,
        )
        self.assertEqual(
            m1._cells[-1][-1].visited,
            False,
        )


if __name__ == "__main__":
    unittest.main()
