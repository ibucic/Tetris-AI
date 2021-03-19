import pygame
import Grid
import Piece
import AI

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
GRID_WIDTH = 10
GRID_HEIGHT = 22
BLOCK_SIZE = 35


class Game:

    def __init__(self):
        self.grid = Grid.Grid(GRID_HEIGHT, GRID_WIDTH)
        self.current_piece = Piece.next_piece()
        self.ai = AI.AI([0.510066, 0.760666, 0.35663, 0.184483])
        self.working_pieces = [Piece.next_piece(), Piece.next_piece()]
        self.working_piece = self.working_pieces[0]
        self.font_score = pygame.font.SysFont('comicsans', 60, True, False)
        self.is_ai_active = True
        self.score = 0

    def draw_grid(self, window, vertical_offset=0):
        colors = [(255, 239, 43), (0, 100, 200), (247, 167, 0), (220, 0, 0), (0, 230, 50), (155, 0, 190), (0, 201, 223)]
        w, h = pygame.display.get_surface().get_size()
        translation = [(w - GRID_WIDTH * BLOCK_SIZE) // 2, (h - (GRID_HEIGHT - 2) * BLOCK_SIZE) // 2]

        pygame.draw.rect(window, (255, 255, 255), (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.draw.rect(window, (0, 0, 0),
                         (translation[0], translation[1], GRID_WIDTH * BLOCK_SIZE, (GRID_HEIGHT - 2) * BLOCK_SIZE), 3)

        for r in range(2, self.grid.rows):
            for c in range(self.grid.columns):
                if self.grid.cells[r][c] != 0:
                    pygame.draw.rect(window, colors[self.grid.cells[r][c] - 1], (
                        translation[0] + BLOCK_SIZE * c, translation[1] + BLOCK_SIZE * (r - 2), BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(window, (0, 0, 0), (
                        translation[0] + BLOCK_SIZE * c, translation[1] + BLOCK_SIZE * (r - 2), BLOCK_SIZE, BLOCK_SIZE),
                                     3)

        for r in range(self.working_piece.dimension):
            for c in range(self.working_piece.dimension):
                if self.working_piece.cells[r][c] != 0:
                    pygame.draw.rect(window, self.working_piece.color, (
                        translation[0] + BLOCK_SIZE * (c + self.working_piece.column),
                        translation[1] + BLOCK_SIZE * ((r + self.working_piece.row) - 2) + vertical_offset,
                        BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(window, (0, 0, 0), (
                        translation[0] + BLOCK_SIZE * (c + self.working_piece.column),
                        translation[1] + BLOCK_SIZE * ((r + self.working_piece.row) - 2) + vertical_offset,
                        BLOCK_SIZE, BLOCK_SIZE), 3)

        self.draw_next_piece(window)
        self.draw_score(window)

        pygame.display.update()

    def draw_next_piece(self, window):
        # pygame.draw.rect(window, (255, 255, 255), (0, 0, GRID_WIDTH, GRID_HEIGHT))
        next_piece = self.working_pieces[1]
        if next_piece.dimension == 2:
            x_offset, y_offset = BLOCK_SIZE, BLOCK_SIZE
        elif next_piece.dimension == 3:
            x_offset, y_offset = BLOCK_SIZE / 2, BLOCK_SIZE
        elif next_piece.dimension == 4:
            x_offset, y_offset = 0, BLOCK_SIZE / 2
        else:
            x_offset, y_offset = None, None

        grid_width, grid_height = GRID_WIDTH * BLOCK_SIZE, GRID_HEIGHT * BLOCK_SIZE
        w, h = pygame.display.get_surface().get_size()
        next_shape_position = [(w - grid_width) // 2, (h - grid_height) // 2]
        next_shape_width = 4 * BLOCK_SIZE
        translation = [(next_shape_position[0] + grid_width) + next_shape_position[0] // 2 - next_shape_width // 2,
                       next_shape_position[1]]
        for r in range(next_piece.dimension):
            for c in range(next_piece.dimension):
                if next_piece.cells[r][c] != 0:
                    pygame.draw.rect(window, self.working_pieces[1].color, (
                        translation[0] + x_offset + BLOCK_SIZE * c, translation[1] + y_offset + BLOCK_SIZE * r,
                        BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(window, (0, 0, 0), (
                        translation[0] + x_offset + BLOCK_SIZE * c, translation[1] + y_offset + BLOCK_SIZE * r,
                        BLOCK_SIZE, BLOCK_SIZE), 3)

    def draw_score(self, window):
        text = self.font_score.render("Score: " + str(self.score), True, (0, 0, 0))
        window.blit(text, (10, 10))

    def change_pieces(self):
        for i in range(len(self.working_pieces) - 1):
            self.working_pieces[i] = self.working_pieces[i + 1]
        self.working_pieces[len(self.working_pieces) - 1] = Piece.next_piece()
        self.working_piece = self.working_pieces[0]
