import matplotlib.pyplot as plt
import numpy as np


def main(a, b):

    x = -a
    dt = a / 10

    plt.grid(color='gray', linestyle='-', linewidth=1)

    while x <= a:
        y = np.sqrt((1 - np.power(x,2) / np.power(a, 2)) * np.power(b, 2))
        print("x: {} - y: {}".format(x, y))
        plt.scatter(x, y)
        plt.scatter(x, -y)
        x += dt

    plt.show()


if __name__ == "__main__":
    while True:
        inputs = input("please input a and b: ")
        if inputs == "q":
            break
        input_array = inputs.split(" ")
        a = int(input_array[0])
        b = int(input_array[1])
        main(a,b)