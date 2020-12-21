import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

# 加载背景
hero = pygame.image.load("./images/background.png")
screen.blit(hero, (0, 0))
# pygame.display.update()

# 游戏循环
plane = pygame.image.load("./images/me1.png")
screen.blit(plane, (200, 300))
pygame.display.update()

# 游戏循环
while True:
    pass

pygame.quit()
