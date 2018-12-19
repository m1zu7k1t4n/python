import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480)

white = (255, 255, 255)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("HELLOWORLD")

# フォントの作成
sysfont = pygame.font.SysFont(None, 80)
# テキストを描画したSurfaceを作成
font1 = sysfont.render("helloworld 1", False, (0, 0, 0))
font2 = sysfont.render("helloworld 2", True, (0, 0, 0))
font3 = sysfont.render("helloworld 3", True, (255, 0, 0), (255, 255, 0))
framerate = 30
clock = pygame.time.Clock()

while True:
    screen.fill(white)
    pressed_keys = pygame.key.get_pressed()
    # 押されているキーに応じて画像を移動
    font4 = sysfont.render(str(len(pressed_keys)), True, (0, 0, 0))

    # テキストを描画
    if pressed_keys[K_m]:
        screen.blit(font4, (20, 50))
    # screen.blit(font1, (20,50))
    # screen.blit(font2, (20,150))
    # screen.blit(font3, (20,250))
    if pressed_keys[K_2]:
        screen.blit(font4, (20, 100))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    clock.tick(framerate)
