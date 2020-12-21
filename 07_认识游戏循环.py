import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

# 加载背景
hero = pygame.image.load("./images/background.png")
screen.blit(hero, (0, 0))

# 游戏循环
plane = pygame.image.load("./images/me1.png")
screen.blit(plane, (200, 300))

# 页面刷新
pygame.display.update()

clock = pygame.time.Clock()

# 游戏循环
while True:
    clock.tick(1)
    print("1")

pygame.quit()
