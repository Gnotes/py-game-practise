"""
sprite.Sprite 对象使用
"""

import pygame
import random


class GameSprite(pygame.sprite.Sprite):
    """精灵图使用"""

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
            y = random.randint(0, 600)
            rect.x = x
            rect.y = y
            self.rect = rect
        else:
            self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        """更新图片位置"""
        self.rect.y += self.speed

        if self.rect.y > 700:
            self.rect.y = 0
