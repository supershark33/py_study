import pygame
from plane_sprites import *


class PlaneGame(object):

    def __init__(self):
        print("游戏初始化")
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 初始化精灵和精灵组
        self.__create_sprites()
        # 创建敌机定时器
        self.__init_evnet_timer()

    def start_game(self):
        print("游戏开始...")
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 时间监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新/绘制精灵
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    def __create_sprites(self):

        # 创建一个背景精灵
        bg1 = BackGround()
        # 创建另外背景精灵
        bg2 = BackGround(True)
        # 创建精灵组
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机精灵组，具体的敌机精灵通过add方法进行添加
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == CREAT_ENEMY_EVENT:
                # 创建敌机精灵
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        # 使用键盘模块监听键盘按键事件
        keys_processed = pygame.key.get_pressed()
        if keys_processed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_processed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()

    @staticmethod
    def __init_evnet_timer():
        pygame.time.set_timer(CREAT_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)


if __name__ == '__main__':
    game = PlaneGame()

    game.start_game()
