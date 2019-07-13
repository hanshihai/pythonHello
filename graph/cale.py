import matplotlib.pyplot as plt
import numpy as np

def main():
    max = 100
    x = -100.0

    plt.grid(color='gray', linestyle='-', linewidth=1)

    while x <= max:
        y = 2.75
        z = y
        if x != 0:
            y = 1 + 1 / x
            z = pow(y, x)

        print(x, z)
        plt.scatter(x, z)
        x += 10

    plt.show()


if __name__ == "__main__":
    main()
