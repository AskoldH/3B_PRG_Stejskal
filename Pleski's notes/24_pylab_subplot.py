import pylab as p

def main():
    # p.subplot(2, 2, 1)
    # p.plot([1, 2, 3, 5], linewidth=4)
    # p.plot([3, 1, 5, 2])
    #
    # p.subplot(2, 2, 2)
    # p.plot([1, 2, 3, 5], linewidth=4)
    # p.plot([3, 1, 5, 2])
    #
    # p.subplot(2, 2, 3)
    # p.plot([1, 2, 3, 5], linewidth=4)
    # p.plot([3, 1, 5, 2])
    #
    # p.subplot(2, 2, 4)
    # p.plot([1, 2, 3, 5], linewidth=4)
    # p.plot([3, 1, 5, 2])

    # 1
    # x = p.arange(-50, 51, 1)
    # y = abs(x-1) + 1
    # p.subplot(2, 1, 1)
    # p.plot(x, y, "g")
    #
    # p.subplot(2, 1, 2)
    # p.fill(x, y, "r")
    # p.plot(x, y, "r")

    # 2
    # x = p.arange(0, 2*p.pi+0.1, 0.1)
    # y1 = p.sin(x)
    # y2 = p.cos(x)
    # p.plot(x, y1)
    # p.plot(x, y2)
    # p.fill_between(x, y1, y2, facecolor="r", where=y2>y1)
    # p.show()

    # 3
    # x = p.arange(0, 2*p.pi+0.1, 0.1)
    # y1 = p.sin(2*x)
    # y2 = p.cos(x)
    # p.plot(x, y1, "#C312FC")
    # p.plot(x, y2, "#C312FC")
    # p.grid()
    # p.text(2, 0, "Popisek", fontsize="15", color="r")
    # p.fill_between(x, y1, y2, racecolor="#C312FC")

    # 4
    x = p.arange(-2, 4.2, 0.2)
    y1 = -(x-2)**2+4
    y2 = x
    p.plot(x, y1, "g--", label='Grag 1')
    p.plot(x, y2, "r", label='Grag 2')
    p.fill_between(x, y1, y2, facecolor="b", where=y1>y2)
    p.annotate('Vybarvená plocha', xy=(1.6, 1), xytext=(2, -4),
             arrowprops=dict(facecolor='b'))
    p.grid()
    # p.text(-1, -6, 'Zahlá čára', fontsize="10", color="g")
    # p.text(-1, 0, 'Rovná čára', fontsize="10", color="r")
    p.legend(labels=["Graf 1", "Graf 2"])
    p.show()



if __name__ == '__main__':
    main()