import pylab as p


def main():
    # x = p.arange(-5, 5, 0.2)
    # y1 = 2 * x + 1
    # y2 = x ** 2
    # y3 = x ** 3

    # x = p.arange(1, 2, 0.25)
    # y = 1/x

    x = p.arange(0, 4*p.pi, 0.1)
    y = p.cos(x)
    y1 = 2*p.cos(3*x) - 1

    # x = [0, 1, -1, 3, 4]
    # y = [5, 2, 1, 2, -1]

    p.grid()
    # p.title("Graf fcí!")
    # p.xlabel("Osa x")
    # p.ylabel("Osa y")

    p.plot(x, y, label="Divnověc")
    p.plot(x, y1, label="Divnověc jinak")

    # p.plot(x, y1, label="$y=2x+1$")
    # p.plot(x, y2, label="$y=\sqrt{x^2}$")
    # p.plot(x, y3, label="$y=x^3$")

    # p.ylim(-1, 10)
    # p.xlim(-3, 3)

    p.legend(loc="upper center")
    p.show()


if __name__ == '__main__':
    main()
