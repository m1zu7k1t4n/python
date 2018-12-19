# config: utf-8
import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480)

#Pygameを初期化
pygame.init()
#SCREEN_SIZEの画面を作成
screen = pygame.display.set_mode(SCREEN_SIZE)
#タイトルバーの文字列をセット
pygame.display.set_caption("ウィンドウを作成")
while True:
    screen.fill((0, 255, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()