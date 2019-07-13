import matplotlib.pyplot as plt
import numpy as np

def main():
    max = 10
    x = -10.0

    plt.grid(color='gray', linestyle='-', linewidth=1)

    while x <= max:
        z = 1 / (1 + pow(2.71828, -x))
        print(x, z)
        plt.scatter(x, z)
        x += 1

    plt.show()


if __name__ == "__main__":
    main()
