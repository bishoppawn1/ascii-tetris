import Tetromino


class S_Tetrimino(Tetromino.Tetrimino):
    def __init__(self, orientation, location):
        super().__init__(orientation, location)
    def add_to_board(self, drawing_board):
        if self.orientation == Tetromino.Orientation.DOWN:
            # center
            Tetromino.board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # upper-left
            Tetromino.board.set_value_at(drawing_board, self.location[0] - 1, self.location[1] + 1, 0)
            # left
            Tetromino.board.set_value_at(drawing_board, self.location[0] - 1, self.location[1], 0)
            # lower
            Tetromino.board.set_value_at(drawing_board, self.location[0], self.location[1] - 1, 0)
        elif self.orientation == Tetromino.Orientation.UP:
            # center
            Tetromino.board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # upper
            Tetromino.board.set_value_at(drawing_board, self.location[0], self.location[1] + 1, 0)
            # left
            Tetromino.board.set_value_at(drawing_board, self.location[0] - 1, self.location[1], 0)
            # lower-left
            Tetromino.board.set_value_at(drawing_board, self.location[0] - 1, self.location[1] - 1, 0)
        elif self.orientation == Tetromino.Orientation.LEFT:
            # center
            Tetromino.board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # upper
            Tetromino.board.set_value_at(drawing_board, self.location[0], self.location[1] + 1, 0)
            # right-upper
            Tetromino.board.set_value_at(drawing_board, self.location[0] + 1, self.location[1] + 1, 0)
            # left
            Tetromino.board.set_value_at(drawing_board, self.location[0] - 1, self.location[1], 0)
        elif self.orientation == Tetromino.Orientation.RIGHT:
            # center
            Tetromino.board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # lower
            Tetromino.board.set_value_at(drawing_board, self.location[0], self.location[1] + 1, 0)
            # right
            Tetromino.board.set_value_at(drawing_board, self.location[0] + 1, self.location[1], 0)
            # lower-left
            Tetromino.board.set_value_at(drawing_board, self.location[0] + 1, self.location[1] + 1, 0)
