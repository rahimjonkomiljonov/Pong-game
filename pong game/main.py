from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)

right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(right_paddle.start_moving_up, 'Up')
screen.onkeyrelease(right_paddle.stop_moving_up, 'Up')

screen.onkeypress(right_paddle.start_moving_down, 'Down')
screen.onkeyrelease(right_paddle.stop_moving_down, 'Down')

screen.onkeypress(left_paddle.start_moving_up, 'w')
screen.onkeyrelease(left_paddle.stop_moving_up, 'w')

screen.onkeypress(left_paddle.start_moving_down, 's')
screen.onkeyrelease(left_paddle.stop_moving_down, 's')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_the_ball()

    # Detect collision with ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


#   Detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed('fastest')

#   Detect when paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.clear()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.clear()
        scoreboard.r_point()

screen.exitonclick()




