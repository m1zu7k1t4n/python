# coding: utf-8

import pygame
from pygame.locals import *
import sys
from collections import deque

BLACK = (0, 0, 0)
GRAY = (198, 198, 198)
YELLOW = (214, 203, 2)
isGen = True
status = "bfs"


def maze_gen():
    maze_base = [["." for x in range(126)] for y in range(70)]
    for y in range(1, 70, 2):
        for x in range(1, 126, 2):
            maze_base[y][x] = "#"
    d = "."
    o = "#"
    maze= [[d,d,d,d],
           [d,o,o,d],
           [d,o,o,o],
           [d,d,d,d]]
    return maze


def maze_bfs(s_x, s_y, t_x, t_y, maze):
    Width = len(maze[0])
    Height = len(maze)
    isEnd = False

    INF = 100

    distance = [[INF for i in range(Width)] for j in range(Height)]
    step_map = [[0 for i in range(Width)] for j in range(Height)]

    queue = deque()

    queue.appendleft((s_x, s_y))

    distance[s_y][s_x] = [(s_x, s_y)]
    step_map[s_y][s_x] = 1

    while len(queue):
        x, y = queue.pop()

        if x == t_x and y == t_y:
            isEnd = True
            break

        for i in range(0, 4):
            nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]

            if (0 <= nx and nx < Width and 0 <= ny and ny < Height and
                        maze[ny][nx] != '#' and distance[ny][nx] == INF):
                queue.appendleft((nx, ny))
                step_map[ny][nx] = 1
                distance[ny][nx] = distance[y][x][:]
                distance[ny][nx].append((nx, ny))
        yield (step_map, distance[ny][nx], isEnd)


def maze_dfs(s_x, s_y, t_x, t_y, maze):
    Width = len(maze[0])
    Height = len(maze)
    isEnd = False
    INF = 100

    distance = [[INF for i in range(Width)] for j in range(Height)]
    step_map = [[0 for i in range(Width)] for j in range(Height)]

    queue = []

    queue.append((s_x, s_y))

    distance[s_y][s_x] = [(s_x, s_y)]
    step_map[s_y][s_x] = 1

    while len(queue):
        x, y = queue.pop()

        if x == t_x and y == t_y:
            isEnd = True
            break

        for i in range(0, 4):
            nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]

            if (0 <= nx and nx < Width and 0 <= ny and ny < Height and
                        maze[ny][nx] != '#' and distance[ny][nx] == INF):
                queue.append((nx, ny))
                step_map[ny][nx] = 1
                distance[ny][nx] = distance[y][x][:]
                distance[ny][nx].append((nx, ny))
        yield (step_map, distance[ny][nx], isEnd)
    yield (step_map, distance[ny][nx], isEnd)


def maze_get_write(step_map):
    x = 0
    y = 0
    for Height in step_map:
        for Width in Height:
            if Width == 1:
                pygame.draw.rect(screen, GRAY, Rect((10 + 10 * x), (10 + 10 * y), (20 + 10 * x), (20 + 10 * y)))
            x += 1
        y += 1


def maze_clear_write(distance):
    for x, y in distance:
        pygame.draw.rect(screen, YELLOW, Rect((10 + 10 * x), (10 + 10 * y), (20 + 10 * x), (20 + 10 * y)))


SCR_X, SCR_Y = (1280, 720)

pygame.init()
screen = pygame.display.set_mode((SCR_X, SCR_Y))
pygame.display.set_caption("maze_animetion")

fps = pygame.time.Clock()

while True:
    fps.tick(60)

    screen.fill(BLACK)
    if isGen:
        maze = maze_gen()
        pygame.time.delay(2000)
        isGen = False
        if status == "wait_dfs":
            status = "dfs"
        if status == "wait_bfs":
            status = "bfs"

    if status == "bfs":
        maze_data = maze_bfs(0, 0, 126, 70, maze)
        status == "wait_dfs"
    if status == "dfs":
        maze_data = maze_dfs(0, 0, 126, 70, maze)
        status == "wait_bfs"

    step_map, distance, isEnd = next(maze_data)
    maze_get_write(step_map)
    if isEnd:
        maze_clear_write(distance)
        isGen = True

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
