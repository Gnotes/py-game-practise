"""
sprite.Sprite 对象使用
"""

import pygame
import random


class GameSprite(pygame.sprite.Sprite):
    """精灵图使用"""

    count = 0

    def __init__(self, image, speed=1, random_position=True):
        super().__init__()
        """
        下边"属性" 都是父类需要用到的，不是随便定义的
        可以在 pygame.sprite.Group 这个类的 draw 方法查看到
        """
        self.image = pygame.image.load(image)

        # 随机生成敌机位置
        if random_position:
            rect = self.image.get_rect()
            x = random.randint(0, 450)
            rect.x = x
            # bottom = y + height,如果 bottom = 0,即 y = -height
            rect.bottom = 0
            self.rect = rect
        else:
            self.rect = self.image.get_rect()
        self.speed = speed
        self.id = GameSprite.count
        GameSprite.count += 1

    def update(self):
        """更新图片位置"""
        self.rect.y += self.speed

        if self.rect.y > 700:
            # 超出屏幕调用Sprite 的kill 方法，会从精灵组中移除，并移除内存占用
            self.kill()

    def __del__(self):
        """__del__
        是声明周期函数，在对象被销毁的时候会被调用
        """
        print('Im done, %d' % self.id)
