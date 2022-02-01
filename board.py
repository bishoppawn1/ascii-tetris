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




def value_at(board, x, y):
  """gets value"""
  return board [__flip_y(board, y)] [x]

def is_play_space(board, x, y):
  """checks is the space is a legit play space"""
  coordanate_value = value_at(board, x, y)
  if coordanate_value == 30 | coordanate_value == 0:
    return True
  else:
    return False

def is_occupied(board, x, y):
  """ckecks if the space is occupied"""
  coordanate_value = value_at(board, x, y)
  if coordanate_value == 0 | coordanate_value == 31 | coordanate_value == 32 | coordanate_value == 33 | coordanate_value == 34 | coordanate_value == 35:
    return True
  else:
    return False
