import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_game):
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings  # 注意此处的ai，可见alien_invasion.py，是将AlienInvasion()传递给了它

        # 加载外星人突袭那个并设置其rect属性。
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人都出现在屏幕左上角附近
        self.rect.x = self.rect.width   # 左边距设置为外星人宽度
        self.rect.y = self.rect.height  # 上边距设置为外星人高度

        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)     # 更关注水平速度，因此记录水平位置

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:  # 判断是否到左边缘或右边缘
            return True

    def update(self):
        """向左或向右移动外星人"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)  # 移动量为速度和方向的乘积，因此有正负
        self.rect.x = self.x   # self.x可以储存小数值，再将其更新外星人的rect的位置

