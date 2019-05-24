import pygame


class Plane(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./images/me1.png")
        self.hSpeed = 0
        self.vSpeed = 0
        self.rect = self.image.get_rect()
        # centerx 为当前 rect 宽度(width)的中心位置，即 width/2
        self.rect.centerx = 240
        self.rect.bottom = 600

    def update(self, *args):
        self.rect.x += self.hSpeed
        self.rect.y += self.vSpeed

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > 480:  # right 值为 x + width,即右边界的值
            self.rect.right = 480
        elif self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.bottom > 700:
            self.rect.bottom = 700

    def __del__(self):
        print("玩完...")
