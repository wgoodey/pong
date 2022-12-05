from turtle import Turtle

number_dict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}


def create_number(block_size=10):
    number = []
    for i in range(5):
        row = []
        for j in range(3):
            new_block = Turtle("square")
            new_block.penup()
            new_block.color("white")
            new_block.shapesize(0.5, 0.5)
            if i > 0:
                new_block.setheading(270)
                new_block.forward(block_size * i)

            new_block.setheading(0)
            new_block.forward(block_size * j)
            row.append(new_block)

        number.append(row)

    return number


class Number:

    def __init__(self, block_size=10):
        self.blocks = create_number(block_size)

    def move(self, x, y):
        for row in self.blocks:
            for block in row:
                block.forward(x)
                block.setheading(90)
                block.forward(y)

    def set_number(self, number):
        number = getattr(self, number_dict[number])
        number()

    def reset(self, mode):
        """Show or hide all the blocks in the number.
        'hide' will turn all the blocks off
        'show' will turn all the blocks on"""
        for row in self.blocks:
            for block in row:
                reset = getattr(block, mode + 'turtle')
                reset()

    def show_number(self):
        for row in self.blocks:
            for block in row:
                block.showturtle()

    def hide_number(self):
        for row in self.blocks:
            for block in row:
                block.hideturtle()

    def one(self):
        self.reset("hide")
        self.blocks[0][0].showturtle()
        for i in range(len(self.blocks)):
            self.blocks[i][1].showturtle()
        self.blocks[4][0].showturtle()
        self.blocks[4][2].showturtle()

    def two(self):
        self.reset("show")
        self.blocks[1][0].hideturtle()
        self.blocks[1][1].hideturtle()
        self.blocks[3][1].hideturtle()
        self.blocks[3][2].hideturtle()

    def three(self):
        self.reset("show")
        self.blocks[1][0].hideturtle()
        self.blocks[1][1].hideturtle()
        self.blocks[3][0].hideturtle()
        self.blocks[3][1].hideturtle()

    def four(self):
        self.reset("show")
        self.blocks[0][1].hideturtle()
        self.blocks[1][1].hideturtle()
        self.blocks[3][0].hideturtle()
        self.blocks[3][1].hideturtle()
        self.blocks[4][0].hideturtle()
        self.blocks[4][1].hideturtle()

    def five(self):
        self.reset("show")
        self.blocks[1][1].hideturtle()
        self.blocks[1][2].hideturtle()
        self.blocks[3][0].hideturtle()
        self.blocks[3][1].hideturtle()

    def six(self):
        self.reset("show")
        self.blocks[1][1].hideturtle()
        self.blocks[1][2].hideturtle()
        self.blocks[3][1].hideturtle()

    def seven(self):
        self.reset("hide")
        self.blocks[0][0].showturtle()
        self.blocks[0][1].showturtle()
        for i in range(len(self.blocks)):
            self.blocks[i][2].showturtle()

    def eight(self):
        self.reset("show")
        self.blocks[1][1].hideturtle()
        self.blocks[3][1].hideturtle()

    def nine(self):
        self.reset("show")
        self.blocks[1][1].hideturtle()
        self.blocks[3][0].hideturtle()
        self.blocks[3][1].hideturtle()
        self.blocks[4][0].hideturtle()
        self.blocks[4][1].hideturtle()

    def zero(self):
        self.reset("show")
        self.blocks[1][1].hideturtle()
        self.blocks[2][1].hideturtle()
        self.blocks[3][1].hideturtle()
