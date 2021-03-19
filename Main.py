import Game
import pygame


def main():
    pygame.init()
    window = pygame.display.set_mode((Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT))
    pygame.display.set_caption("Tetris")

    game = Game.Game()

    clock = pygame.time.Clock()
    fps = 80

    run, game_over = True, False
    while run:
        clock.tick(fps)

        if game.is_ai_active:
            game.working_piece = game.ai.find_best(game.grid, game.working_pieces)
            while game.working_piece.can_move_down(game.grid):
                clock.tick(fps)

                game.working_piece.move_down(game.grid)

                if game.grid.clear_lines():
                    game.score += 1

                game.draw_grid(window)

        for event in list(pygame.event.get()):
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.working_piece.rotate(game.grid)
                elif event.key == pygame.K_DOWN:
                    game.working_piece.move_down(game.grid)
                elif event.key == pygame.K_LEFT:
                    game.working_piece.move_left(game.grid)
                elif event.key == pygame.K_RIGHT:
                    game.working_piece.move_right(game.grid)

        if not game.is_ai_active:
            game.grid.clear_lines()
            game.draw_grid(window)

        if not game.working_piece.move_down(game.grid):
            game.grid.add_piece(game.working_piece)
            game.change_pieces()

        if game.grid.exceeded():
            run = False
            game_over = True

    while game_over:
        for event in list(pygame.event.get()):
            if event.type == pygame.QUIT:
                game_over = False
        game.draw_grid(window)


if __name__ == '__main__':
    main()
