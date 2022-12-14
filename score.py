from number import Number

X_OFFSET = 120


class Score:

    def __init__(self, side, screen_height, block_size):
        self.side = side
        self.left = Number(block_size)
        self.right = Number(block_size)
        self.score = 0
        self.y_offset = (screen_height / 2) - block_size

        y_offset = (screen_height / 2) - block_size
        if self.side == "left":
            self.left.move((X_OFFSET + block_size * 4) * -1, y_offset)
            self.right.move(-X_OFFSET, y_offset)
        elif self.side == "right":
            self.left.move(X_OFFSET - (block_size * 2), y_offset)
            self.right.move(X_OFFSET + (block_size * 2), y_offset)

        self.hide_under_ten()


    def hide_under_ten(self):
        if self.side == "left":
            self.left.hide_number()
        elif self.side == "right":
            self.right.hide_number()
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()

    def update(self):
        """Updates the number based on the current score."""

        if self.score == 10:
            self.left.set_number(1)
            self.right.set_number(0)
        else:
            if self.side == "left":
                self.right.set_number(self.score)
            else:
                self.left.set_number(self.score)
