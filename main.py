import time
from turtle import Turtle, Screen, mainloop
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
NUMBER_BLOCK_SIZE = 10
BALL_WIDTH = 20
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PAUSE_BETWEEN_ROUNDS = 3
PLAY_TO = 10

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.cv._rootwindow.resizable(False, False)
screen.bgcolor("black")
screen.tracer(False)

scoreboard = Scoreboard(SCREEN_HEIGHT, NUMBER_BLOCK_SIZE)
left_paddle = Paddle("left", SCREEN_HEIGHT, SCREEN_WIDTH)
right_paddle = Paddle("right", SCREEN_HEIGHT, SCREEN_WIDTH)
ball = Ball(SCREEN_HEIGHT, SCREEN_WIDTH)

end_message = Turtle()
end_message.hideturtle()
end_message.color("white")
end_message.penup()


# screen.mode("logo")

def left_paddle_up():
    left_paddle.up()


def left_paddle_down():
    left_paddle.down()


def right_paddle_up():
    right_paddle.up()


def right_paddle_down():
    right_paddle.down()


def detect_hit():
    if ball.distance(left_paddle) < BALL_WIDTH or ball.distance(right_paddle) < BALL_WIDTH:
        ball.bounce("paddle")


def detect_bounce():
    if abs(ball.ycor()) + BALL_WIDTH / 2 > SCREEN_HEIGHT / 2:
        ball.bounce("wall")
    elif ball.distance(left_paddle) < 50 and ball.xcor() <= left_paddle.xcor() + BALL_WIDTH:
        ball.bounce("paddle")
        return True
    elif ball.distance(right_paddle) < 50 and ball.xcor() >= right_paddle.xcor() - BALL_WIDTH:
        ball.bounce("paddle")
        return True

    return False


def detect_score():
    if ball.xcor() <= (-SCREEN_WIDTH / 2):
        add_point("right")
        return True

    if ball.xcor() >= (SCREEN_WIDTH / 2):
        add_point("left")
        return True

    return False


def add_point(side):
    player = getattr(scoreboard, side)
    player.increase_score()
    scoreboard.set_winner()


def is_game_over():
    return scoreboard.left.score == PLAY_TO or scoreboard.right.score == PLAY_TO


def play():
    point_scored = False
    while not point_scored:

        ball.move()
        detect_bounce()
        time.sleep(ball.ball_speed)
        point_scored = detect_score()
        screen.update()


def reset_ball():
    ball.goto(0, 0)
    ball.prepare_ball()
    left_paddle.move_to_side("left")
    right_paddle.move_to_side("right")
    screen.update()
    time.sleep(PAUSE_BETWEEN_ROUNDS)


def play_again():
    scoreboard.reset()
    return True


screen.onkeypress(fun=left_paddle_up, key="e")
screen.onkeypress(fun=left_paddle_down, key="d")
screen.onkeypress(fun=right_paddle_up, key="Up")
screen.onkeypress(fun=right_paddle_down, key="Down")
screen.onkeypress(fun=play_again, key='space')

screen.listen()

play_again = True
while play_again:
    end_message.clear()

    game_over = is_game_over()
    while not game_over:
        reset_ball()
        play()
        game_over = is_game_over()

    if scoreboard.winner == "Player 1":
        offset = -200
    else:
        offset = 200
    end_message.goto(offset, 0)
    end_message.write(f"{scoreboard.winner} wins!", align="center", font=("lucida console", 16, "normal"))

mainloop()
