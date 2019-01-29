
class Person:
    name = []


def main():
    print("hello world")
    p1 = Person()
    p2 = Person()
    p1.name.append("p1")
    print(p1.name)
    print(p2.name)
    print(Person.name)


if __name__ ==  '__main__':
    main()