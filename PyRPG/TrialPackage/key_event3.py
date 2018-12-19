# _*_coding:utf-8_*_
# キー操作する
import sys
import pygame
from pygame.locals import *


def delta_amp(delta):
    if delta[0] < 300:
        delta[0] += 1


def delta_get(delta): return delta[0] // 30


pygame.init()  # pygameの初期化
screen = pygame.display.set_mode((400, 300))  # ウィンドウの大きさ
pygame.display.set_caption("PyGame")  # タイトルバー
image = pygame.image.load("python.png")  # 画像を読み込む

pygame.key.set_repeat(5, 5)  # キーの押下と押しっぱなしの取得(追加したとこ)
position = [200, 150]  # 座標を配列に[x座標, y座標](追加したとこ)


# mainループ
def main():
    delta = [0]

    while True:
        screen.fill((0, 0, 0))  # ウィンドウの背景色
        # イベントの取得
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()  # 閉じるボタンが押されたらプログラムを終了
                sys.exit

            # キー操作(追加したとこ)
            elif event.type == KEYDOWN:
                delta_amp(delta)
                if event.key == K_LEFT:
                    position[0] -= delta_get(delta)
                elif event.key == K_RIGHT:
                    position[0] += delta_get(delta)
                elif event.key == K_UP:
                    position[1] -= delta_get(delta)
                elif event.key == K_DOWN:
                    position[1] += delta_get(delta)
            else:
                delta[0] = 0

        # 画面の端に行ったら反対から出るようにする(追加したとこ)
        position[0] = position[0] % 400
        position[1] = position[1] % 300

        # 画像の描画位置(追加したとこ)
        rect = image.get_rect()
        rect.center = position

        # 画像の描画
        screen.blit(image, rect)
        pygame.display.update()


if __name__ == '__main__':
    main()
