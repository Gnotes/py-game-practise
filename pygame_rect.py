"""
使用 pygame.Rect 类生成一个矩形区域
"""
import pygame


rect = pygame.Rect(100, 100, 120, 150)

print("x: %d, y: %d" % (rect.x, rect.y))
print("width: %d, height: %d" % (rect.width, rect.height))
print("width: %d, height: %d" % rect.size)  # rect.size 是一个元组
