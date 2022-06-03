import pylab as p
import random
def main():
    # 1
    # x = p.arange(-20, 20, 1)
    # y = x**3 - 2*x**2 + x-1
    # p.plot(x, y, "go")
    # p.plot(x, y, "g-o")
    # p.show()

    # 2
    # y = []
    # for i in range(0, 100):
    #     y.append(random.randint(0, 20))
    # x = p.arange(0, 100)
    # p.plot(x, y, "rs")
    # p.show()

    # 3
    bod_a_x = int(input("Zadejte souřadnici x bodu A: "))
    bod_a_y = int(input("Zadejte souřadnici y bodu A: "))
    bod_b_x = int(input("Zadejte souřadnici x bodu B: "))
    bod_b_y = int(input("Zadejte souřadnici y bodu B: "))
    bod_c_x = int(input("Zadejte souřadnici x bodu C: "))
    bod_c_y = int(input("Zadejte souřadnici y bodu C: "))

    x = [bod_a_x, bod_b_x, bod_c_x, bod_a_x]
    y = [bod_a_y, bod_b_y, bod_c_y, bod_a_y]
    p.plot(x, y)
    p.show()

if __name__ == '__main__':
    main()