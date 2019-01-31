import random


def main():
    _MAX = 999
    _THRESHOLD = int(_MAX / 2)
    target = random.randint(1,_MAX)
    print("generating a random number: {}".format(target))

    guess(target, _MAX, _THRESHOLD)


def guess(target, MAX, THRESHOLD):
    index = 1
    i_min = 0
    i_max = MAX
    num = int((i_min + i_max) / 2)
    while num != target and index < THRESHOLD:
        print("round {} and the guess is {}.".format(index, num))

        if num < target:
            i_min = num
        elif num > target:
            i_max = num

        num = int((i_min + i_max) / 2)
        index += 1

    if num == target:
        print("Bigoo, the guess is out {} with round {}".format(num, index))

    if index >= THRESHOLD:
        print("Failed to guess out...")


if __name__ == '__main__':
    main()