import turtle

min = -80
max = 80

def main(a):
    c = -1 / a
    p1 = a * max
    p2 = a * min
    c1 = c * max
    c2 = c * min

    turtle.goto(max, 0)
    turtle.goto(min, 0)
    turtle.goto(0, 0)
    turtle.goto(0, max)
    turtle.goto(0, min)
    turtle.goto(0, 0)

    turtle.color("green")
    turtle.pendown()
    turtle.goto(max, p1)
    turtle.goto(min, p2)
    turtle.goto(0, 0)

    turtle.color("red")
    turtle.goto(max, c1)
    turtle.goto(min, c2)
    turtle.goto(0, 0)

    turtle.exitonclick()


if __name__ == '__main__':
    inputs = input("please input a:")
    a = float(inputs)
    main(a)


