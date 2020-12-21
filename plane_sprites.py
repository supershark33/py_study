import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 定义刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREAT_ENEMY_EVENT = pygame.USEREVENT
# 发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT+1


class GameSprrite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        """
        初始化方法
        :param image_name:图片路径
        :param speed:速度
        """
        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        """
        更新精灵坐标
        """
        # 在屏幕的垂直方向上面移动
        self.rect.y += self.speed


class BackGround(GameSprrite):
    """游戏背景精灵"""

    def __init__(self, out=False):
        super().__init__("./images/background.png")
        # 判断是否为屏幕外初始化
        if out:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类的方法
        super().update()
        # 判断是否移出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprrite):

    def __init__(self):
        super().__init__("./images/enemy1.png")
        # 指定敌机的随机速度
        self.speed = random.randint(1, 3)
        # 敌机初始位置在上方，避免突兀
        self.rect.bottom = 0
        # 水平方向的初始位置
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)

    def update(self):
        super().update()
        # 敌机飞出，然后销毁
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()


class Hero(GameSprrite):

    def __init__(self):
        # 英雄的初始速度为0
        super().__init__("./images/me1.png", 0)

        # 设置英雄初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹的空精灵组
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        for index in (0, 1, 2):
            bullet = Bullet()
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.y = self.rect.y - 20 * index
            self.bullet_group.add(bullet)


class Bullet(GameSprrite):

    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()