import pygame
from plane_sprites import *

pygame.init()

screen = pygame.display.set_mode((480, 700))

# 加载背景
bg = pygame.image.load("./images/background.png")

# 加载英雄
plane = pygame.image.load("./images/me1.png")
# 定义英雄初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

clock = pygame.time.Clock()

# 创建精灵对象
enemy = GameSprrite("./images/enemy1.png")

# 创建精灵组
enemy_group = pygame.sprite.Group(enemy)

# 游戏循环
while True:

    clock.tick(60)

    # 获取事件并处理事件
    for event in pygame.event.get():
        # 判断事件类似是不是退出事件
        if event.type == pygame.QUIT:
            print("退出游戏")
            pygame.quit()
            exit()

    # 更新坐标
    hero_rect.y -= 1
    if hero_rect.bottom <= 0:
        hero_rect.y = 700
    # 重新绘制背景图片，防止出现残影
    screen.blit(bg, (0, 0))
    # 屏幕加载英雄飞机
    screen.blit(plane, hero_rect)
    # 刷新
    pygame.display.update()

    # 让精灵组调用update方法更新内部所有精灵的坐标
    enemy_group.update()
    # 让精灵组调用draw方法，让screen对精灵进行blit
    enemy_group.draw(screen)
    # 投影
    pygame.display.update()

pygame.quit()
