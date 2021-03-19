import random
import math


class Piece:
    def __init__(self, cells):
        self.cells = cells
        self.dimension = len(self.cells)
        self.color = None
        self.row = 0
        self.column = 0

    def clone_piece(self):
        clone_cells = [[self.cells[i][j] for j in range(self.dimension)] for i in range(self.dimension)]
        clone = Piece(clone_cells)
        clone.row = self.row
        clone.column = self.column
        clone.color = self.color
        return clone

    def can_move_left(self, grid):
        for row in range(len(self.cells)):
            for column in range(len(self.cells[row])):
                r = self.row + row
                c = self.column + column - 1
                if self.cells[row][column] != 0:
                    if c < 0 or grid.cells[r][c] != 0:
                        return False
        return True

    def can_move_right(self, grid):
        for row in range(len(self.cells)):
            for column in range(len(self.cells[row])):
                r = self.row + row
                c = self.column + column + 1
                if self.cells[row][column] != 0:
                    if c > grid.columns - 1 or grid.cells[r][c] != 0:
                        return False
        return True

    def can_move_down(self, grid):
        for row in range(len(self.cells)):
            for column in range(len(self.cells[row])):
                r = self.row + row + 1
                c = self.column + column
                if self.cells[row][column] != 0 and r >= 0:
                    if not (r < grid.rows and grid.cells[r][c] == 0):
                        return False
        return True

    def move_left(self, grid):
        if not self.can_move_left(grid):
            return False
        self.column -= 1
        return True

    def move_right(self, grid):
        if not self.can_move_right(grid):
            return False
        self.column += 1
        return True

    def move_down(self, grid):
        if not self.can_move_down(grid):
            return False
        self.row += 1
        return True

    def rotate_cells(self):
        clone_cells = [[self.cells[i][j] for j in range(self.dimension)] for i in range(self.dimension)]
        if len(self.cells) == 2:
            clone_cells[0][0] = self.cells[1][0]
            clone_cells[0][1] = self.cells[0][0]
            clone_cells[1][0] = self.cells[1][1]
            clone_cells[1][1] = self.cells[0][1]
        elif len(self.cells) == 3:
            clone_cells[0][0] = self.cells[2][0]
            clone_cells[0][1] = self.cells[1][0]
            clone_cells[0][2] = self.cells[0][0]
            clone_cells[1][0] = self.cells[2][1]
            clone_cells[1][1] = self.cells[1][1]
            clone_cells[1][2] = self.cells[0][1]
            clone_cells[2][0] = self.cells[2][2]
            clone_cells[2][1] = self.cells[1][2]
            clone_cells[2][2] = self.cells[0][2]
        elif len(self.cells) == 4:
            clone_cells[0][0] = self.cells[3][0]
            clone_cells[0][1] = self.cells[2][0]
            clone_cells[0][2] = self.cells[1][0]
            clone_cells[0][3] = self.cells[0][0]
            clone_cells[1][0] = self.cells[3][1]
            clone_cells[1][1] = self.cells[2][1]
            clone_cells[1][2] = self.cells[1][1]
            clone_cells[1][3] = self.cells[0][1]
            clone_cells[2][0] = self.cells[3][2]
            clone_cells[2][1] = self.cells[2][2]
            clone_cells[2][2] = self.cells[1][2]
            clone_cells[2][3] = self.cells[0][2]
            clone_cells[3][0] = self.cells[3][3]
            clone_cells[3][1] = self.cells[2][3]
            clone_cells[3][2] = self.cells[1][3]
            clone_cells[3][3] = self.cells[0][3]

        self.cells = [[clone_cells[i][j] for j in range(len(clone_cells[i]))] for i in range(len(clone_cells))]

    def compute_rotate_offset(self, grid):
        clone = self.clone_piece()
        clone.rotate_cells()
        if grid.valid(clone):
            return [clone.row - self.row, clone.column - self.column]

        initial_row = clone.row
        initial_column = clone.column

        for i in range(clone.dimension - 1):
            clone.column = initial_column + i
            if grid.valid(clone):
                return [clone.row - self.row, clone.column - self.column]
            for j in range(clone.dimension - 1):
                clone.row = initial_row - j
                if grid.valid(clone):
                    return [clone.row - self.row, clone.column - self.column]
            clone.row = initial_row
        clone.column = initial_column

        for i in range(clone.dimension - 1):
            clone.column = initial_column - i
            if grid.valid(clone):
                return [clone.row - self.row, clone.column - self.column]
            for j in range(clone.dimension - 1):
                clone.row = initial_row - j
                if grid.valid(clone):
                    return [clone.row - self.row, clone.column - self.column]
            clone.row = initial_row
        clone.column = initial_column

        return None

    def rotate(self, grid):
        offset = self.compute_rotate_offset(grid)
        if offset is not None:
            self.rotate_cells()
            self.row += offset[0]
            self.column += offset[1]


def next_piece():
    pieces = [[[1, 1],  # O
               [1, 1]],
              [[2, 0, 0],  # J
               [2, 2, 2],
               [0, 0, 0]],
              [[0, 0, 3],  # L
               [3, 3, 3],
               [0, 0, 0]],
              [[4, 4, 0],  # Z
               [0, 4, 4],
               [0, 0, 0]],
              [[0, 5, 5],  # S
               [5, 5, 0],
               [0, 0, 0]],
              [[0, 6, 0],  # T
               [6, 6, 6],
               [0, 0, 0]],
              [[0, 0, 0, 0],  # I
               [7, 7, 7, 7],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]]
    colors = [(255, 239, 43), (0, 100, 200), (247, 167, 0), (220, 0, 0), (0, 230, 50), (155, 0, 190), (0, 201, 223)]
    random_id = random.randint(0, len(pieces) - 1)
    piece = Piece(pieces[random_id])
    piece.column = math.floor((10 - piece.dimension) / 2)
    piece.color = colors[random_id]
    return piece
