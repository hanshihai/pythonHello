import turtle

FORWARD_ANGLE = 20
FORWARD_DETLA = 10
BRANCH_MIN_LENGTH = 8


def main():
    length = 80
    turtle.left(90)
    turtle.penup()
    turtle.backward(length)
    turtle.pendown()
    branch(length)
    turtle.exitonclick()


def change_pen_color(length):
    if BRANCH_MIN_LENGTH + FORWARD_DETLA >= length:
        turtle.color("green")
    else:
        turtle.color("brown")


def branch(length):
    if length > BRANCH_MIN_LENGTH:
        change_pen_color(length)
        turtle.forward(length)
        turtle.right(FORWARD_ANGLE)
        branch(length - FORWARD_DETLA)
        turtle.left(FORWARD_ANGLE * 2)
        branch(length - FORWARD_DETLA)
        turtle.right(FORWARD_ANGLE)
        change_pen_color(length)
        turtle.backward(length)


if __name__ == '__main__':
    main()