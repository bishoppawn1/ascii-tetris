import Tetrimino

class S_tetrimino(Tetrimino.Tetromino):
    def __init__(self, orientation, location):
        super().__init__(orientation, location)
    def add_to_board(self, drawing_board):
        if self.orientation == Tetrimino.Orientation.DOWN:
            # center
            Tetrimino.board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # upper-left
            Tetrimino.board.set_value_at(drawing_board, self.location[0] - 1, self.location[1] + 1, 0)
            # left
            Tetrimino.board.set_value_at(drawing_board, self.location[0] - 1, self.location[1], 0)
            # lower
            Tetrimino.board.set_value_at(drawing_board, self.location[0], self.location[1] - 1, 0)
        elif self.orientation == Tetrimino.Orientation.UP:
            # center
            Tetrimino.board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # upper
            Tetrimino.board.set_value_at(drawing_board, self.location[0], self.location[1] + 1, 0)
            # left
            Tetrimino.board.set_value_at(drawing_board, self.location[0] - 1, self.location[1], 0)
            # lower-left
            Tetrimino.board.set_value_at(drawing_board, self.location[0] - 1, self.location[1] - 1, 0)
        elif self.orientation == Tetrimino.Orientation.LEFT:
            # center
            Tetrimino.board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # upper
            Tetrimino.board.set_value_at(drawing_board, self.location[0], self.location[1] + 1, 0)
            # right-upper
            Tetrimino.board.set_value_at(drawing_board, self.location[0] + 1, self.location[1] + 1, 0)
            # left
            Tetrimino.board.set_value_at(drawing_board, self.location[0] - 1, self.location[1], 0)
        elif self.orientation == Tetrimino.Orientation.RIGHT:
            # center
            Tetrimino.board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # lower
            Tetrimino.board.set_value_at(drawing_board, self.location[0], self.location[1] + 1, 0)
            # right
            Tetrimino.board.set_value_at(drawing_board, self.location[0] + 1, self.location[1], 0)
            # lower-left
            Tetrimino.board.set_value_at(drawing_board, self.location[0] + 1, self.location[1] + 1, 0)
