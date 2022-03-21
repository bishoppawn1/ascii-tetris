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


