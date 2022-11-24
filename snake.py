import pygame as pg
import random as rand


FPS = 6.0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 64)
W = 800
H = 800

sc = pg.display.set_mode((W, H))
clock = pg.time.Clock()

dirs = {'W': True, 'S': True, 'A': True, 'D': True, }  # Для того щоб запобігти пересуваню змійки в бік свого хвосту

SIZE = 50  # розмір однієї клітинки змійки
score = 0
y = rand.randrange(0, W, SIZE)  # рандомні координати для змійки
x = rand.randrange(0, H, SIZE)
apple = (rand.randrange(0, H, SIZE), rand.randrange(0, H, SIZE))  # рандомні координати для яблука
length = 1
dx, dy = 0, 0
snake = [(x, y)]  # кортеж із координатами змійки


runGame = True
while runGame:
    clock.tick(FPS)

    # наступний блок if-elif-else перевіряє чи вийшла змійка за ігрову зону
    if x < 0:
        x = H
    elif x > H:
        x = 0 - SIZE
    elif y < 0:
        y = W
    elif y > W:
        y = 0 - SIZE

    # заливає вікно чорним кольором
    sc.fill(BLACK)

    for i in pg.event.get():
        if i.type == pg.QUIT:
            runGame = False

    # Малювання змійки та яблука
    [(pg.draw.rect(sc, GREEN, (i, j, SIZE, SIZE))) for i, j in snake]
    pg.draw.rect(sc, RED, (*apple, SIZE, SIZE))

    # Наступний блок відповідає за переміщення змійки по ігровій зоні
    x += dx*SIZE
    y += dy*SIZE
    snake.append((x, y))
    snake = snake[-length:]

    # Перевіряє чи торкається голова змійки яблука
    if snake[-1] == apple:
        apple = (rand.randrange(0, H, SIZE), rand.randrange(0, H, SIZE))
        length += 1
        score += 1
        if length % 2 == 0:
            FPS += 0.5

    # Перевіряє чи не доторкнулась змійка до свого хвоста
    if len(snake) != len(set(snake)):
        dx, dy = 0, 0
        dirs = {'W': False, 'S': False, 'A': False, 'D': False}

    pressed_keys = pg.key.get_pressed()

    # Наступний блок перевіряє натискання клавіш та зміннює відповідні значення завдяки яким змійка почне рухатись
    # а також забороняє змійці рухатись у зворотньому русі
    if pressed_keys[pg.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
    if pressed_keys[pg.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
    if pressed_keys[pg.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
    if pressed_keys[pg.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True, }
    if pressed_keys[pg.K_j]:
        dx, dy = 0, 0
        x = H/2-SIZE
        y = W/2-SIZE
        dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
        length = 1
        FPS = 6.0

    pg.display.flip()

pg.quit()
