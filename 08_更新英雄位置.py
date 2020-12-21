import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

# 加载背景
bg = pygame.image.load("./images/background.png")
# screen.blit(hero, (0, 0))

# 加载英雄
plane = pygame.image.load("./images/me1.png")
# 定义英雄初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)
# screen.blit(plane, (200, 300))

# 页面刷新
pygame.display.update()

clock = pygame.time.Clock()

# 游戏循环
while True:

    clock.tick(60)
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

pygame.quit()
