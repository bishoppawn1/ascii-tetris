import board
import draw
from enum import Enum

class Orientation(Enum):
    UP, DOWN, LEFT, RIGHT = range(4)

class Shape(Enum):
    I, O, T, S, Z, J, L = range(7)

active_location_x = (5)
active_location_y = (5)
active_shape = Shape.T
active_orientation = Orientation.UP


def add_piece(board1, x, y, orientation, shape):
    if orientation == Orientation.DOWN || shape == Shape.T:
        # center
        board.set_value_at(board1, x, y, 0)
        # lower
        board.set_value_at(board1, x, y - 1, 0)
        # left
        board.set_value_at(board1, x - 1, y, 0)
        # right
        board.set_value_at(board1, x + 1, y, 0)
    elif orientation == Orientation.UP:
        # center
        board.set_value_at(board1, x, y, 0)
        # upper
        board.set_value_at(board1, x, y + 1, 0)
        # left
        board.set_value_at(board1, x - 1, y, 0)
        # right
        board.set_value_at(board1, x + 1, y, 0)
    elif orientation == Orientation.LEFT:
        # center
        board.set_value_at(board1, x, y, 0)
        # upper
        board.set_value_at(board1, x, y + 1, 0)
        # left
        board.set_value_at(board1, x - 1, y, 0)
        # lower
        board.set_value_at(board1, x, y - 1, 0)
    elif orientation == Orientation.RIGHT:
        # center
        board.set_value_at(board1, x, y, 0)
        # upper
        board.set_value_at(board1, x, y + 1, 0)
        # left
        board.set_value_at(board1, x - 1, y, 0)
        # lower
        board.set_value_at(board1, x, y - 1, 0)


    if orientation == Orientation.DOWN || shape == Shape.L:
        # center
        board.set_value_at(board1, x, y, 0)
        # lower
        board.set_value_at(board1, x, y - 1, 0)
        # left
        board.set_value_at(board1, x - 1, y, 0)
        # lower2
        board.set_value_at(board1, x, y - 2, 0)
    elif orientation == Orientation.UP:
        # center
        board.set_value_at(board1, x, y, 0)
        # upper
        board.set_value_at(board1, x, y + 1, 0)
        # upper2
        board.set_value_at(board1, x, y + 2, 0)
        # right
        board.set_value_at(board1, x + 1, y, 0)
    elif orientation == Orientation.LEFT:
        # center
        board.set_value_at(board1, x, y, 0)
        # upper
        board.set_value_at(board1, x, y + 1, 0)
        # left
        board.set_value_at(board1, x - 1, y, 0)
        # left2
        board.set_value_at(board1, x - 2, y, 0)
    elif orientation == Orientation.RIGHT:
        # center
        board.set_value_at(board1, x, y, 0)
        # lower
        board.set_value_at(board1, x, y - 1, 0)
        # right
        board.set_value_at(board1, x + 1, y, 0)
        # right2
        board.set_value_at(board1, x + 2, y, 0)


    if orientation == Orientation.DOWN || shape == Shape.J:
        # center
        board.set_value_at(board1, x, y, 0)
        # lower
        board.set_value_at(board1, x, y - 1, 0)
        # lower2
        board.set_value_at(board1, x, y - 2, 0)
        # right
        board.set_value_at(board1, x + 1, y, 0)
    elif orientation == Orientation.UP:
        # center
        board.set_value_at(board1, x, y, 0)
        # upper
        board.set_value_at(board1, x, y + 1, 0)
        # upper2
        board.set_value_at(board1, x, y + 2, 0)
        # left
        board.set_value_at(board1, x - 1, y, 0)
    elif orientation == Orientation.LEFT:
        # center
        board.set_value_at(board1, x, y, 0)
        # lower
        board.set_value_at(board1, x, y - 1, 0)
        # left
        board.set_value_at(board1, x - 1, y, 0)
        # left2
        board.set_value_at(board1, x - 2, y, 0)
    elif orientation == Orientation.RIGHT:
        # center
        board.set_value_at(board1, x, y, 0)
        # right
        board.set_value_at(board1, x + 1, y, 0)
        # right2
        board.set_value_at(board1, x + 2, y, 0)
        # lower
        board.set_value_at(board1, x, y - 1, 0)

board2 = board.copy(board.classic_tetris_board)
add_piece(board2, 5, 6, active_orientation, active_shape)
draw.draw_int_2d_array(board2)