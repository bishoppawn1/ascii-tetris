import Tetrimino

class T_tetrimino(Tetromino):
    def __init__(self, orientation, location):
        super().__init__(orientation, location)
    def add_to_board(self, drawing_board):
        if self.orientation == Orientation.DOWN:
            # center
            board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # lower
            board.set_value_at(drawing_board, self.location[0], self.location[1] - 1, 0)
            # left
            board.set_value_at(drawing_board, self.location[0] - 1, self.location[1], 0)
            # right
            board.set_value_at(drawing_board, self.location[0] + 1, self.location[1], 0)
        elif self.orientation == Orientation.UP:
            # center
            board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # upper
            board.set_value_at(drawing_board, self.location[0], self.location[1] + 1, 0)
            # left
            board.set_value_at(drawing_board, self.location[0] - 1, self.location[1], 0)
            # right
            board.set_value_at(drawing_board, self.location[0] + 1, self.location[1], 0)
        elif self.orientation == Orientation.LEFT:
            # center
            board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # upper
            board.set_value_at(drawing_board, self.location[0], self.location[1] + 1, 0)
            # left
            board.set_value_at(drawing_board, self.location[0] - 1, self.location[1], 0)
            # lower
            board.set_value_at(drawing_board, self.location[0], self.location[1] - 1, 0)
        elif self.orientation == Orientation.RIGHT:
            # center
            board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # upper
            board.set_value_at(drawing_board, self.location[0], self.location[1] + 1, 0)
            # right
            board.set_value_at(drawing_board, self.location[0] + 1, self.location[1], 0)
            # lower
            board.set_value_at(drawing_board, self.location[0], self.location[1] - 1, 0)
