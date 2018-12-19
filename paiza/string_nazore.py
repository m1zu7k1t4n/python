# coding: utf-8


# ダンジョンマップを取得
def map_get(M):
    maze = []
    for _ in range(M):
        maze.append(list(input()))
    return maze

def solve(s_x, s_y, size, strings, maze):

    INF = 100000000

    distance = [[INF for i in range(size)] for j in range(size)]
    step_map = [["?" for i in range(size)] for j in range(size)]

    def bfs():
        queue = []

        queue.insert(0, (s_x, s_y))

        distance[s_y][s_x] = 0
        step_map[s_y][s_x] = ""
        can_clear = False

        while len(queue):
            x, y = queue.pop()

            if step_map[y][x] == strings:
                can_clear = True
                break

            for i in range(0, 4):
                nx, ny = x + (1, 0, -1, 0)[i], y + (0, 1, 0, -1)[i]

                if (0 <= nx and nx < Width and 0 <= ny and ny < Height and
                        maze[ny][nx] != '#' and distance[ny][nx] == INF):
                    queue.insert(0, (nx, ny))
                    distance[ny][nx] = distance[y][x] + 1
                    if "A" <= maze[ny][nx] <= "Z":
                        distance[ny][nx] += 100
                        trap_word += maze[ny][nx]
                    step_map[ny][nx] = step_map[y][x] + ["R", "D", "L", "U"][i]

        return can_clear

    return bfs()

M = int(input())