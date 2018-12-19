import matplotlib.pyplot as plt
import math
import csv
import sys

class Graph(object):

    plt_kwargs = {"horizontalalignment": 'center',
                  "verticalalignment": 'center',
                  "fontsize": 15
                  }
    csv_kwargs = {"delimiter": " ",
                  "doublequote": True,
                  "lineterminator": "\n",
                  "quotechar": '"',
                  "skipinitialspace": True
                  }
    cr2 = math.pi * 2

    def __init__(self, path):
        plt.xlim([-1.3, 1.3])
        plt.ylim([-1.3, 1.3])
        plt.gca().set_aspect('equal', adjustable='box')
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['left'].set_visible(False)
        plt.gca().spines['bottom'].set_visible(False)
        plt.tick_params(labelbottom=False, labelleft=False, color='white')
        self.order = 0
        self.path = path

    def _decide_place(self, rad, scalar):
        normalize_const = math.pi / 2
        # clockwise rotation
        x = round(math.cos(-rad + normalize_const) * scalar, 4)
        y = round(math.sin(rad + normalize_const) * scalar, 4)
        return x, y

    def savefig(self,format="png", dpi=200):
        """format :
            One of the file extensions supported by the active backend.
            Most backends support png, pdf, ps, eps and svg.
        """
        formats = ("png", "pdf", "ps", "eps", "svg")
        plt.title("{} Elements Graph".format(self.order))
        plt.xlabel("(Powered by Masashi Kihara)", fontsize=8)
        if not format in formats:
            sys.stderr.writelines(
                'Formatが不正です。(Supported: png, pdf, ps, eps, svg.)')
            sys.exit(1)
        if dpi <= 0:
            sys.stderr.writelines("DPIが不正です。None または 0以下の可能性があります。")
            sys.exit(1)
        plt.savefig("graph.{}".format(format), format=format, dpi=dpi)

    def arrange(self):
        connected = list()
        try:
            with open(self.path, "r") as csv_file:
                f = csv.reader(csv_file, **self.csv_kwargs)
                for loop, row in enumerate(f):
                    if not loop:
                        self.order = [int(x) for x in row][0]
                    else:
                        connected.append([int(x) for x in row])
        except FileNotFoundError:
            sys.stderr.writelines("入力されたファイルが見つかりませんでした。")
            sys.exit(1)
        place_table = [self._decide_place((rad * self.cr2) / self.order, 1.0) for rad in range(self.order)]
        for loop in range(self.order):
            x, y = self._decide_place((loop * self.cr2) / self.order, 1.2)
            xdot, ydot = place_table[loop]
            plt.plot(xdot, ydot, 'ko', markersize=3)
            plt.text(x, y, "V" + str(loop + 1), **self.plt_kwargs)

        for loop, col in enumerate(connected):
            x, y = place_table[loop]
            for loop2, isConnect in enumerate(col):
                if not isConnect:
                    continue
                tx, ty = place_table[loop2]
                plt.plot([x, tx], [y, ty],
                            linestyle="-", color="k",  lw=0.5)


def main(path, format, dpi):
    graph = Graph(path)
    graph.arrange()
    graph.savefig(format=format, dpi=dpi)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        prog="Graph Image Printer",  # プログラム名
        usage="graph.py [[-p, --path path][-f, --format format][-d, --dpi dpi]]",  # プログラムの利用方法
		description="---help start---",
		epilog = "---help end---",
        add_help=True  # [-h],[--help]オプションをデフォルトで追加するか
    )
    # 引数の追加
    parser.add_argument("-p", "--path",  # オプション引数
                        help="input csv argment",  # 引数の説明
                        required = True,
                        default = "input.csv"
                        )
    parser.add_argument("-f", "--format",  # オプション引数
                        help="output image format argment",  # 引数の説明
                        default = "png",
                        choices=["png", "pdf", "ps", "eps", "svg"]
                        )
    parser.add_argument("-d", "--dpi",  # オプション引数
                        help="output image dpi argment",  # 引数の説明
                        default = 400,
                        type = int
                        )
    args = parser.parse_args()  # 引数の解析
    main(args.path, args.format, args.dpi)
