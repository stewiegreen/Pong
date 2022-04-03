import turtle
import random

window = turtle.Screen()
window.bgcolor("black")

turtle.penup()
turtle.color('white')
turtle.sety(300)
pong = turtle.write("PONG", align='center', font=("Verdana", 60, "normal"))

# making the court
turtle.sety(250)
turtle.pendown()
turtle.setx(450)
turtle.sety(-250)
turtle.setx(-450)
turtle.sety(250)
turtle.setx(0)

# making the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.move_x = 5
ball.move_y = 5

# making the right paddle
right_paddle = turtle.Turtle()
right_paddle.right(90)
right_paddle.shape("square")
right_paddle.shapesize(1.5, 5)
right_paddle.setx(400)
right_paddle.sety(0)
right_paddle.color("white")

# making the left paddle
left_paddle = turtle.Turtle()
left_paddle.right(90)
left_paddle.shape("square")
left_paddle.shapesize(1.5, 5)
left_paddle.setx(-400)
left_paddle.sety(0)
left_paddle.color("white")

# moving left paddle


def upLeftPaddle():
    left_paddle.penup()
    left_paddle.forward(-40)


def downLeftPaddle():
    left_paddle.penup()
    left_paddle.forward(40)

# moving right paddle


def downRightPaddle():
    right_paddle.penup()
    right_paddle.forward(40)


def upRightPaddle():
    right_paddle.penup()
    right_paddle.forward(-40)


def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 30 and abs(a.ycor() - b.ycor()) < 30


turtle.listen()
turtle.onkeypress(upLeftPaddle, 'w')
turtle.onkeypress(downLeftPaddle, 'x')
turtle.onkeypress(upRightPaddle, 'Up')
turtle.onkeypress(downRightPaddle, 'Down')


tess = turtle.Turtle()


def buttonclick(x, y):
    print("You clicked at this coordinate({0},{1})".format(x, y))


turtle.onscreenclick(buttonclick, 1)
turtle.listen()  # listen to incoming connections
turtle.speed(10)  # set the speed"""


def main():

    left_paddle_score = 0
    right_paddle_score = 0
    score = turtle.Turtle()
    score.penup()
    score.goto(0, 260)
    score.color("white")
    score.write(f"Left: {left_paddle_score} Right: {right_paddle_score}",
                align='center', font=("Verdana", 45, "normal"))

    while True:

        window.update()
        ball.penup()
        ball.setx(ball.xcor() + ball.move_x)
        ball.sety(ball.ycor() + ball.move_y)

        if is_collided_with(right_paddle, ball):
            ball.move_x *= -1
            print("hit")

        if is_collided_with(left_paddle, ball):
            ball.move_x *= -1

        if ball.ycor() > 240:
            ball.sety(240)
            ball.move_y *= -1

        if ball.ycor() < -240:
            ball.sety(-240)
            ball.move_y *= -1

        if ball.xcor() > 430:
            ball.goto(0, 0)
            left_paddle_score += 1
            score.clear()
            score.write(f"Left: {left_paddle_score} Right: {right_paddle_score}",
                        align='center', font=("Verdana", 45, "normal"))

        if ball.xcor() < -440:
            ball.goto(0, 0)
            right_paddle_score += 1
            score.clear()
            score.write(f"Left: {left_paddle_score} Right: {right_paddle_score}",
                        align='center', font=("Verdana", 45, "normal"))

        if left_paddle_score == 5 or right_paddle_score == 5:
            break

    turtle.done()


main()

# hold the screen


# onscreen function to send coordinate
