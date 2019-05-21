"""
创建窗口
"""

import pygame
import time

pygame.init()

# 指定窗口宽高，是一个元组类型
windowSize = (480, 700)
# 创建窗口
screen = pygame.display.set_mode(windowSize)
# 暂时写一个循环挂起窗口，防止直接 quit，为了方式宕机使用了 time.sleep
# while True:
#     pass

# 睡眠10s
time.sleep(10)

pygame.quit()
