import turtle
import numpy as np

STEP_LENGTH = 10


def printPoint(x, y):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.dot(3,'red')
    turtle.penup()
    turtle.home()
    turtle.pendown()


def main(a, b):
    x = -a
    dt = a / STEP_LENGTH

    while x <= a:
        y = np.sqrt((1 - np.power(x,2) / np.power(a, 2)) * np.power(b, 2))
        print("x:y - {}:{}".format(x, y))
        printPoint(x, y)
        printPoint(x, -y)
        x += dt

    turtle.exitonclick()


if __name__ == "__main__":

        inputs = input("please input a and b: ")
        input_array = inputs.split(" ")
        a = int(input_array[0])
        b = int(input_array[1])
        main(a, b)