import matplotlib.pyplot as plt


def main(labels, values):
    fig, ax = plt.subplots()
    ax.text(0.5,-0.0,'label', horizontalalignment='center',verticalalignment='center', transform=ax.transAxes)
    ax.pie(values, labels=labels, startangle=90)
    ax.axis('equal')
    plt.show()


if __name__ == "__main__":
    a = ['a','b','c']
    b = [20, 40, 80]
    main(a,b)