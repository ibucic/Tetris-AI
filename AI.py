class AI:

    def __init__(self, weights):
        self.height_w = weights[0]
        self.lines_w = weights[1]
        self.holes_w = weights[2]
        self.bumpiness_w = weights[3]

    def best(self, grid, working_pieces, working_pieces_id):
        best = None
        best_score = float('-inf')
        working_piece = working_pieces[working_pieces_id]

        for rotation in range(4):
            piece = working_piece.clone_piece()
            for i in range(rotation):
                piece.rotate(grid)

            while piece.move_left(grid):
                pass
            while grid.valid(piece):
                piece_set = piece.clone_piece()
                while piece_set.move_down(grid):
                    pass
                grid_clone = grid.clone_grid()
                grid_clone.add_piece(piece_set)

                if working_pieces_id == len(working_pieces) - 1:
                    score = - self.height_w * grid_clone.aggregate_height() + self.lines_w * grid_clone.lines() - \
                            self.holes_w * grid_clone.holes() - self.bumpiness_w * grid_clone.bumpiness()
                else:
                    scores = self.best(grid_clone, working_pieces, working_pieces_id + 1)
                    score = scores["score"]

                if score > best_score:
                    best_score = score
                    best = piece.clone_piece()

                piece.column += 1
        return {"piece": best, "score": best_score}

    def find_best(self, grid, working_pieces):
        best = self.best(grid, working_pieces, 0)
        return best["piece"]
