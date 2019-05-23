"""
调用 sprite 自动重绘图片
"""
import pygame
import game_sprite


pygame.init()

bg = pygame.image.load('./images/background.png')

windowSize = (480, 700)
screen = pygame.display.set_mode(windowSize)

screen.blit(bg, (0, 0))

plane = pygame.image.load('./images/me1.png')
screen.blit(plane, (180, 500))

position = pygame.Rect(180, 500, 102, 126)
pygame.display.update()

clock = pygame.time.Clock()

# 创建敌机数组
# enemyGroup = []
# for i in range(0, 10):
#     enemy = game_sprite.GameSprite("./images/enemy1.png")  # 创建敌机对象
#     enemyGroup.append(enemy)  # 添加到数据中

# 创建精灵图"组"，该对象可以调用 update, draw 方法重绘
spriteGroup = pygame.sprite.Group()
# 创建用户事件对象变量
EVENT_CREATE_ENEMY = pygame.USEREVENT
# 使用计时器，每秒触发一次用户事件
pygame.time.set_timer(EVENT_CREATE_ENEMY, 1000)


while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    elif event.type == EVENT_CREATE_ENEMY:  # 判断，如果是用户事件，就创建敌机
        enemy = game_sprite.GameSprite("./images/enemy1.png")  # 创建敌机对象
        spriteGroup.add(enemy)  # 添加到数据中

    clock.tick(40)
    screen.blit(bg, (0, 0))

    position.y -= 5
    if position.y <= -126:
        position.y = 700

    # 重绘飞机
    screen.blit(plane, position)
    # 重绘敌机
    spriteGroup.update()
    spriteGroup.draw(screen)
    # 刷新
    pygame.display.update()
