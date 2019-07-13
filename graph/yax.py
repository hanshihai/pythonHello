import matplotlib.pyplot as plt
import numpy as np

def main(a):
    c = -1 / a

    min = -5
    max = 5

    x = min

    plt.figure(figsize=(6.4,4.8))
    plt.grid(color='gray', linestyle='-', linewidth=1)
    plt.xticks(np.arange(-10, 10, 1.25))

    while x <= max:
        y = a * x
        z = c * x

        plt.scatter(x, y)
        plt.scatter(x, z)
        x += 1

    plt.show()


if __name__ == "__main__":
        input = input("please input a:")
        a = int(input)
        main(a)
