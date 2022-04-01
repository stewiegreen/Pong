import turtle

window = turtle.Screen()
window.bgcolor("black")

turtle.penup()
turtle.color('white')
turtle.sety(300)
pong = turtle.write("PONG", align='center', font=("Verdana", 60, "normal"))

turtle.sety(250)
turtle.pendown()
turtle.setx(450)
turtle.sety(-250)
turtle.setx(-450)
turtle.sety(250)
turtle.setx(0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")


right_paddle = turtle.Turtle()
right_paddle.right(90)
right_paddle.shape("square")
right_paddle.shapesize(1.5, 5)
right_paddle.setx(400)
right_paddle.sety(0)
right_paddle.color("white")
print(right_paddle.position())

left_paddle = turtle.Turtle()
left_paddle.right(90)
left_paddle.shape("square")
left_paddle.shapesize(1.5, 5)
left_paddle.setx(-400)
left_paddle.sety(0)
left_paddle.color("white")
print(left_paddle.position())


def upLeftPaddle():
    left_paddle.penup()
    left_paddle.forward(-40)


def downLeftPaddle():
    left_paddle.penup()
    left_paddle.forward(40)


def downRightPaddle():
    right_paddle.penup()
    right_paddle.forward(40)


def upRightPaddle():
    right_paddle.penup()
    right_paddle.forward(-40)


turtle.onkey(upLeftPaddle, 'Up')
turtle.onkey(downLeftPaddle, 'Down')

turtle.onkey(upRightPaddle, 'w')
turtle.onkey(downRightPaddle, 'x')

turtle.listen()

turtle.done()    # hold the screen


# onscreen function to send coordinate
"""tess = turtle.Turtle()


def buttonclick(x, y):
    print("You clicked at this coordinate({0},{1})".format(x, y))


turtle.onscreenclick(buttonclick, 1)
turtle.listen()  # listen to incoming connections
turtle.speed(10)  # set the speed"""
