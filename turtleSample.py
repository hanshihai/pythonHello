import turtle


def thread(max_length):
    length = 1
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    while length < max_length:
        turtle.forward(length)
        turtle.right(90)
        length += 5
    turtle.end_fill()
    turtle.exitonclick()
    return


def initPosition(left, up):
    print("init position: ", turtle.position())
    turtle.penup()
    turtle.backward(left)
    turtle.left(90)
    turtle.forward(up)
    turtle.right(90)
    turtle.pendown()
    print("move to position: ", turtle.position())


def charp(length, count, argle):
    int = 1
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    while int <= count:
        turtle.forward(length)
        turtle.right(argle)
        int += 1
    turtle.end_fill()
    turtle.exitonclick()


def circle(max_length):
    length = 1

    while length < max_length:
        turtle.circle(length)
        length += 10
    turtle.exitonclick()
    return


if __name__ == '__main__':
    initPosition(75, 75)
    charp(150, 24, 165)
    #thread(100)
