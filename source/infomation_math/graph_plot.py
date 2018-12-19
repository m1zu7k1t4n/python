import matplotlib.pyplot as plt
import csv


def read_csv(path):
    with open(path, "r", encoding="utf-8", errors="", newline="") as csv_file:
            f = csv.reader(csv_file,
                           delimiter=",",
                           doublequote=True,
                           lineterminator="\n",
                           quotechar='"',
                           skipinitialspace=True
                           )
            number = [int(x) for x in next(f)]


plt.title("graph")
plt.xlim(-0.7,0.7)
plt.ylim(-0.7,0.7)

if __name__ == '__main__':
    import sys
    args = sys.argv
    if len(args) != 1:
        for path in args[1:]:
            isGraph(path)
    else:
        isGraph("input.csv")
