import Tetromino
import board
import pieces.S_tetrimino
import pieces.T_tetrimino
import pieces.L_tetrimino
import pieces.J_tetrimino
import pieces.O_tetrimino
import pieces.I_tetrimino
import input
import time

board2 = board.copy(board.classic_tetris_board)


def on_press2(key):
    try:
        print('Alphanumeric key pressed: {0} '.format(
            key.char))
    except AttributeError:
        print('special key pressed: {0}'.format(
            key))


tetrimino_1 = pieces.S_tetrimino.S_Tetrimino(Tetromino.Orientation.UP, [6, 5])
tetrimino_1.add_to_board(Tetromino.board.classic_tetris_board)


def dummy_function():
    tetrimino_1.rotate(Tetromino.Rotation.CCW)
    tetrimino_1.add_to_board(board2)
    Tetromino.draw.draw_int_2d_array(board2)
    Tetromino.draw.draw_int_2d_array(Tetromino.board.classic_tetris_board)


input.register_key_press_listener(on_press2)
dummy_function()
