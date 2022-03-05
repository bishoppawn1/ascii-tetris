class Tetromino:
    def __init__(self, orientation, location):
        self.orientation = orientation
        self.location = location

    def can_rotate(self, board):
        return True

    def rotate(self, cw, ccw):

        return True

    def can_move(self, board):
        return True

    def move(self, board):
        return True

    def draw(self, board):
        return True




class I_tetrimino(Tetromino):
    def __init__(self, orientation, location):

      super().__init__(orientation, location)




tetrimino_1 = I_tetrimino("up", "5, 5")
print(tetrimino_1.location)