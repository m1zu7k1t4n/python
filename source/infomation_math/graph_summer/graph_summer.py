import matplotlib.pyplot as plt
import math
import csv

kwargs = {"horizontalalignment": 'center',
          "verticalalignment": 'center',
          "fontsize": 15
          }
csv_kwargs = {"delimiter": " ",
              "doublequote": True,
              "lineterminator": "\n",
              "quotechar": '"',
              "skipinitialspace": True
              }
pi2 = math.pi * 2


def chara_spot(rad, long):
    """
    rad: float , long: float -> (x: float, y: float)
    """
    bias = math.pi / 2
    return (round(math.cos(-rad + bias) * long, 4),
            round(math.sin(rad + bias) * long, 4))


def main(path):
    order = 0
    connected = list()
    with open(path, "r") as csv_file:
        f = csv.reader(csv_file, **csv_kwargs)
        for loop, xx in enumerate(f):
            if not loop:
                order = [int(x) for x in xx][0]
            else:
                connected.append([int(x) for x in xx])

    plot_table = [chara_spot((rad * pi2)/order, 1.0) for rad in range(order)]
    for loop in range(order):
        x, y = chara_spot((loop * pi2)/order, 1.2)
        xdot, ydot = plot_table[loop]
        plt.plot(xdot, ydot, 'ko', markersize=3)
        plt.text(x, y, str(loop + 1), **kwargs)

    for loop, match_vector in enumerate(connected):
        here_x, here_y = plot_table[loop]
        for loop2, isConnect in enumerate(match_vector):
            if not isConnect:
                continue
            target_x, target_y = plot_table[loop2]
            plt.plot([here_x, target_x], [here_y, target_y],
                     linestyle="-",  lw=0.5)

    plt.xlim([-1.3, 1.3])
    plt.ylim([-1.3, 1.3])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.tick_params(labelbottom=False, labelleft=False, color='white')
    plt.savefig("graph_summer.png", format="png", dpi=2000)
    plt.show()


if __name__ == '__main__':
    import sys
    try:
        path = sys.argv[1]
    except IndexError:
        path = "summer.csv"
    main(path)
