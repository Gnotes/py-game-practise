"""
绘制图片
"""
import pygame

pygame.init()

screenSize = (480, 700)
screen = pygame.display.set_mode(screenSize)

# 加载图片
bg = pygame.image.load('./images/background.png')
# 绘制图像
screen.blit(bg, (0, 0))
plane = pygame.image.load('./images/me1.png')
position = plane.get_rect()
screen.blit(plane, (180, 500))

# 更新窗口
pygame.display.update()

# 不明白，先这样用吧
# https://www.jianshu.com/p/a8482a040e6d
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()
