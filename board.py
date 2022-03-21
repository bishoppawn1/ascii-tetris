import draw

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
    copy_board = []
    for row in range(len(board)):
        row_array = []
        copy_board.append(row_array)
        for column in range(len(board[row])):
          row_array.append(board[row][column])
    return copy_board

def value_at(board, x, y):
  """gets value"""
  return board [__flip_y(board, y)] [x]

def set_value_at(board, x, y, value):
    board [__flip_y(board, y)] [x] = value
    return board


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

# board2 = copy(classic_tetris_board)
# set_value_at(board2, 7, 6, 0)
# draw.draw_int_2d_array(board2)
# draw.draw_int_2d_array(classic_tetris_board)