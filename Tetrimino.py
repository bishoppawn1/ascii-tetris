class Tetrimino:
    def __init__(self, orientation, location):
        self.orientation = orientation
        self.location = location

    def can_rotate(self):
        print(self.location)
        return True

    def rotate(self):
        return True

    def can_move(self):
        return True

    def move(self):
        return True


tetrimino_1 = Tetrimino("up", "5, 5")
print(tetrimino_1.location)
