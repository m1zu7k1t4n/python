# conding: utf-8


# ダンジョン形状を取得
def frame_get():
    H, W, N = [int(x) for x in input().split(" ")]
    return H, W, N


# ダンジョンマップを取得
def map_get():
    maze = []
    for _ in range(H):
        maze.append(list(input()))
    return maze


# 座標情報を取得
def position_get():
    p_x, p_y = [int(x) for x in input().split(" ")]
    p_x -= 1
    p_y -= 1
    return p_x, p_y


def maze_print(maze):
    print()
    for line in maze:
        print("".join(line))


def clear_print(clear):
    for v in clear:
        print(v)


def maze_solve_shortest(s_x, s_y, t_x, t_y, Height, Width, maze):

    INF = 100000000

    distance = [[INF for i in range(Width)] for j in range(Height)]
    step_map = [["?" for i in range(Width)] for j in range(Height)]

    def bfs():
        queue = []

        queue.insert(0, (s_x, s_y))

        distance[s_y][s_x] = 0
        step_map[s_y][s_x] = ""
        trap_word = ""

        while len(queue):
            x, y = queue.pop()

            if x == t_x and y == t_y:
                break

            for i in range(0, 4):
                nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]

                if (0 <= nx and nx < Width and 0 <= ny and ny < Height and
                        maze[ny][nx] != '#' and distance[ny][nx] == INF):
                    queue.insert(0, (nx, ny))
                    distance[ny][nx] = distance[y][x] + 1
                    if "A" <= maze[ny][nx] <= "Z":
                        distance[ny][nx] += 100
                        trap_word += maze[ny][nx]
                    step_map[ny][nx] = step_map[y][x] + ["R", "D", "L", "U"][i]

        return (step_map[t_y][t_x], distance[t_y][t_x], trap_word)

    return bfs()


def maze_solve_interigent(s_x, s_y, t_x, t_y, Height, Width, trap, trap_word, maze):

    INF = 100000000

    distance = [[INF for i in range(Width)] for j in range(Height)]
    step_map = [["?" for i in range(Width)] for j in range(Height)]
    trap_list = [x for x in trap_word]
    find_not_trap = [x.upper() for x in trap_word]

    def bfs():
        queue = []
        dist_back = distance[:]

        queue.insert(0, (s_x, s_y))
        distance[s_y][s_x] = 0
        step_map[s_y][s_x] = ""
        loop_flag = True

        while loop_flag and len(queue):
            x, y = queue.pop()

            if x == t_x and y == t_y:
                loop_flag = False

            for i in range(0, 4):
                nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]
                if (0 <= nx and nx < Width and 0 <= ny and ny < Height and maze[ny][nx] != '#' and maze[ny][nx] not in find_not_trap and distance[ny][nx] == INF):
                    queue.insert(0, (nx, ny))
                    if maze[ny][nx] in trap_list:
                        trap_list.remove(maze[ny][nx])
                        find_not_trap.remove(maze[ny][nx].upper())
                    distance[ny][nx] = distance[y][x] + 1
                    step_map[ny][nx] = step_map[y][x] + ["R", "D", "L", "U"][i]
        return (step_map[t_y][t_x], len(step_map[t_y][t_x]))

    return bfs()


# 入力される情報を全て取得
H, W, N = frame_get()
maze = map_get()
s_x, s_y = position_get()
t_x, t_y = position_get()

result_shortest = maze_solve_shortest(s_x, s_y, t_x, t_y, H, W, maze)
result_intelligent = maze_solve_interigent(
    s_x, s_y, t_x, t_y, H, W, N, result_shortest[2], maze)
if result_shortest[1] < result_intelligent[1]:
    result = result_shortest[0]
else:
    retult = result_intelligent[0]
clear_print(result)
