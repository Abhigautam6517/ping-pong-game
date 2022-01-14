import time
from turtle import Turtle, Screen
from Paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Ping Pong Game")
screen.bgcolor("Black")
screen.tracer(0)
tim = Turtle()
ball = Ball()
scoreboard = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.down_up, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.down_up, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect a collision with ball
    if ball.xcor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    # Detect a collision with paddle
    if ball.distance(r_paddle) < 50 and  ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:

        ball.bounce_x()


    # detect a right ball goes out
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # detect a left paddle goes out
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()