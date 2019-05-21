
"""
移动图片
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
screen.blit(plane, (180, 500))

# 更新窗口
pygame.display.update()

# 创建刷新频率时钟对象
clock = pygame.time.Clock()
# 创建飞机位置矩形对象
position = pygame.Rect(180, 500, 102, 126)

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    clock.tick(40)  # 一秒刷新40次
    position.y -= 10  # 每次向上移动 10px
    if position.y <= -126:  # 移出屏幕时，重置到屏幕底部
        position.y = 700

    screen.blit(bg, (0, 0))  # 重绘背景图，重要哟！！！可以注释掉试试.
    screen.blit(plane, position)  # 重绘飞机

    pygame.display.update()  # 刷新


