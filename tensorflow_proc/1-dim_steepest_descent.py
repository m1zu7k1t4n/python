import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import *
from matplotlib import animation as ani

# set graph range
x_low = -3
x_high = 3
y_low = -3
y_high = 3

# set field
X = np.linspace(x_low, x_high, 1000)
Y = np.linspace(y_low, y_high, 1000)
X, Y = np.meshgrid(X, Y)

# set parameters
Z = 3 * X ** 2 - 5 * Y ** 2 - 6 * X * Y


def get_grad_vec(x, y):
    grad_x = 6 * x - 6 * y
    grad_y = 10 * y - 6 * x
    return [grad_x, grad_y]


def calc_2val_norm(init_x=3, init_y=3, learning_ratio=.1, precision=3):
    list_xs = []
    list_ys = []
    list_nxs = []
    list_nys = []
    list_diff = []
    xs = init_x
    ys = init_y
    i = 0
    for i in range(100):

        grad_vec = get_grad_vec(xs, ys)
        n_xs = xs + learning_ratio * grad_vec[0]
        n_ys = ys + learning_ratio * grad_vec[1]

        list_xs.append(xs)
        list_ys.append(ys)
        list_nxs.append(n_xs)
        list_nys.append(n_ys)

        # judge convergence
        diff = np.sqrt(grad_vec[0]**2 + grad_vec[1]**2)
        list_diff.append(diff)
        if diff < 0.1**precision:
            print("break")
            break

        xs = n_xs
        ys = n_ys

    ret_dict = {}
    ret_dict['num'] = i + 1
    ret_dict['list_xs'] = list_xs
    ret_dict['list_ys'] = list_ys
    ret_dict['list_nxs'] = list_nxs
    ret_dict['list_nys'] = list_nys
    ret_dict['list_diff'] = list_diff

    return ret_dict


def animate(i):
    list_xs = ret_dict['list_xs']
    list_ys = ret_dict['list_ys']
    list_nxs = ret_dict['list_nxs']
    list_nys = ret_dict['list_nys']
    list_diff = ret_dict['list_diff']

    if i == 0:
        plt.scatter(list_xs[i], list_ys[i], s=20, c="b", alpha=0.6)
        plt.title("n %2d, x %.5f, y %.5f, diff %.5f" %
                  (i, list_xs[i], list_ys[i], list_diff[i]))
    else:
        # draw graph
        plt.scatter(list_xs[i - 1], list_ys[i - 1], s=20, c="b", alpha=0.6)
        plt.plot([list_xs[i - 1], list_nxs[i - 1]],
                 [list_ys[i - 1], list_nys[i - 1]])
        plt.title("n %2d, x %.5f, y %.5f, diff %.5f" %
                  (i, list_xs[i - 1], list_ys[i - 1], list_diff[i - 1]))


fig = plt.figure(figsize=(6, 4))
ret_dict = calc_2val_norm(init_x=0, init_y=-3, learning_ratio=.1)
interval = [x ** 2 for x in range(10)]
CS = plt.contour(X, Y, Z, interval)
plt.clabel(CS, inline=1, fontsize=10)
print(ret_dict['num'])
anim = ani.FuncAnimation(fig, animate, frames=ret_dict['num'], blit=True)
anim.save('quadratic_decent_anim.mp4', fps=2.5)

clip = VideoFileClip("quadratic_decent_anim.mp4")
clip.write_gif("quadratic_decent_anim.gif")
