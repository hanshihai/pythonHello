
_replace_a = 'Fizz'
_replace_b = 'Buzz'
_replace_ab = _replace_a + _replace_b
_jump_a = 3
_jump_b = 5


def jump(max):
    result = []
    result.append(0)
    index = 1
    while index < max:
        if index%_jump_a == 0 and index%_jump_b == 0:
            result.append(_replace_ab)
        elif index%_jump_a == 0:
            result.append(_replace_a)
        elif index%_jump_b == 0:
            result.append(_replace_b)
        else:
            result.append(index)

        index += 1
    return result


def main():
    print(jump(100))


if __name__ == '__main__':
    main()