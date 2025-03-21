from turtle import Turtle


MOVE_DIS = 15
class Paddle(Turtle):
    def __init__(self, x_coordinate):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.speed('fastest')
        self.x_coordinate = x_coordinate
        self.goto(x_coordinate, 0)
        self.showturtle()
        self.moving_up = False
        self.moving_down = False

    def up(self):
        if self.ycor() < 250 and self.moving_up:
            self.goto(self.x_coordinate, self.ycor() + MOVE_DIS)

    def down(self):
        if self.ycor() > -250 and self.moving_down:
            self.goto(self.x_coordinate, self.ycor() - MOVE_DIS)

    def start_moving_up(self):
        self.moving_up = True
        self.up()

    def start_moving_down(self):
        self.moving_down = True
        self.down()

    def stop_moving_up(self):
        self.moving_up = False

    def stop_moving_down(self):
        self.moving_down = False