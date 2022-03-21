import Tetromino
import pieces.S_tetrimino
import pieces.T_tetrimino
import pieces.L_tetrimino
import pieces.J_tetrimino
import pieces.O_tetrimino
import pieces.I_tetrimino


tetrimino_1 = pieces.I_tetrimino.I_tetrimino(Tetromino.Orientation.RIGHT, [5, 7])
tetrimino_1.add_to_board(Tetromino.board.classic_tetris_board)


tetrimino_2 = pieces.O_tetrimino.O_tetrimino(Tetromino.Orientation.LEFT, [2, 5])
tetrimino_2.add_to_board(Tetromino.board.classic_tetris_board)


tetrimino_3 = pieces.J_tetrimino.J_tetrimino(Tetromino.Orientation.DOWN, [3, 11])
tetrimino_3.add_to_board(Tetromino.board.classic_tetris_board)


tetrimino_4 = pieces.L_tetrimino.L_tetrimino(Tetromino.Orientation.UP, [8, 5])
tetrimino_4.add_to_board(Tetromino.board.classic_tetris_board)


tetrimino_5 = pieces.T_tetrimino.T_tetromino(Tetromino.Orientation.UP, [3, 7])
tetrimino_5.add_to_board(Tetromino.board.classic_tetris_board)


tetrimino_6 = pieces.S_tetrimino.S_Tetrimino(Tetromino.Orientation.UP, [1, 5])
tetrimino_6.add_to_board(Tetromino.board.classic_tetris_board)
Tetromino.draw.draw_int_2d_array(Tetromino.board.classic_tetris_board)
