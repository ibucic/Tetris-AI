class Grid:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def clone_grid(self):
        clone_grid = Grid(self.rows, self.columns)
        clone_grid.cells = [[self.cells[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return clone_grid

    def clear_lines(self):
        distance = 0
        for r in range(self.rows - 1, -1, -1):
            if self.is_line(r):
                distance += 1
                for c in range(self.columns):
                    self.cells[r][c] = 0
            elif distance > 0:
                for c in range(self.columns):
                    self.cells[r + distance][c] = self.cells[r][c]
                    self.cells[r][c] = 0
        return distance

    def is_line(self, row):
        for c in range(self.columns):
            if self.cells[row][c] == 0:
                return False
        return True

    def is_empty_row(self, row):
        for c in range(self.columns):
            if self.cells[row][c] != 0:
                return False
        return True

    def exceeded(self):
        return not self.is_empty_row(0) or not self.is_empty_row(1)

    def height(self):
        r = 0
        for _ in range(self.rows):
            if self.is_empty_row(r):
                return self.rows - r
            r += 1
        return self.rows - r

    def lines(self):
        count = 0
        for r in range(self.rows):
            if self.is_line(r):
                count += 1
        return count

    def holes(self):
        count = 0
        for c in range(self.columns):
            block = False
            for r in range(self.rows):
                if self.cells[r][c] != 0:
                    block = True
                elif self.cells[r][c] == 0 and block:
                    count += 1
        return count

    def blockades(self):
        count = 0
        for c in range(self.columns):
            hole = False
            for r in range(self.rows - 1. - 1, -1):
                if self.cells[r][c] == 0:
                    hole = True
                elif self.cells[r][c] != 0 and hole:
                    count += 1
        return count

    def aggregate_height(self):
        total = 0
        for c in range(self.columns):
            total += self.column_height(c)
        return total

    def bumpiness(self):
        total = 0
        for c in range(self.columns - 1):
            total += abs(self.column_height(c) - self.column_height(c + 1))
        return total

    def column_height(self, column):
        r = 0
        for _ in range(self.rows):
            if self.cells[r][column] == 0:
                return self.rows - r
            r += 1
        return self.rows - r

    def add_piece(self, piece):
        for row in range(len(piece.cells)):
            for column in range(len(piece.cells[row])):
                r = piece.row + row
                c = piece.column + column
                if piece.cells[row][column] != 0 and r >= 0:
                    self.cells[r][c] = piece.cells[row][column]

    def valid(self, piece):
        for row in range(len(piece.cells)):
            for column in range(len(piece.cells[row])):
                r = piece.row + row
                c = piece.column + column
                if piece.cells[row][column] != 0:
                    if r < 0 or r >= self.rows:
                        return False
                    elif c < 0 or c >= self.columns:
                        return False
                    elif self.cells[r][c] != 0:
                        return False
        return True
