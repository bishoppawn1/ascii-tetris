from enum import Enum
import piece, board, draw
class Orientation(Enum):
    UP, DOWN, LEFT, RIGHT = range(4)

class Rotation(Enum):
    CW, CCW = range(2)


class Movement(Enum):
    LEFT, RIGHT, DOWN = range(3)


class Tetromino:
    def __init__(self, orientation, location):
        self.orientation = orientation
        self.location = location

    def can_rotate(self, board):
        return True

    def rotate(self, rotation):
        if rotation == Rotation.CW:
            if self.orientation == Orientation.UP:
                self.orientation = Orientation.RIGHT

            elif self.orientation == Orientation.RIGHT:
                self.orientation = Orientation.DOWN

            elif self.orientation == Orientation.DOWN:
                self.orientation = Orientation.LEFT

            elif self.orientation == Orientation.LEFT:
                self.orientation = Orientation.UP

        if rotation == Rotation.CCW:
            if self.orientation == Orientation.RIGHT:
                self.orientation = Orientation.UP

            elif self.orientation == Orientation.DOWN:
                self.orientation = Orientation.RIGHT

            elif self.orientation == Orientation.LEFT:
                self.orientation = Orientation.DOWN

            elif self.orientation == Orientation.UP:
                self.orientation = Orientation.LEFT

    def can_move(self, board):
        return True

    def move(self, movement):
        if movement == Movement.LEFT:
            self.location[0] -= 1

        if movement == Movement.RIGHT:
            self.location[0] += 1

        if movement == Movement.DOWN:
            self.location[1] -= 1

    def add_to_board(self, board):
        raise Exception("there is no draw method for this parent class")


class I_tetrimino(Tetromino):
    def __init__(self, orientation, location):
        super().__init__(orientation, location)

    def add_to_board(self, drawing_board):
        if self.orientation == Orientation.DOWN:
            # center
            board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # upper
            board.set_value_at(drawing_board, self.location[0], self.location[1] + 1, 0)
            # lower
            board.set_value_at(drawing_board, self.location[0], self.location[1] - 1, 0)
            # upper2
            board.set_value_at(drawing_board, self.location[0], self.location[1] + 2, 0)
        elif self.orientation == Orientation.RIGHT:
            # center
            board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # left
            board.set_value_at(drawing_board, self.location[0] - 1, self.location[1], 0)
            # right
            board.set_value_at(drawing_board, self.location[0] + 1, self.location[1], 0)
            # right2
            board.set_value_at(drawing_board, self.location[0] + 2, self.location[1], 0)
        if self.orientation == Orientation.UP:

            # center
            board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # upper
            board.set_value_at(drawing_board, self.location[0], self.location[1] + 1, 0)
            # lower
            board.set_value_at(drawing_board, self.location[0], self.location[1] - 1, 0)
            # upper2
            board.set_value_at(drawing_board, self.location[0], self.location[1] + 2, 0)
        elif self.orientation == Orientation.LEFT:
            # center
            board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # left
            board.set_value_at(drawing_board, self.location[0] - 1, self.location[1], 0)
            # right
            board.set_value_at(drawing_board, self.location[0] + 1, self.location[1], 0)
            # right2
            board.set_value_at(drawing_board, self.location[0] + 2, self.location[1], 0)





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

class L_tetrimino(Tetromino):
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
            # lower2
            board.set_value_at(drawing_board, self.location[0], self.location[1] - 2, 0)
        elif self.orientation == Orientation.UP:
            # center
            board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # upper
            board.set_value_at(drawing_board, self.location[0], self.location[1] + 1, 0)
            # upper2
            board.set_value_at(drawing_board, self.location[0], self.location[1] + 2, 0)
            # right
            board.set_value_at(drawing_board, self.location[0] + 1, self.location[1], 0)
        elif self.orientation == Orientation.LEFT:
            # center
            board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # upper
            board.set_value_at(drawing_board, self.location[0], self.location[1] + 1, 0)
            # left
            board.set_value_at(drawing_board, self.location[0] - 1, self.location[1], 0)
            # left2
            board.set_value_at(drawing_board, self.location[0] - 2, self.location[1], 0)
        elif self.orientation == Orientation.RIGHT:
            # center
            board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # lower
            board.set_value_at(drawing_board, self.location[0], self.location[1] - 1, 0)
            # right
            board.set_value_at(drawing_board, self.location[0] + 1, self.location[1], 0)
            # right2
            board.set_value_at(drawing_board, self.location[0] + 2, self.location[1], 0)

class J_tetrimino(Tetromino):
    def __init__(self, orientation, location):
        super().__init__(orientation, location)
    def add_to_board(self, drawing_board):
        if self.orientation == Orientation.DOWN:
            # center
            board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # lower
            board.set_value_at(drawing_board, self.location[0], self.location[1] - 1, 0)
            # lower2
            board.set_value_at(drawing_board, self.location[0], self.location[1] - 2, 0)
            # right
            board.set_value_at(drawing_board, self.location[0] + 1, self.location[1], 0)
        elif self.orientation == Orientation.UP:
            # center
            board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # upper
            board.set_value_at(drawing_board, self.location[0], self.location[1] + 1, 0)
            # upper2
            board.set_value_at(drawing_board, self.location[0], self.location[1] + 2, 0)
            # left
            board.set_value_at(drawing_board, self.location[0] - 1, self.location[1], 0)
        elif self.orientation == Orientation.LEFT:
            # center
            board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # lower
            board.set_value_at(drawing_board, self.location[0], self.location[1] - 1, 0)
            # left
            board.set_value_at(drawing_board, self.location[0] - 1, self.location[1], 0)
            # left2
            board.set_value_at(drawing_board, self.location[0] - 2, self.location[1], 0)
        elif self.orientation == Orientation.RIGHT:
            # center
            board.set_value_at(drawing_board, self.location[0], self.location[1], 0)
            # right
            board.set_value_at(drawing_board, self.location[0] + 1, self.location[1], 0)
            # right2
            board.set_value_at(drawing_board, self.location[0] + 2, self.location[1], 0)
            # lower
            board.set_value_at(drawing_board, self.location[0], self.location[1] - 1, 0)

tetrimino_1 = L_tetrimino(Orientation.RIGHT, [5, 7])
tetrimino_1.add_to_board(board.classic_tetris_board)

tetrimino_2 = J_tetrimino(Orientation.LEFT, [2, 5])
tetrimino_2.add_to_board(board.classic_tetris_board)

tetrimino_3 = T_tetrimino(Orientation.DOWN, [3, 11])
tetrimino_3.add_to_board(board.classic_tetris_board)

tetrimino_4 = I_tetrimino(Orientation.UP, [8, 5])
tetrimino_4.add_to_board(board.classic_tetris_board)
draw.draw_int_2d_array(board.classic_tetris_board)