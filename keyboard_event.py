"""
键盘监听
"""
import pygame
import game_sprite
import plane


pygame.init()

bg = pygame.image.load('./images/background.png')

windowSize = (480, 700)
screen = pygame.display.set_mode(windowSize)

screen.blit(bg, (0, 0))
pygame.display.update()

clock = pygame.time.Clock()

# 创建飞机，并添加到精灵组中，自动重绘
hero = plane.Plane()
# 创建精灵图"组"，该对象可以调用 update, draw 方法重绘
spriteGroup = pygame.sprite.Group(hero)
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

    # 键盘监听事件处理
    # 获取所有键盘监听（当然也可以通过 "pygame.event" 处理，会有差异）
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        hero.hSpeed = 2
    elif pressed_keys[pygame.K_LEFT]:
        hero.hSpeed = -2
    elif pressed_keys[pygame.K_UP]:
        hero.vSpeed = -2
    elif pressed_keys[pygame.K_DOWN]:
        hero.vSpeed = 2
    else:
        hero.hSpeed = 0
        hero.vSpeed = 0

    screen.blit(bg, (0, 0))

    # 重绘
    spriteGroup.update()
    spriteGroup.draw(screen)
    # 刷新
    pygame.display.update()
