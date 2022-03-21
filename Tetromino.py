from enum import Enum
import board
import draw



class Orientation(Enum):
    UP, DOWN, LEFT, RIGHT = range(4)


class Rotation(Enum):
    CW, CCW = range(2)


class Movement(Enum):
    LEFT, RIGHT, DOWN = range(3)


class Tetrimino:
    def __init__(self, orientation, location):
        self.orientation = orientation
        self.location = location

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

    def move(self, movement):
        if movement == Movement.LEFT:
            self.location[0] -= 1

        if movement == Movement.RIGHT:
            self.location[0] += 1

        if movement == Movement.DOWN:
            self.location[1] -= 1

    def add_to_board(self, board):
        raise Exception("there is no draw method for this parent class")

