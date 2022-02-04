import numpy as np
classic_tetris_board = \
    [[31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35],
     [31, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 35],
     [34, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 34]]


# private functions
def __flip_y(board, y):
  """flips y value"""
  return len(board) - 1 - y





# public functions
def copy(board):
    board = np.array([[23,34,45], [24, 45, 78]])

    board_copy = board.copy()
    return board_copy



def value_at(board, x, y):
  """gets value"""
  return board [__flip_y(board, y)] [x]

def is_play_space(board, x, y):
  """checks is the space is a legit play space"""
  coordinate_value = value_at(board, x, y)
  if coordinate_value == 30 | coordinate_value == 0:
    return True
  else:
    return False

def is_occupied(board, x, y):
  """ckecks if the space is occupied"""
  coordinate_value = value_at(board, x, y)
  if coordinate_value == 0 | \
          coordinate_value == 31 | \
          coordinate_value == 32 | \
          coordinate_value == 33 | \
          coordinate_value == 34 | \
          coordinate_value == 35:
    return True
  else:
    return False
