import matplotlib.pyplot as plt


def main(a, b, c):

    m = b / (2 * a)
    n = (4*a*c - b*b) / (4*a)
    print(" --- y = {}x^2 + {}x + {} ---".format(a,b,c))
    print(" --- m = {} , and n = {}".format(m, n))

    middle = -m
    min = -5
    max = middle + 5

    x = min + middle

    plt.grid(color='gray', linestyle='-', linewidth=1)

    while x <= max:
        y = a * x * x + b * x + c
        print("x: {} - y: {}".format(x, y))
        plt.scatter(x, y)
        x += 1

    plt.show()


if __name__ == "__main__":
    while True:
        inputs = input("please input a, b, and c: ")
        if inputs == "q":
            break
        input_array = inputs.split(" ")
        a = int(input_array[0])
        b = int(input_array[1])
        c = int(input_array[2])
        main(a,b,c)