import matplotlib.pyplot as plt


def main(a, b):

    x = -10

    plt.grid(color='gray', linestyle='-', linewidth=1)

    while x < 11:
        y = (x+a)*(x+a) + b
        print("x: {} - y: {}".format(x, y))
        plt.scatter(x, y)
        x += 1

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