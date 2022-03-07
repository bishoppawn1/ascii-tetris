from enum import Enum
import piece


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
            if self.orientation == piece.Orientation.UP:
                self.orientation = piece.Orientation.RIGHT

            elif self.orientation == piece.Orientation.RIGHT:
                self.orientation = piece.Orientation.DOWN

            elif self.orientation == piece.Orientation.DOWN:
                self.orientation = piece.Orientation.LEFT

            elif self.orientation == piece.Orientation.LEFT:
                self.orientation = piece.Orientation.UP

        if rotation == Rotation.CCW:
            if self.orientation == piece.Orientation.RIGHT:
                self.orientation = piece.Orientation.UP

            elif self.orientation == piece.Orientation.DOWN:
                self.orientation = piece.Orientation.RIGHT

            elif self.orientation == piece.Orientation.LEFT:
                self.orientation = piece.Orientation.DOWN

            elif self.orientation == piece.Orientation.UP:
                self.orientation = piece.Orientation.LEFT

    def can_move(self, board):
        return True

    def move(self, movement):
        if movement == Movement.LEFT:
            self.location[0] -= 1

        if movement == Movement.RIGHT:
            self.location[0] += 1

        if movement == Movement.DOWN:
            self.location[1] -= 1

    def draw(self, board):
        return True


class I_tetrimino(Tetromino):
    def __init__(self, orientation, location):
        super().__init__(orientation, location)



tetrimino_1 = I_tetrimino(piece.Orientation.UP, [5, 5])
tetrimino_1.move(Movement.LEFT)
print(tetrimino_1.location)
